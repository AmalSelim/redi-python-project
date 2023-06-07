import matplotlib.pyplot as plt

class EnergyConsumptionChart:
    def __init__(self, renewable_data, non_renewable_data, years):
        self.renewable_data = renewable_data
        self.non_renewable_data = non_renewable_data
        self.years = years


    def plot_chart(self):
        fig, ax = plt.subplots()

        # Create the bar chart
        renewable_bars = ax.bar(self.years, self.renewable_data, label='Renewable')
        non_renewable_bars = ax.bar(self.years, self.non_renewable_data, bottom=self.renewable_data, label='Non-renewable')

        # Add labels and title
        plt.xlabel('Year')
        plt.ylabel('Energy Consumption (in units)')
        plt.title('Energy Consumption: Renewable vs. Non-renewable')

        # Add individual values as tooltips
        renewable_labels = [f"{val}\nTotal: {self.get_total_renewable()}" for val in self.renewable_data]
        non_renewable_labels = [f"{val}\nTotal: {self.get_total_non_renewable()}" for val in self.non_renewable_data]

        plt.bar_label(renewable_bars, labels=renewable_labels, label_type='edge', fontsize=8)
        plt.bar_label(non_renewable_bars, labels=non_renewable_labels, label_type='edge', fontsize=8)

        # Add a legend
        plt.legend()

        # Display the chart
        plt.show()

    def get_total_renewable(self):
        return sum(self.renewable_data)

    def get_total_non_renewable(self):
        return sum(self.non_renewable_data)


# Usage example
renewable_data = [50, 60, 70, 80, 90]
non_renewable_data = [150, 140, 130, 120, 110]
years = [2015, 2016, 2017, 2018, 2019]

chart = EnergyConsumptionChart(renewable_data, non_renewable_data, years)
chart.plot_chart()
