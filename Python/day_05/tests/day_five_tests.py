import unittest

import part_one


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        expected = 35
        actual = day_five.part_one(input_file_path="input.txt")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
