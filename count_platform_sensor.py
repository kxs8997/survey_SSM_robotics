import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy for range generation

# Load the Excel file
file_path = "SSM_Perception_scratch.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path, sheet_name='DataProcessing')

# Combine 'PC' and 'PC_ASSUME' into 'PC_Combined'
df['PC_Combined'] = df['PC'].fillna(0) + df['PC_ASSUME'].fillna(0)

# Define original platforms and sensors
platforms_original = ['PC_Combined', 'EMBEDDEDLIN', 'BAREMETAL']
sensors_original = ['1DTOF', '3DTOF', 'LiDAR', 'RADAR', 'MONOVISION', 'STEREOVISION']

# Define display names for platforms and sensors
platforms_display = ['PC_Combined', 'Embedded', 'Baremetal']
sensors_display = ['1DTOF', '3DTOF', 'LiDAR', 'Radar', 'Monovision', 'Stereovision']

# Create mappings for display names
platform_mapping = dict(zip(platforms_original, platforms_display))
sensor_mapping = dict(zip(sensors_original, sensors_display))

# Filter valid years (non-zero years)
valid_data = df[df['Publication Year'] > 2007]

# Count the number of papers using each platform and sensor
platform_counts = (valid_data[platforms_original] > 0).sum()
sensor_counts = (valid_data[sensors_original] > 0).sum()

# Rename the index for display
platform_counts.index = platform_counts.index.map(platform_mapping)
sensor_counts.index = sensor_counts.index.map(sensor_mapping)

# Plot the histogram of platform counts
plt.figure(figsize=(10, 5))
platform_counts.plot(kind='bar', color='steelblue')
plt.title('Number of Papers Using Each Platform')
plt.xlabel('Platforms')
plt.ylabel('Count of Papers')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()  # Adjust layout to prevent cutoff
plt.savefig("platform_count.png", format='png', dpi=300)
plt.show()

# Plot the histogram of sensor counts
plt.figure(figsize=(10, 5))
sensor_counts.plot(kind='bar', color='darkorange')
plt.title('Number of Papers Using Each Sensor')
plt.xlabel('Sensors')
plt.ylabel('Count of Papers')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Ensure y-axis ticks are integer values
plt.yticks(np.arange(0, sensor_counts.max() + 1, 1))

plt.tight_layout()  # Adjust layout to prevent cutoff
plt.savefig("sensor_count.png", format='png', dpi=300)
plt.show()
