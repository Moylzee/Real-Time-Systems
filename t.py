import json
import matplotlib.pyplot as plt

# Function to find blocks with ".cloudflare" in their name and store their values
def find_cloudflare_values(data):
    parent_names = []  # Array to store parent names
    poll_values = []  # Array to store poll values
    reach_values = []  # Array to store reach values
    delay_values = []  # Array to store delay values
    offset_values = []  # Array to store offset values
    jitter_values = []  # Array to store jitter values
    
    for parent_key in data:
        # For each nested block in the data
        for remote_key, block in data[parent_key].items():
            # Check if '.cloudflare' is in the remote key name
            if '202.28' in remote_key:
                # Check if the keys exist in the block
                # if 'poll' in block:
                #     poll_values.append(float(block['poll']))
                if 'reach' in block:
                    reach_values.append(float(block['reach']))
                if 'delay' in block:
                    delay_values.append(float(block['delay']))
                if 'offset' in block:
                    offset_values.append(float(block['offset']))
                if 'jitter' in block:
                    jitter_values.append(float(block['jitter']))
                # Append parent name to the array
                parent_names.append(parent_key)
    
    return parent_names, poll_values, reach_values, delay_values, offset_values, jitter_values

# Read JSON data from the file
with open('data/output.json', 'r') as f:
    data = json.load(f)

# Find parent names and values
parent_names, poll_values, reach_values, delay_values, offset_values, jitter_values = find_cloudflare_values(data)

# Create maps for parent names and values
poll_map = dict(zip(parent_names, poll_values))
reach_map = dict(zip(parent_names, reach_values))
delay_map = dict(zip(parent_names, delay_values))
offset_map = dict(zip(parent_names, offset_values))
jitter_map = dict(zip(parent_names, jitter_values))

# Write the maps to JSON files
with open('202.28_poll_map.json', 'w') as outfile:
    json.dump(poll_map, outfile, indent=4)

with open('202.28_reach_map.json', 'w') as outfile:
    json.dump(reach_map, outfile, indent=4)

with open('202.28_delay_map.json', 'w') as outfile:
    json.dump(delay_map, outfile, indent=4)

with open('202.28_offset_map.json', 'w') as outfile:
    json.dump(offset_map, outfile, indent=4)

with open('202.28_jitter_map.json', 'w') as outfile:
    json.dump(jitter_map, outfile, indent=4)

print("Parent value maps saved to respective JSON files")
