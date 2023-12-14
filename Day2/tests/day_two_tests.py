import unittest

import day_two


class DayTwoTests(unittest.TestCase):
    def test_part_one(self):
        expected_total_game_ids = 8

        input_file_path = "input.txt"
        total_game_ids = day_two.part_one(input_file_path,
                                          expected_reds=12,
                                          expected_greens=13,
                                          expected_blues=14)

        self.assertEqual(expected_total_game_ids, total_game_ids)

    def test_part_two(self):
        expected_total_power_set = 2286

        input_file_path = "input.txt"
        total_power_set = day_two.part_two(input_file_path)

        self.assertEqual(expected_total_power_set, total_power_set)


if __name__ == '__main__':
    unittest.main()
