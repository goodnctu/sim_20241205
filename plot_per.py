import os
import numpy as np
import matplotlib.pyplot as plt

# Function to read SNR and PER from a file
def read_data(file_path):
    snr = []
    per = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by commas and extract SNR and PER
            parts = line.split(',')
            snr_value = float(parts[0].split(':')[1].strip())
            per_value = float(parts[3].split(':')[1].strip())
            snr.append(snr_value)
            per.append(per_value)
    return np.array(snr), np.array(per)

# Directory containing mcs folders
base_dir = './'

# Initialize plot
plt.figure()

# Get and sort mcs folders in reverse order
mcs_folders = sorted([f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))], reverse=True)

# Iterate over each mcs folder
for mcs_folder in mcs_folders:
    folder_path = os.path.join(base_dir, mcs_folder)
    file_path = os.path.join(folder_path, 'mimo_top_result.txt')
    if os.path.exists(file_path):
        snr, per = read_data(file_path)
        plt.semilogy(snr, per, label=mcs_folder)

# Customize plot
plt.xlabel('SNR')
plt.ylabel('PER')
plt.title('SNR vs PER')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show plot
plt.show()