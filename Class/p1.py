"""To accept an object mass in kilograms and velocity in meters per second and display its momentum.
Momentum is calculated as e=mc2 where m is the mass of the object and c is its velocity."""
m = int(input("Enter mass "))
v = int(input("Enter Velocity "))
print("Energy = ", m * (v**2))