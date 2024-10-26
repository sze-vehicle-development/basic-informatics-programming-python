from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print(p.x)

# Example #2
# Define namedtuple
Car = namedtuple("Car", ["make", "model", "year"])

# Create instance
my_car = Car("Toyota", "Corolla", 2020)

# Access fields
print(my_car.make)    # Toyota
print(my_car._asdict())  # {'make': 'Toyota', 'model': 'Corolla', 'year': 2020}