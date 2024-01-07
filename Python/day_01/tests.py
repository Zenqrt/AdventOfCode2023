import unittest
import solution


class MyTestCase(unittest.TestCase):
    def test_retrieve_calibration_value(self):
        calibration_inputs = {
            "two1nine": 29,
            "eightwothree": 83,
            "abcone2threexyz": 13,
            "xtwone3four": 24,
            "4nineeightseven2": 42,
            "zoneight234": 14,
            "7pqrstsixteen": 76,
            "jdlsqp4onefour59lhdthreenine": 49
        }

        for calibration_input, expected_digit in calibration_inputs.items():
            actual_digit = solution.retrieve_calibration_value(calibration_input)
            self.assertEqual(expected_digit, actual_digit)

    def test_sum_calibration_values(self):
        calibration_values = [29, 83, 13, 24, 42, 14, 76]

        expected_sum = 281
        actual_sum = solution.sum_calibration_values(calibration_values)
        self.assertEqual(expected_sum, actual_sum)


if __name__ == '__main__':
    unittest.main()
