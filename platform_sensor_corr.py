import pandas as pd

# Load the Excel file
file_path = "SSM_Perception_scratch.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path, sheet_name='DataProcessing')

# Combine 'PC' and 'PC_ASSUME' columns into 'PC_Combined'
df['PC_Combined'] = df['PC'].fillna(0) + df['PC_ASSUME'].fillna(0)

# Define the platform and sensor columns
platforms = ['PC_Combined', 'EMBEDDEDLIN', 'BAREMETAL']
sensors = ['1DTOF', '3DTOF', 'LiDAR', 'RADAR', 'MONOVISION', 'STEREOVISION']

# Filter valid years (non-zero years)
valid_data = df[df['Publication Year'] > 2021]

# Extract relevant columns (platforms and sensors)
platform_sensor_data = valid_data[platforms + sensors].fillna(0)

# Compute the correlation matrix
platform_sensor_correlation = platform_sensor_data.corr()

# Extract only platform-sensor correlations
platform_sensor_correlation_matrix = platform_sensor_correlation.loc[platforms, sensors]

# Display the correlation matrix
print("Platform-Sensor Correlation Matrix:")
print(platform_sensor_correlation_matrix)
