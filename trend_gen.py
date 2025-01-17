import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "SSM_Perception_scratch.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path, sheet_name='DataProcessing')

# Combine PC and PC_ASSUME columns
df['PC_Combined'] = df['PC'].fillna(0) + df['PC_ASSUME'].fillna(0)

# Extract relevant columns (original names)
platforms_original = ['PC_Combined', 'EMBEDDEDLIN', 'BAREMETAL']
sensors_original = ['1DTOF', '3DTOF', 'LiDAR', 'RADAR', 'MONOVISION', 'STEREOVISION']

# Display names
platforms_display = ['PC_Combined', 'Embedded', 'Baremetal']
sensors_display = ['1DTOF', '3DTOF', 'LiDAR', 'Radar', 'Monovision', 'Stereovision']

# Create a mapping for display names
platform_mapping = dict(zip(platforms_original, platforms_display))
sensor_mapping = dict(zip(sensors_original, sensors_display))

# Filter valid years (non-zero years)
valid_data = df[df['Publication Year'] > 0]

# Group by 'Publication Year' and sum values within each year
time_trend = valid_data.groupby('Publication Year')[platforms_original + sensors_original].sum()

# Combine 1996-2010 into a single point
time_range_1996_2010 = time_trend.loc[1996:2010].sum()
time_trend_adjusted = time_trend.drop(time_trend.index[(time_trend.index >= 1996) & (time_trend.index <= 2010)])
time_trend_adjusted.loc[1996] = time_range_1996_2010

# Combine 2023-2024 into a single point
time_range_2023_2024 = time_trend.loc[2023:2024].sum()
time_trend_adjusted = time_trend_adjusted.drop(time_trend_adjusted.index[(time_trend_adjusted.index >= 2023)])
time_trend_adjusted.loc[2024] = time_range_2023_2024

# Sort the index for proper plotting
time_trend_adjusted = time_trend_adjusted.sort_index()

# Plot platform trends with updated display names
plt.figure(figsize=(15, 8))
for platform in platforms_original:
    plt.plot(time_trend_adjusted.index, time_trend_adjusted[platform], marker='o', label=platform_mapping[platform])

plt.title('Platform Usage Trends Over Time (1996-2010 and 2023-2024 Combined)')
plt.xlabel('Publication Year')
plt.ylabel('Total Usage')
plt.xticks(time_trend_adjusted.index, rotation=45)
plt.legend(title='Platforms', loc='upper left')
plt.grid(True)
plt.savefig("platform_trend_analysis.png", format='png', dpi=300)
plt.show()

# Plot sensor trends with updated display names
plt.figure(figsize=(15, 8))
for sensor in sensors_original:
    plt.plot(time_trend_adjusted.index, time_trend_adjusted[sensor], marker='o', label=sensor_mapping[sensor])

plt.title('Sensor Usage Trends Over Time (1996-2010 and 2023-2024 Combined)')
plt.xlabel('Publication Year')
plt.ylabel('Total Usage')
plt.xticks(time_trend_adjusted.index, rotation=45)
plt.legend(title='Sensors', loc='upper left')
plt.grid(True)
plt.savefig("sensor_trend_analysis.png", format='png', dpi=300)
plt.show()
