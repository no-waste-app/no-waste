from scrapy.cmdline import execute
import sys
sys.argv = ['scrapy', 'crawl', 'recipes', '-o', 'recipes.json']
execute()
