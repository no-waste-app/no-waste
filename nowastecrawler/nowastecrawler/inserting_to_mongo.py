import pymongo  # biblioteka mongo
import pandas as pd  # python -m pip install pandas
import json

DATABASE_HOST = "localhost"
DATABASE_PORT = 27017


def main():
    #  local db
    client = pymongo.MongoClient(DATABASE_HOST, DATABASE_PORT)  # lokalne mongo

    db = client.RecipeDB

    # RECIPES

    collection_name = db["recipes"]  # recipes collection

    if collection_name.estimated_document_count() == 0:
        records = pd.read_json('../recipes.json')
        collection_name.insert_many(records.to_dict('records'))

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
