import matplotlib.pyplot as plt
import random

# Parameters
num_steps = 100  # Number of steps in the random walk

# Initialize starting point
x, y = 0, 0
x_values = [x]
y_values = [y]

# Generate random walk
for _ in range(num_steps):
    step_direction = random.choice(['up', 'down', 'left', 'right'])
    if step_direction == 'up':
        y += 1
    elif step_direction == 'down':
        y -= 1
    elif step_direction == 'left':
        x -= 1
    elif step_direction == 'right':
        x += 1
    x_values.append(x)
    y_values.append(y)

# Plot the random walk
plt.figure(figsize=(8, 8))
plt.plot(x_values, y_values, marker='o', color='b', markersize=3, linewidth=1)
plt.title('Random Walk Simulation')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid(True)
plt.show()