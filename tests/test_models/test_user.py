#!/usr/bin/python3
"""
Unit tests for User class
"""


import pep8
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_user_pep8(self):
        """
        Test PEP8 style compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_user_instance(self):
        """
        Test instance creation.
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        """
        Test default attributes.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_initialization(self):
        """
        Test initialization with attributes.
        """
        user = User(
                email="test@example.com",
                password="password",
                first_name="John",
                last_name="Doe"
                )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_to_dict(self):
        """
        Test conversion to dictionary.
        """
        user = User(
                email="test@example.com",
                password="password",
                first_name="John",
                last_name="Doe"
                )
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['__class__'], "User")

    def test_user_save(self):
        """
        Test save method.
        """
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

    def test_user_reload(self):
        """
        Test reload method.
        """
        user = User(
                email="test@example.com",
                password="password",
                first_name="John",
                last_name="Doe"
                )
        user.save()
        user_id = user.id
        del user
        storage.reload()
        reloaded_user = storage.all()["User." + user_id]
        self.assertEqual(reloaded_user.email, "test@example.com")
        self.assertEqual(reloaded_user.password, "password")
        self.assertEqual(reloaded_user.first_name, "John")
        self.assertEqual(reloaded_user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
