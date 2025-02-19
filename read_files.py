import json

# Function to replace each nested block with its 'remote' value
def replace_with_remote(data):
    for key, blocks in data.items():
        updated_data = {}
        for block in blocks:
            remote_value = block["remote"]
            updated_data[remote_value] = block
        data[key] = updated_data
    return data

# Read JSON data from a file (output.json)
with open('data/output.json', 'r') as f:
    data = json.load(f)

# Replace blocks with remote values
updated_data = replace_with_remote(data)

# Write the modified data back to a new file (updated_output.json)
with open('updated_output.json', 'w') as f:
    json.dump(updated_data, f, indent=4)

print("JSON data has been updated and saved to 'updated_output.json'")
