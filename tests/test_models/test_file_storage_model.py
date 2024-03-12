#!/usr/bin/python3
"""
Unit tests for FileStorage class
"""

import pep8
import unittest
import io
import sys
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up method
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Tear down method
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_file_storage_pep8(self):
        """
        Test for PEP8 style compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_all(self):
        """
        Test the all method of FileStorage.
        """
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], obj)

    def test_new(self):
        """
        Test the new method of FileStorage.
        """
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """
        Test the save method of FileStorage.
        """
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        with open("file.json", 'r') as file:
            saved_data = json.load(file)
        self.assertIn(key, saved_data)

    def test_reload(self):
        """
        Test the reload method of FileStorage.
        """
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].id, obj.id)


if __name__ == '__main__':
    unittest.main()
