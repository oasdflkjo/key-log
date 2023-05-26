import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
import numpy as np
from PIL import Image

# Connect to the SQLite database
conn = sqlite3.connect('key_log.db')

# Read the key_log data into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM key_log WHERE type='keyboard'", conn)

# Calculate the frequency of each key
key_freq = df['key_or_button'].value_counts().to_dict()

# Load an image of your keyboard
keyboard_img = Image.open('keyboard.png')

# Calculate the relative position of each key on the image
# This might need some manual adjustments depending on your keyboard image
jump_size = 88
y_pos = [123, 212, 306, 393, 477, 567]
x_pos = [223, 269, 292, 335]
key_positions = {
    "'1'": (x_pos[0], 217),
    "'2'": (x_pos[0] + jump_size * 1, y_pos[1]),
    "'3'": (x_pos[0] + jump_size * 2, y_pos[1]),
    "'4'": (x_pos[0] + jump_size * 3, y_pos[1]),
    "'5'": (x_pos[0] + jump_size * 4, y_pos[1]),
    "'6'": (x_pos[0] + jump_size * 5, y_pos[1]),
    "'7'": (x_pos[0] + jump_size * 6, y_pos[1]),
    "'8'": (x_pos[0] + jump_size * 7, y_pos[1]),
    "'9'": (x_pos[0] + jump_size * 8, y_pos[1]),
    "'0'": (x_pos[0] + jump_size * 9, y_pos[1]),
    "'-'": (x_pos[0] + jump_size * 10, y_pos[1]),
    "'='": (x_pos[0] + jump_size * 11, y_pos[1]),
    "'backspace'": (x_pos[0] + jump_size * 12, y_pos[1]),

    "'q'": (x_pos[1], y_pos[2]),
    "'w'": (x_pos[1] + jump_size * 1, y_pos[2]),
    "'e'": (x_pos[1] + jump_size * 2, y_pos[2]),
    "'r'": (x_pos[1] + jump_size * 3, y_pos[2]),
    "'t'": (x_pos[1] + jump_size * 4, y_pos[2]),
    "'y'": (x_pos[1] + jump_size * 5, y_pos[2]),
    "'u'": (x_pos[1] + jump_size * 6, y_pos[2]),
    "'i'": (x_pos[1] + jump_size * 7, y_pos[2]),
    "'o'": (x_pos[1] + jump_size * 8, y_pos[2]),
    "'p'": (x_pos[1] + jump_size * 9, y_pos[2]),
    "'['": (x_pos[1] + jump_size * 10, y_pos[2]),
    "']'": (x_pos[1] + jump_size * 11, y_pos[2]),
    "'\\'": (x_pos[1] + jump_size * 12, y_pos[2]),

    "'a'": (x_pos[2], y_pos[3]),
    "'s'": (x_pos[2] + jump_size * 1, y_pos[3]),
    "'d'": (x_pos[2] + jump_size * 2, y_pos[3]),
    "'f'": (x_pos[2] + jump_size * 3, y_pos[3]),
    "'g'": (x_pos[2] + jump_size * 4, y_pos[3]),
    "'h'": (x_pos[2] + jump_size * 5, y_pos[3]),
    "'j'": (x_pos[2] + jump_size * 6, y_pos[3]),
    "'k'": (x_pos[2] + jump_size * 7, y_pos[3]),
    "'l'": (x_pos[2] + jump_size * 8, y_pos[3]),
    "';'": (x_pos[2] + jump_size * 9, y_pos[3]),
    "'''": (x_pos[2] + jump_size * 10, y_pos[3]),
    "'enter'": (x_pos[2] + jump_size * 11, y_pos[3]),

    "'z'": (x_pos[3], y_pos[4]),
    "'x'": (x_pos[3] + jump_size * 1, y_pos[4]),
    "'c'": (x_pos[3] + jump_size * 2, y_pos[4]),
    "'v'": (x_pos[3] + jump_size * 3, y_pos[4]),
    "'b'": (x_pos[3] + jump_size * 4, y_pos[4]),
    "'n'": (x_pos[3] + jump_size * 5, y_pos[4]),
    "'m'": (x_pos[3] + jump_size * 6, y_pos[4]),
    "','": (x_pos[3] + jump_size * 7, y_pos[4]),
    "'.'": (x_pos[3] + jump_size * 8, y_pos[4]),
    "'/'": (x_pos[3] + jump_size * 9, y_pos[4]),

    # Add more keys...
}

# Create a heatmap
fig, ax = plt.subplots()
ax.imshow(keyboard_img, aspect='equal')

# Use a colormap to map frequencies to colors
# 'RdYlGn' is a colormap that goes from red to green
cmap = plt.get_cmap('RdYlGn')

min_freq = np.min(list(key_freq.values()))
max_freq = np.max(list(key_freq.values()))

for key, freq in key_freq.items():
    if key in key_positions:
        # Normalize the frequency to the range between 0 and 1
        normalized_freq = (freq - min_freq) / (max_freq - min_freq)

        # Create a circle at the key's position with a color based on the normalized frequency
        circle = patches.Circle(
            key_positions[key], radius=20, color=cmap(normalized_freq))
        ax.add_patch(circle)

plt.savefig('heatmap.png')

plt.savefig('heatmap.png')
