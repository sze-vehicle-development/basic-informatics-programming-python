import random
import matplotlib.pyplot as plt

# Parameters
num_customers = 50            # Number of customers in the simulation
arrival_rate = 2              # Average number of customers arriving per minute
service_rate = 3              # Average number of customers served per minute

# Variables to track
arrival_times = []
service_start_times = []
departure_times = []

# Simulation events
current_time = 0
queue = []
teller_busy_until = 0

for i in range(num_customers):
    # Customer arrival
    inter_arrival_time = random.expovariate(arrival_rate)
    current_time += inter_arrival_time
    arrival_times.append(current_time)
    queue.append(current_time)

    # Service start time (when teller is free and customer is first in queue)
    if teller_busy_until <= current_time:
        service_start_time = current_time
    else:
        service_start_time = teller_busy_until
    service_start_times.append(service_start_time)

    # Service duration and departure
    service_duration = random.expovariate(service_rate)
    teller_busy_until = service_start_time + service_duration
    departure_times.append(teller_busy_until)

# Calculate waiting times and total time in system
waiting_times = [service_start_times[i] - arrival_times[i] for i in range(num_customers)]
total_times = [departure_times[i] - arrival_times[i] for i in range(num_customers)]

# Plot waiting times and total times
plt.figure(figsize=(12, 6))
plt.plot(range(num_customers), waiting_times, label="Waiting Time", color="orange", marker="o")
plt.plot(range(num_customers), total_times, label="Total Time in System", color="blue", marker="x")
plt.xlabel("Customer Number")
plt.ylabel("Time (minutes)")
plt.title("Event-Based Simulation of Bank Queue System")
plt.legend()
plt.grid()
plt.show()