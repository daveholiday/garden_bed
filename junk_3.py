import matplotlib.pyplot as plt
import numpy as np

# Bed dimensions
bed_length = 72  # in inches (6 feet)
bed_width = 36   # in inches (3 feet)

# Planting parameters
plant_spacing = 7.0  # in inches, distance between garlic cloves
row_offset = (plant_spacing / 2)     # in inches, horizontal offset for staggered rows
edge_buffer = 2.5    # in inches, minimum distance from the edge of the bed

# Circle (existing object) parameters
circle_radius = 10.0  # in inches
circle1_center = (20, bed_width / 2)
circle2_center = (52, bed_width / 2)

# Calculate available space after edge buffer
available_length = bed_length - 2 * edge_buffer
available_width = bed_width - 2 * edge_buffer

# Calculate the number of rows and columns that can fit
num_columns = int(available_length // plant_spacing) + 1
num_rows = int(available_width // row_offset) + 1

# Calculate the actual planting area dimensions
actual_planting_length = (num_columns - 1) * plant_spacing
actual_planting_width = (num_rows - 1) * row_offset

# Calculate new starting points to center the planting area
# Calculate which min makes sense, a normal or offset row value.
x_start_offset = (bed_length - (actual_planting_length + row_offset)) / 2
x_start_base = (bed_length - actual_planting_length) / 2
x_start = min(x_start_base, x_start_offset)
y_start = (bed_width - actual_planting_width) / 2

# Generate garlic planting positions
clove_positions = []

y = y_start
for row in range(num_rows):
    offset = 0 if row % 2 == 0 else row_offset
    x = x_start + offset
    for col in range(num_columns):
        # Check if the position is within the edge buffer
        if (x > edge_buffer and x < bed_length - edge_buffer and 
            y > edge_buffer and y < bed_width - edge_buffer):
            # Check if the position is outside the exclusion circles
            if (np.hypot(x - circle1_center[0], y - circle1_center[1]) > circle_radius and 
                np.hypot(x - circle2_center[0], y - circle2_center[1]) > circle_radius):
                clove_positions.append((x, y))
        x += plant_spacing
    y += row_offset

# Plotting the garden bed and garlic positions
fig, ax = plt.subplots()

# Draw the bed
bed = plt.Rectangle((0, 0), bed_length, bed_width, fill=None, edgecolor='black')
limit_length = (bed_length-edge_buffer*2)
limit_width = (bed_width-edge_buffer*2)
limit_bed= plt.Rectangle((edge_buffer, edge_buffer), limit_length, limit_width, fill=None, edgecolor='blue', linestyle='dashed')
ax.add_patch(bed)
ax.add_patch(limit_bed)

# Draw the circles (existing objects)
circle1 = plt.Circle(circle1_center, circle_radius, color='red', fill=False)
circle2 = plt.Circle(circle2_center, circle_radius, color='red', fill=False)
ax.add_patch(circle1)
ax.add_patch(circle2)

# Plot the garlic clove positions
for pos in clove_positions:
    ax.plot(pos[0], pos[1], 'go')  # 'go' indicates green color and circle marker

# Display the calculated plant and row spacing on the plot
plt.text(5, bed_width+.5, f"Garlic Spacing: {plant_spacing} inches", fontsize=10)

# Set limits and aspect
ax.set_xlim(-1, bed_length + 1)
ax.set_ylim(-1, bed_width + 3)
ax.set_aspect('equal')

# Show the plot
plt.title(f"Garlic Planting Layout ({len(clove_positions)} plants)")
plt.show()

# Print the number of garlic planting spots
print(f"Number of garlic planting spots: {len(clove_positions)}")
print(f"First plot location: {clove_positions[0]}")
