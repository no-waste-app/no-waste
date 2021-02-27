import pymongo  # mongo database
import json
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")


def main():
    #  local db
    client = pymongo.MongoClient(DATABASE_HOST, int(DATABASE_PORT))  # local mongo database

    db = client.RecipeDB

    # RECIPES

    collection_name = db["recipes"]  # recipes collection

    if collection_name.estimated_document_count() == 0:
        with open('../recipes.json') as file:
            collection_name.insert_many([{'recipe': x} for x in json.load(file)]) #  adding recipes
        pass

    #  test first random element
    print(collection_name.find_one())

    # INGREDIENTS

    collection_name = db["ingredients"]  # ingredients collection

    if collection_name.estimated_document_count() == 0:
        with open('../ingredients_dict.json') as file:
            collection_name.insert_many([{'ingredient_name': x} for x in json.load(file)]) #  adding ingredients to collection

    #  test first random element
    print(collection_name.find_one())



if __name__ == "__main__":
    main()
