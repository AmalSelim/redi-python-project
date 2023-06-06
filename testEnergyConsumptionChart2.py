import unittest
from energy_consumption_chart import EnergyConsumptionChart

class TestEnergyConsumptionChart(unittest.TestCase):
    def test_different_lengths(self):
        renewable_data = [50, 60, 70, 80, 90]
        non_renewable_data = [150, 140, 130, 120, 110]
        years = [2015, 2016, 2017, 2018,2019]  # Incorrect length of 'years' list

        with self.assertRaises(ValueError) as cm:
            EnergyConsumptionChart(renewable_data, non_renewable_data, years)

        error_message = str(cm.exception)
        self.assertEqual(error_message, "Lengths of 'years', 'renewable_data', and 'non_renewable_data' must be the same.")


if __name__ == '__main__':
    unittest.main()
