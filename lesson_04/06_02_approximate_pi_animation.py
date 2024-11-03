import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the total number of points
num_points = 1000

# Initialize counts for points inside the circle
x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_title("Monte Carlo Simulation to Approximate π")

# Set up plot elements
inside_scatter, = ax.plot([], [], 'bo', markersize=2, label="Inside Circle")
outside_scatter, = ax.plot([], [], 'ro', markersize=2, label="Outside Circle")
text_pi = ax.text(-0.9, 0.9, '', fontsize=12, color='black')
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
ax.add_patch(circle)
ax.legend(loc="upper right")

# Function to initialize the animation
def init():
    inside_scatter.set_data([], [])
    outside_scatter.set_data([], [])
    text_pi.set_text('')
    return inside_scatter, outside_scatter, text_pi

# Update function for each frame
def update(frame):
    # Generate a random point
    x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)

    # Check if the point is inside the unit circle
    if x**2 + y**2 <= 1:
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

    # Update the scatter plot data
    inside_scatter.set_data(x_inside, y_inside)
    outside_scatter.set_data(x_outside, y_outside)

    # Calculate and update π approximation
    total_points = len(x_inside) + len(x_outside)
    pi_approximation = 4 * len(x_inside) / total_points
    text_pi.set_text(f'Approximation of π: {pi_approximation:.4f}')

    return inside_scatter, outside_scatter, text_pi

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_points, init_func=init, blit=True, interval=100)
ani.save("approximate_pi.mp4", writer="ffmpeg", fps=1000)
# Display the animation
plt.show()