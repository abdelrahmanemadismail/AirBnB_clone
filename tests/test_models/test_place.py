#!/usr/bin/python3
"""
Unit tests for Place class
"""

import unittest
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_place_pep8(self):
        """
        Test PEP8 style compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_place_instance(self):
        """
        Test instance creation.
        """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        """
        Test default attributes.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
