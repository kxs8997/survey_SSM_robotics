import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "SSM_Perception_scratch.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path, sheet_name='DataProcessing')

# Define the sensors
sensors = ['1DTOF', '3DTOF', 'LiDAR', 'RADAR', 'MONOVISION', 'STEREOVISION']

# Display Labels
display_labels = ['1DTOF', '3DTOF', 'LiDAR', 'Radar', 'Monovision', 'Stereovision']

# Filter valid years (non-zero years)
valid_data = df[df['Publication Year'] > 2007]

# Group by 'Publication Year' and sum sensor usage
sensor_trends = valid_data.groupby('Publication Year')[sensors].sum()

# Plot the sensor migration using a stacked area chart
ax = sensor_trends.plot(
    kind='area',
    stacked=True,
    alpha=0.7,
    colormap='plasma',
    figsize=(15, 8),
    legend=False,  # Disable the default legend
)

# Add the custom legend with handles
handles, _ = ax.get_legend_handles_labels()  # Get handles from the plot
plt.legend(handles, display_labels, title='Sensors', loc='upper left')

# Add titles and labels
plt.title('Sensor Migration Analysis Over Time')
plt.xlabel('Publication Year')
plt.ylabel('Total Usage')
plt.xticks(sensor_trends.index, rotation=45)
plt.grid(True)
plt.legend(title='Sensors', loc='upper left')
plt.tight_layout()
plt.savefig("sensor_migration_analysis.png", format='png', dpi=300)
plt.show()
