import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxFunctionTest(unittest.TestCase):

    def test_integer_list(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(list), 5)
