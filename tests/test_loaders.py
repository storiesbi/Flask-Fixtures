import os
import unittest
from datetime import datetime

from flask_fixtures import config
from flask_fixtures.config import JSON_PARSE_DATETIME
from flask_fixtures.loaders import JSONLoader
from flask_fixtures.loaders import load, FixtureLoader, add, remove

from myapp import app


class CustomJSONLoader(FixtureLoader):
    extensions = ('.json',)

    def load(self, filename):
        return ["foo"]


class TestLoaders(unittest.TestCase):

    def tearDown(self):
        config.reset()

    def test_only_loader_can_be_added(self):
        self.assertRaises(ValueError, add, {})

    def test_custom_loader_is_used_first(self):
        add(CustomJSONLoader)
        path = os.path.join(app.root_path, "fixtures", "authors.json")
        data = load(path)
        remove(CustomJSONLoader)

        assert ["foo"] == data

    def test_datetime_parsing_in_json(self):
        def assert_datetime(expected_value):
            path = os.path.join(app.root_path, "fixtures", "dates.json")
            json_loader = JSONLoader()
            data = json_loader.load(path)

            assert expected_value == data[0]['records'][0]['published_date']

        config.settings[JSON_PARSE_DATETIME] = True
        assert_datetime(datetime(1984, 7, 1))

        config.settings[JSON_PARSE_DATETIME] = False
        assert_datetime("1984-07-01")
