import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "SSM_Perception_scratch.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path, sheet_name='DataProcessing')

# Combine 'PC' and 'PC_ASSUME' into 'PC_Combined'
df['PC_Combined'] = df['PC'].fillna(0) + df['PC_ASSUME'].fillna(0)

# Define platforms and sensors
platforms = ['PC_Combined', 'EMBEDDEDLIN', 'BAREMETAL']
sensors = ['1DTOF', '3DTOF', 'LiDAR', 'RADAR', 'MONOVISION', 'STEREOVISION']

# Filter valid years (non-zero years)
valid_data = df[df['Publication Year'] > 0]

# Count the number of papers using each platform and sensor
platform_counts = (valid_data[platforms] > 0).sum()
sensor_counts = (valid_data[sensors] > 0).sum()

# Plot the histogram of platform counts
plt.figure(figsize=(10, 5))
platform_counts.plot(kind='bar', color='steelblue')
plt.title('Number of Papers Using Each Platform')
plt.xlabel('Platform')
plt.ylabel('Count of Papers')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.savefig("platform_count.png", format='png', dpi=300)
plt.show()

# Plot the histogram of sensor counts
plt.figure(figsize=(10, 5))
sensor_counts.plot(kind='bar', color='darkorange')
plt.title('Number of Papers Using Each Sensor')
plt.xlabel('Sensor')
plt.ylabel('Count of Papers')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.savefig("sensor_count.png", format='png', dpi=300)
plt.show()
