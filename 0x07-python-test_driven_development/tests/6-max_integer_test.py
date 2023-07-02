import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxFunction(unittest.TestCase):

    def test_integer_orderedlist(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(list), 5)

    def test_integer_unorderedlist(self):
        list = [4, 2, 5, 1, 23, 44]
        self.assertEqual(list, 44)

    def test_strings_list(self):
        list = ["something", "name", "alx", "school"]
        self.assertEqual(list, "something")

    def test_characters_list(self):
        list = ["a", "b", 'c', "A"]
        self.assertEqual(list, "c")

if __name__ == "__main__":
    unittest.main()
