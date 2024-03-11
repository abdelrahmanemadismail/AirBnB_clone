#!/usr/bin/python3
"""
Unit tests for City class
"""

import unittest
import pep8
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def test_city_pep8(self):
        """
        Test PEP8 style compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_city_instance(self):
        """
        Test instance creation.
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        """
        Test default attributes.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
