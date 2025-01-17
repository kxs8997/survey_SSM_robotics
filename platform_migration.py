import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "SSM_Perception_scratch.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path, sheet_name='DataProcessing')

# Combine 'PC' and 'PC_ASSUME' into 'PC_Combined'
df['PC_Combined'] = df['PC'].fillna(0) + df['PC_ASSUME'].fillna(0)

# Define the platforms
platforms = ['PC_Combined', 'EMBEDDEDLIN', 'BAREMETAL']

display_labels = ['PC_Combined', 'Embedded', 'Baremetal']

# Filter valid years (non-zero years)
valid_data = df[df['Publication Year'] > 0]

# Group by 'Publication Year' and sum platform usage
platform_trends = valid_data.groupby('Publication Year')[platforms].sum()

# Plot the platform migration using a stacked area chart
ax = platform_trends.plot(
    kind='area',
    stacked=True,
    alpha=0.7,
    colormap='plasma',
    figsize=(15, 8),
    legend=False,  # Disable the default legend
)

# Add the custom legend with handles
handles, _ = ax.get_legend_handles_labels()  # Get handles from the plot
plt.legend(handles, display_labels, title='Platforms', loc='upper left')

# Add titles and labels
plt.title('Platform Migration Analysis Over Time')
plt.xlabel('Publication Year')
plt.ylabel('Total Usage')
plt.xticks(platform_trends.index, rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("platform_migration_analysis.png", format='png', dpi=300)
plt.show()
