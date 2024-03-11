#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""


import pep8
import unittest
import io
import sys
from models.base_model import BaseModel
from models import storage


class TestBase(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up method
        """
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """
        Tear down method
        """
        pass

    def test_base_pep8(self):
        """
        test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """
        test doc in the file
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_uuid(self):
        """
        Test for uuid
        """
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertEqual(type(self.base1.id), str)
        self.assertEqual(type(self.base2.id), str)

    def test_instance(self):
        """
        Test for instance
        """
        self.assertTrue(isinstance(self.base1, BaseModel))
        self.assertTrue(isinstance(self.base2, BaseModel))

    def test_type(self):
        """
        Test for type of object
        """
        self.assertEqual(type(self.base1), BaseModel)
        self.assertEqual(type(self.base2), BaseModel)

    def test_save(self):
        """
        Test for save
        """
        time = self.base1.updated_at
        self.base1.save()
        self.assertFalse(time == self.base1.updated_at)

    def test_update(self):
        """
        Test for update
        """
        self.base1.name = "Holberton"
        self.assertTrue(hasattr(self.base1, "name"))

    def test_init_with_kwargs(self):
        """
        Test to init for kwargs
        """
        self.base1.name = "Holberton"
        model_json = self.base1.to_dict()
        new_model = BaseModel(**model_json)
        self.assertDictEqual(model_json, new_model.to_dict())
        self.assertIn("name", new_model.to_dict())
        self.assertIsNot(self.base1, new_model)


if __name__ == '__main__':
    unittest.main()
