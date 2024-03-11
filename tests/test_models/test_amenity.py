#!/usr/bin/python3
"""
Unit tests for Amenity class
"""

import unittest
import pep8
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_amenity_pep8(self):
        """
        Test PEP8 style compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_amenity_instance(self):
        """
        Test instance creation.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attributes(self):
        """
        Test default attributes.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
