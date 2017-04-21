import os
import unittest

from flask_fixtures.loaders import load, FixtureLoader, add, remove

from myapp import app


class CustomJSONLoader(FixtureLoader):
    extensions = ('.json',)

    def load(self, filename):
        return ["foo"]


class TestLoaders(unittest.TestCase):

    def test_only_loader_can_be_added(self):
        self.assertRaises(ValueError, add, {})

    def test_custom_loader_is_used_first(self):
        add(CustomJSONLoader)
        path = os.path.join(app.root_path, "fixtures", "authors.json")
        data = load(path)
        remove(CustomJSONLoader)

        assert ["foo"] == data
