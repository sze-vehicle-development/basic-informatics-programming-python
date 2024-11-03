import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the random walk
num_steps = 100  # Total number of steps in the walk

# Generate random walk data
x = np.zeros(num_steps)
y = np.zeros(num_steps)

# Generate steps
for i in range(1, num_steps):
    angle = np.random.uniform(0, 2 * np.pi)  # Random angle in radians
    x[i] = x[i - 1] + np.cos(angle)  # Step in the x direction
    y[i] = y[i - 1] + np.sin(angle)  # Step in the y direction

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("2D Random Walk Animation")
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")

# Initialize line plot for the walk
line, = ax.plot([], [], color="blue", lw=2)
point, = ax.plot([], [], "o", color="red")  # Current position marker

# Initialize function for animation
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# Update function for each frame
def update(step):
    line.set_data(x[:step], y[:step])
    point.set_data(x[step - 1], y[step - 1])
    return line, point

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=True, interval=100)
ani.save("random_walk.mp4", writer="ffmpeg", fps=10)
# Display the animation
plt.show()