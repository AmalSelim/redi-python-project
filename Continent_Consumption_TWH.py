
import pandas as pd
from plotly.graph_objects import Scatter, Figure

# Read the CSV file using pandas
data = pd.read_csv("C:/Users/amirh/Desktop/REDI Project/Project REDO Data/Continent_Consumption_TWH.csv", delimiter=',')

# Store the data in a dictionary
data_dict = {
    'Europe': data['Europe'],
    'Africa': data['Africa'],
    'Pacific': data['Pacific'],
    'Asia': data['Asia'],
    'BRICS': data['BRICS'],
    'Latin America': data['Latin_America'],
    'North America': data['North_America'],
    'Middle East': data['Middle_East'],
    'OECD': data['OECD'],
    'CIS': data['CIS'],
    'World': data['World']
}

# Define the years
years = data['Year']

# Create the figure
fig = Figure()

# Iterate over the data dictionary
for label, values in data_dict.items():
    fig.add_trace(Scatter(
        x=years,
        y=values,
        mode='lines',
        name=label,
        stackgroup='one',
        hovertemplate='%{y:.2f}',
        fill='tonexty',
        line=dict(width=0.5),
    ))

# Update the layout
fig.update_layout(
    title='Continent_Consumption_TWH - Area',
    xaxis_title='Years',
    yaxis_title='Consumption',
    showlegend=True,
    hovermode='x unified',
)

# Display the figure
fig.show()
