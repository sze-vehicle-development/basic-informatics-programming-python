# Define a function to translate a point by modifying only the x-coordinate
def translate_x(point, offset):
    x, y = point
    return (x + offset, y)

# Define a function to filter points based on x-coordinate
def filter_by_x(point):
    x, _ = point
    return x > 2

# Original list of tuples (coordinates)
coordinates = [(1, 2), (3, 4), (5, 6)]

# Translate each point by +1 on the x-axis
translated_coordinates = [translate_x(point, 1) for point in coordinates]

# Filter points where x > 2
filtered_coordinates = [point for point in translated_coordinates if filter_by_x(point)]

# Output results
print("Original coordinates:", coordinates)
# Output: Original coordinates: [(1, 2), (3, 4), (5, 6)]

print("Translated coordinates:", translated_coordinates)
# Output: Translated coordinates: [(2, 2), (4, 4), (6, 6)]

print("Filtered coordinates (x > 2):", filtered_coordinates)
# Output: Filtered coordinates (x > 2): [(4, 4), (6, 6)]