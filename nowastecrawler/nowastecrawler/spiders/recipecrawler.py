import scrapy
import json
from pydispatch import dispatcher
from scrapy import signals
from scrapy.http.request import Request

#  list of ingredients
ingredient_list = []


class RecipeSpider(scrapy.Spider):
    name = "recipes"
    start_urls = ["https://www.przepisy.pl/skladniki/kasza"]

    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self):
        with open("ingredients_dict.json", "w") as f:
            json.dump(ingredient_list, f, ensure_ascii=False)

    def parse(self, response):

        if response.css("div.person-count::text") == []:
            dish_list = response.css("div.recipe-box")
            for dish in dish_list:
                next_url_href = response.urljoin(dish.css("a ::attr(href)").get())
                yield scrapy.Request(
                    next_url_href, callback=self.parse, dont_filter=True
                )
            # next page
            try:
                next_page_with_recipes = response.css(
                    "a.pagination__btn--arrow--right"
                ).attrib["href"]
                next_url_with_recipes_href = response.urljoin(next_page_with_recipes)
                yield scrapy.Request(
                    next_url_with_recipes_href, callback=self.parse, dont_filter=True
                )
            except:
                pass  # end

        else:
            dish_size = response.css("div.person-count::text").get()
            dish_name = response.css("title::text").get()
            ingredients = response.css("div.ingredients-list-content-item")
            ingredients_list = []
            for ingredient in ingredients:
                ingredient_name = ingredient.css("::text").get()
                ingredient_name = ingredient_name.strip().lower()
                #  change name to singular
                if ingredient_name not in ingredient_list:
                    ingredient_list.append(ingredient_name)  # missing new value
                ingredient_quantity = ingredient.css(".quantity span::text").get()
                ingredients_list.append(
                    {
                        "name": ingredient_name,
                        "quantity": ingredient_quantity.strip(),
                    }
                )
            steps = response.css("div.step-info")
            step_list = []
            for step in steps:
                step_list.append(step.css("p::text").get())
            yield {
                "title": dish_name,
                "servings": dish_size,
                "directions": " ".join(step_list),
                "ingredients": ingredients_list,
                "description": None,
                "imgUrl": None
            }
