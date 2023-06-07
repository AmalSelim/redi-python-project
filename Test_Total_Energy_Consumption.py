import unittest
from energy_consumption_chart import EnergyConsumptionChart

class TestEnergyConsumptionChart(unittest.TestCase):
    def test_total_values(self):
        renewable_data = [50, 60, 70, 80, 90]
        non_renewable_data = [150, 140, 130, 120, 110]
        years = [2015, 2016, 2017, 2018, 2019]

        chart = EnergyConsumptionChart(renewable_data, non_renewable_data, years)

        total_renewable = sum(renewable_data)
        total_non_renewable = sum(non_renewable_data)

        self.assertEqual(chart.get_total_renewable(), total_renewable)
        self.assertEqual(chart.get_total_non_renewable(), total_non_renewable)
