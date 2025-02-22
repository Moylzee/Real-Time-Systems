import json
import matplotlib.pyplot as plt

file_groups = {
    "jitter": [
        "data/cloudflare_data/cloudflare_jitter_map.json",
        "data/103-152_data/103-152_jitter_map.json",
        "data/144.20_data/144.20_jitter_map.json",
        "data/183.ip_data/183.ip_jitter_map.json",
        "data/202.28_data/202.28_jitter_map.json",
    ],
    "delay": [
        "data/cloudflare_data/cloudflare_delay_map.json",
        "data/103-152_data/103-152_delay_map.json",
        "data/144.20_data/144.20_delay_map.json",
        "data/183.ip_data/183.ip_delay_map.json",
        "data/202.28_data/202.28_delay_map.json",
    ],
    "offset": [
        "data/cloudflare_data/cloudflare_offset_map.json",
        "data/103-152_data/103-152_offset_map.json",
        "data/144.20_data/144.20_offset_map.json",
        "data/183.ip_data/183.ip_offset_map.json",
        "data/202.28_data/202.28_offset_map.json",
        "data/81.94_data/81.94_offset.json",
    ],
    "reach": [
        "data/cloudflare_data/cloudflare_reach_map.json",
        "data/103-152_data/103-152_reach_map.json",
        "data/144.20_data/144.20_reach_map.json",
        "data/183.ip_data/183.ip_reach_map.json",
        "data/202.28_data/202.28_reach_map.json",
        "data/81.94_data/81.94_reach_map.json",
    ],
    "reach_map": [
        "data/cloudflare_data/cloudflare_reach_map.json",
        "data/103-152_data/103-152_reach_map.json",
        "data/144.20_data/144.20_reach_map.json",
        "data/183.ip_data/183.ip_reach_map.json",
        "data/202.28_data/202.28_reach_map.json",
        "data/81.94_data/81.94_reach_map.json",
    ]
}

for group_name, filepaths in file_groups.items():
    num_files = len(filepaths)
    rows = 3
    cols = 2
    fig, axs = plt.subplots(rows, cols, figsize=(15, 10))

    for i, filepath in enumerate(filepaths):
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Convert data to lists for plotting
        timestamps = list(data.keys())
        values = list(data.values())
        
        # Create the line plot for each file in a separate subplot
        ax = axs[i // cols, i % cols]
        ax.plot(timestamps, values, label=filepath.split('/')[-1])
        ax.set_title(filepath.split('/')[-1])
        ax.set_xlabel('Timestamp')
        ax.set_ylabel(f'{group_name.capitalize()} Value')
        ax.grid(True)
        ax.legend()
        ax.tick_params(axis='x', rotation=45)

    # Hide any unused subplots
    for j in range(i + 1, rows * cols):
        fig.delaxes(axs[j // cols, j % cols])

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot to a file
    plt.savefig(f'bucket/graphs/{group_name}_graphs.png')
    plt.close(fig)