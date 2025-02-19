import json
import matplotlib.pyplot as plt

# Function to find blocks with ".cloudflare" in their name and store their jitter values
def find_cloudflare_jitter(data):
    parent_names = []  # Array to store parent names
    jitter_values = []  # Array to store jitter values
    
    for parent_key in data:
        # For each nested block in the data
        for remote_key, block in data[parent_key].items():
            # Check if '.cloudflare' is in the remote key name
            if '.cloudflare' in remote_key:
                # Check if 'jitter' key exists in the block
                if 'jitter' in block:
                    # Append parent name and jitter value to their respective arrays
                    parent_names.append(parent_key)
                    jitter_values.append(float(block['jitter']))  # Convert jitter value to float for plotting
    
    return parent_names, jitter_values

# Read JSON data from the file
with open('data/output.json', 'r') as f:
    data = json.load(f)

# Find parent names and jitter values
parent_names, jitter_values = find_cloudflare_jitter(data)

# Output the collected data
print("Parent Names:", parent_names)
print("Jitter Values:", jitter_values)

# Create a line graph
plt.plot(parent_names, jitter_values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Set the labels and title
plt.xlabel('Parent Name')
plt.ylabel('Jitter Value')
plt.title('Jitter Values for cloudflare')

# Customize the y-axis to have increments of 50
plt.yticks(range(0, int(max(jitter_values)) + 50, 50))

# Rotate x-axis labels for better readability if needed
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
