import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxFunction(unittest.TestCase):

    def test_integer_orderedlist(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(list), 5)

    def test_integer_unorderedlist(self):
        list = [4, 2, 5, 1, 23, 44]
        self.assertEqual(max_integer(list), 44)

    def test_strings_list(self):
        list = ["something", "name", "alx", "school"]
        self.assertEqual(max_integer(list), "something")

    def test_characters_list(self):
        list = ["a", "b", 'c', "A"]
        self.assertEqual(max_integer(list), "c")
    
    def test_float_numbers(self):
        list = [1.2, 4.5, 2.3, 1.8, -5.4]
        self.assertEqual(max_integer(list), 4.5)

    def test_int_float_numbers(self):
        list = [4, 5.2, 5, 9, -2 ,1, 3.4, 2.2]
        self.assertEqual(max_integer(list), 9)

    def test_empty_list(self):
        list = []
        self.assertEqual(max_integer(list), None)

if __name__ == "__main__":
    unittest.main()
