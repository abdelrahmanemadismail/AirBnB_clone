#!/usr/bin/python3
"""
Unit tests for State class
"""

import unittest
import pep8
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_state_pep8(self):
        """
        Test PEP8 style compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_state_instance(self):
        """
        Test instance creation.
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_state_attributes(self):
        """
        Test default attributes.
        """
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
