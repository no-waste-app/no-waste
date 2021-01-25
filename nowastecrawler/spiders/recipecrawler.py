import scrapy
from scrapy.http.request import Request

class RecipeSpider(scrapy.Spider):
    name = "recipes"
    start_urls = [
        'https://www.przepisy.pl/skladniki/kasza'
    ]

    def parse(self, response):

        if response.css('div.person-count::text') == []:
            dish_list = response.css('div.recipe-box')
            for dish in dish_list:
                next_url_href = response.urljoin(dish.css('a ::attr(href)').get())
                yield scrapy.Request(next_url_href, callback=self.parse, dont_filter=True)
            # next page
            try:
                next_page_with_recipes = response.css('a.pagination__btn--arrow--right').attrib['href']
                next_url_with_recipes_href = response.urljoin(next_page_with_recipes)
                yield scrapy.Request(next_url_with_recipes_href, callback=self.parse, dont_filter=True)
            except:
                pass  # end


        else:
            dish_size = response.css('div.person-count::text').get()
            dish_name = response.css('title::text').get()
            ingredients = response.css('div.ingredients-list-content-item')
            ingredients_list = []
            for ingredient in ingredients:
                ingredient_name = ingredient.css('::text').get()
                ingredient_quantity = ingredient.css('.quantity span::text').get()
                ingredients_list.append({
                    'ingredient_name': ingredient_name,
                    'ingredient_quantity': ingredient_quantity
                })
            steps = response.css('div.step-info')
            step_list = []
            for step in steps:
                step_list.append(step.css('p::text').get())
            yield{
                'dish_name': dish_name,
                'dish_size': dish_size,
                'steps': ' '.join(step_list),
                'ingredients': ingredients_list
            }
