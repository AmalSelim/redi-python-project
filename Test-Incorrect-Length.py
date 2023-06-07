import unittest
from Energy_Consumption_Chart import EnergyConsumptionChart

class TestEnergyConsumptionChart(unittest.TestCase):
    def test_different_lengths(self):
        renewable_data = [50, 60, 70, 80, 90]
        non_renewable_data = [150, 140, 130, 120, 110]
        years = [2015, 2016, 2017, 2018]  # Incorrect length

        with self.assertRaises(ValueError) as cm:
            EnergyConsumptionChart(renewable_data, non_renewable_data, years)

        error_message = str(cm.exception)
        self.assertEqual(error_message, "Lengths of 'years', 'renewable_data', and 'non_renewable_data' must be the same.")

    def test_same_lengths(self):
        renewable_data = [50, 60, 70, 80, 90]
        non_renewable_data = [150, 140, 130, 120, 110]
        years = [2015, 2016, 2017, 2018, 2019]  # Correct length

        try:
            EnergyConsumptionChart(renewable_data, non_renewable_data, years)
        except ValueError:
            self.fail("Unexpected ValueError raised")

