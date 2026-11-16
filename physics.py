# COS 101 Assignment
# Five Physics Operations Using Functions and a While Loop

# 1. Speed
def calculate_speed(distance, time):
    return distance / time

# 2. Acceleration
def calculate_acceleration(final_velocity, initial_velocity, time):
    return (final_velocity - initial_velocity) / time

# 3. Force
def calculate_force(mass, acceleration):
    return mass * acceleration

# 4. Work Done
def calculate_work(force, distance):
    return force * distance

# 5. Kinetic Energy
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

# Main program
while True:
    print("\nPHYSICS CALCULATOR")
    print("1. Speed")
    print("2. Acceleration")
    print("3. Force")
    print("4. Work Done")
    print("5. Kinetic Energy")

    choice = input("Choose a physics operation (1-5): ")

    if choice == "1":
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            print("Speed:", calculate_speed(distance, time), "m/s")

    elif choice == "2":
        final_velocity = float(input("Enter final velocity: "))
        initial_velocity = float(input("Enter initial velocity: "))
        time = float(input("Enter time: "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            print("Acceleration:", calculate_acceleration(final_velocity, initial_velocity, time), "m/s^2")

    elif choice == "3":
        mass = float(input("Enter mass: "))
        acceleration = float(input("Enter acceleration: "))
        print("Force:", calculate_force(mass, acceleration), "N")

    elif choice == "4":
        force = float(input("Enter force: "))
        distance = float(input("Enter distance: "))
        print("Work Done:", calculate_work(force, distance), "J")

    elif choice == "5":
        mass = float(input("Enter mass: "))
        velocity = float(input("Enter velocity: "))
        print("Kinetic Energy:", calculate_kinetic_energy(mass, velocity), "J")

    else:
        print("Invalid choice. Please select 1-5.")

    again = input("\nDo you want to perform another calculation? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break
