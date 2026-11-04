import unittest

from heat_index import calculate_heat_index, risk_category


class HeatIndexTests(unittest.TestCase):
    def test_nws_reference_90_f_70_percent(self):
        # The NWS equation example calculates approximately 105°F.
        self.assertAlmostEqual(calculate_heat_index(90, 70), 105.0, delta=1.0)

    def test_low_humidity_adjustment(self):
        self.assertAlmostEqual(calculate_heat_index(100, 10), 94.12, delta=0.02)

    def test_high_humidity_adjustment(self):
        self.assertAlmostEqual(calculate_heat_index(85, 90), 101.78, delta=0.02)

    def test_lower_range_uses_simple_method(self):
        self.assertAlmostEqual(calculate_heat_index(70, 10), 68.585, places=3)

    def test_invalid_humidity_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_heat_index(90, 101)

    def test_risk_category_boundaries(self):
        expected = [(79.9, "Below caution"), (80, "Caution"), (89.9, "Caution"),
                    (90, "Extreme Caution"), (102.9, "Extreme Caution"),
                    (103, "Danger"), (124.9, "Danger"), (125, "Extreme Danger")]
        for value, category in expected:
            with self.subTest(value=value):
                self.assertEqual(risk_category(value), category)

    def test_higher_humidity_increases_index_for_example(self):
        self.assertGreater(calculate_heat_index(90, 80), calculate_heat_index(90, 30))


if __name__ == "__main__":
    unittest.main()
