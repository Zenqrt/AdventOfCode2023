import unittest

import part_one
import part_two


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        expected = 288
        actual = part_one.part_one("input.txt")
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 71503
        actual = part_two.part_two("input.txt")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
