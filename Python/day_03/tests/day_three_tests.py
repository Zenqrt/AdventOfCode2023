import unittest

import part_one
import part_two


class DayThreeTests(unittest.TestCase):
    def test_part_one(self):
        expected = 4361
        actual = part_one.part_one(input_file_path="input.txt")
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 467835
        actual = part_two.part_two(input_file_path="input.txt")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
