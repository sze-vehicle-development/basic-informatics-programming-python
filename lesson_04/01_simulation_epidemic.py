import matplotlib.pyplot as plt
import random

# Parameters
population_size = 100   # Total number of people
initial_infected = 5    # Initial number of infected individuals
infection_chance = 0.1  # Probability of infecting a neighbor per step
recovery_chance = 0.03  # Probability of recovery per step
num_steps = 50          # Simulation duration in steps

# States: 0 = Susceptible, 1 = Infected, 2 = Recovered
population = [0] * population_size
for i in range(initial_infected):
    population[i] = 1  # Start with some infected individuals

# Lists to track counts of each state over time
susceptible_counts = []
infected_counts = []
recovered_counts = []

# Run the simulation
for step in range(num_steps):
    new_population = population.copy()  # Copy to avoid simultaneous state changes

    for i in range(population_size):
        if population[i] == 1:  # If infected
            # Chance of recovery
            if random.random() < recovery_chance:
                new_population[i] = 2  # Recover

            # Spread infection to neighbors
            else:
                for j in range(max(0, i-1), min(population_size, i+2)):  # Immediate neighbors
                    if population[j] == 0 and random.random() < infection_chance:
                        new_population[j] = 1  # Infect susceptible neighbor

    # Update population state for the next step
    population = new_population

    # Count each state for tracking
    susceptible_counts.append(population.count(0))
    infected_counts.append(population.count(1))
    recovered_counts.append(population.count(2))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(susceptible_counts, label='Susceptible', color='blue')
plt.plot(infected_counts, label='Infected', color='red')
plt.plot(recovered_counts, label='Recovered', color='green')
plt.title('Stochastic Epidemic Spread Simulation')
plt.xlabel('Time Step')
plt.ylabel('Number of Individuals')
plt.legend()
plt.grid()
plt.show()