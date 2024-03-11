#!/usr/bin/python3
"""
Unit tests for Review class
"""

import unittest
import pep8
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def test_review_pep8(self):
        """
        Test PEP8 style compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_review_instance(self):
        """
        Test instance creation.
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        """
        Test default attributes.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
