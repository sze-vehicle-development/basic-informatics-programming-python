import matplotlib.pyplot as plt
import numpy as np

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to the n-th term."""
    fib_seq = [0, 1]
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def plot_continuous_fibonacci_spiral(n_terms):
    """Plot a continuous Fibonacci spiral."""
    # Generate Fibonacci sequence
    fib_seq = fibonacci_sequence(n_terms)

    # Initialize figure
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    ax.set_aspect('equal')

    # Starting point and angle
    x, y = 0, 0
    angle = 0  # Starting angle in degrees

    for i in range(2, len(fib_seq)):
        # Define the radius for the current segment
        radius = fib_seq[i]

        # Generate theta values for a quarter circle
        theta = np.linspace(np.radians(angle), np.radians(angle + 90), 100)

        # Compute x and y points of the arc
        x_arc = x + radius * np.cos(theta)
        y_arc = y + radius * np.sin(theta)

        # Plot the arc
        plt.plot(x_arc, y_arc, color='blue', lw=2)

        # Update x, y to the endpoint of the arc
        angle += 90  # Rotate by 90 degrees
        x += radius * np.cos(np.radians(angle))
        y += radius * np.sin(np.radians(angle))

    # Set plot limits
    max_radius = sum(fib_seq)
    plt.xlim(-max_radius, max_radius)
    plt.ylim(-max_radius, max_radius)
    plt.grid()
    plt.title("Continuous Fibonacci Spiral")
    plt.show()

# Plot the continuous Fibonacci spiral with 10 terms
plot_continuous_fibonacci_spiral(10)