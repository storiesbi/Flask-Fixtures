import os
import unittest
from datetime import datetime

from flask_fixtures import config
from flask_fixtures.config import JSON_PARSE_DATETIME
from flask_fixtures.loaders import JSONLoader

from myapp import app


class TestLoaders(unittest.TestCase):

    def tearDown(self):
        config.reset()

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
