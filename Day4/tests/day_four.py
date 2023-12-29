import unittest

import part_one


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        expected = 13
        actual = part_one.part_one("input.txt")
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
