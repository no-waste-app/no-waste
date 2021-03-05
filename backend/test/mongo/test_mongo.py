import unittest
from unittest.mock import MagicMock, patch


class MongoTest(unittest.TestCase):

    def test_service_products(self):
        # given
        from application.service import NoWasteService
        mongo_mock = MagicMock()
        service = NoWasteService(mongo_mock)

        # and
        mongo_mock.db.ingredients.find.return_value = [{"a": "b"}]
        query = "Cos"

        # when
        result = service.products(query)

        # then
        self.assertEqual(result, [{"a": "b"}])

        # and
        mongo_mock.db.ingredients.find.assert_called_with({"ingredient_name": {'$regex': query}})

    def test_service_recipe_list(self):
        # given
        from application.service import NoWasteService
        mongo_mock = MagicMock()
        service = NoWasteService(mongo_mock)

        # and
        mongo_mock.db.recipes.find.return_value = [{"a": "b"}, {"c": "d"}]

        # when
        result = service.recipe_list()

        # then
        self.assertEqual(result, [{"a": "b"}, {"c": "d"}])

        # and
        mongo_mock.db.recipes.find.assert_called_with()
