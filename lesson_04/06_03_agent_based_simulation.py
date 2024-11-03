import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the simulation
num_agents = 20          # Number of agents
num_steps = 100           # Number of steps in the simulation
bounds = 10               # Boundary limits of the space

# Initialize agents' positions randomly within the bounds
positions = np.random.uniform(-bounds, bounds, (num_agents, 2))

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-bounds, bounds)
ax.set_ylim(-bounds, bounds)
ax.set_title("Agent-Based Simulation: Random Walk")
scat = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='blue', alpha=0.7)

# Update function for the animation
def update(frame):
    global positions
    # Each agent moves randomly in x and y directions
    steps = np.random.uniform(-1, 1, (num_agents, 2))
    positions += steps

    # Ensure agents stay within bounds (simple boundary reflection)
    positions = np.clip(positions, -bounds, bounds)

    # Update scatter plot with new positions
    scat.set_offsets(positions)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=100, blit=True)
ani.save("agent_based_simulation.gif", writer='pillow', fps=100)
# Show animation
plt.show()