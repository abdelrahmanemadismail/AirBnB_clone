#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test the initialization of a BaseModel instance.
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_save(self):
        """
        Test the save method of the BaseModel class.
        """
        obj = BaseModel()
        updated_at_before_save = obj.updated_at
        obj.save()
        self.assertNotEqual(updated_at_before_save, obj.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
