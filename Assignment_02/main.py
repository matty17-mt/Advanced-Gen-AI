from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles and a renter
car = Vehicle("Porsche", "Carrera", "(9M9119)")
electric_car = ElectricCar("BYD", "Model 2026", "8M808", 80)
motorbike = Motorbike("Yamaha", "YMH2026", "8M197", 500)

renter = Renter("Matty", 670514)

# Rent and return a vehicle
print(car)

car.rent()
renter.rented.append(car)
print(car)

car.return_vehicle()
renter.rented.remove(car)
print(car)

# Test invalid renter name
try:
    Renter("", 670514)
except ValueError as e:
    print("Caught ValueError:", e)

# Test invalid license number
try:
    Renter("Shine", 0)
except ValueError as e:
    print("Caught ValueError:", e)

# Test polymorphism
vehicles = [car, electric_car, motorbike]

print("\nAll vehicles:")
for vehicle in vehicles:
    print(vehicle)
