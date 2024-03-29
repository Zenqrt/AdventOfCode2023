import unittest

import part_one
import part_two


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        expected = 35
        actual = part_one.part_one(input_file_path="input.txt")
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 46
        actual = part_two.part_two(input_file_path="input.txt")
        self.assertEqual(expected, actual);

if __name__ == '__main__':
    unittest.main()
