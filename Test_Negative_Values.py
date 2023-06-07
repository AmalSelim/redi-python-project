import unittest
import matplotlib.pyplot as plt

from Energy_Consumption_Chart import EnergyConsumptionChart

class TestEnergyConsumptionChart(unittest.TestCase):
    def test_plot_chart(self):
        renewable_data = [50, 60, 70, 80, 90]
        non_renewable_data = [150, 140, -130, 120, 110]
        years = [2015, 2016, 2017, 2018, 2019]

        # Check if any value in renewable_data is negative or null
        self.assertFalse(any(value <= 0 for value in renewable_data), "Renewable data contains negative or null values")

        # Check if any value in non_renewable_data is negative or null
        self.assertFalse(any(value <= 0 for value in non_renewable_data), "Non-renewable data contains negative or null values")

        # Check if any value in years is negative or null
        self.assertFalse(any(value <= 0 for value in years), "Years data contains negative or null values")

        # Create the EnergyConsumptionChart object and plot the chart only if there are no negative values
        if all(value > 0 for value in renewable_data + non_renewable_data + years):
            chart = EnergyConsumptionChart(renewable_data, non_renewable_data, years)
            chart.plot_chart()

        # Assert that the chart is not displayed
        self.assertEqual(plt.gcf().number, 0)
