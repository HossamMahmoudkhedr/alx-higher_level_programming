#!/usr/bin/python3
"""Module to test the function rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_output(self):
        """Function to test the output the function rectangle"""
        self.assertAlmostEqual(Rectangle)

    def test_rectangle_input(self):
        self.assertRaises(TypeError, Rectangle, )
