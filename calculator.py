print("=== Ohm's Law Calculator ===")

# menu options
print("Select an option:")
print("1. Calculate Voltage (V)")
print("2. Calculate Current (I)")
print("3. Calculate Resistance (R)")

option = input("Enter your choice (1/2/3): ")

if option == '1':
    current = float(input("Enter the current (I) in amperes: "))
    resistance = float(input("Enter the resistance (R) in ohms: "))
    voltage = current * resistance
    print(f"The voltage (V) is: {voltage} volts")

elif option == '2':
    voltage = float(input("Enter the voltage (V) in volts: "))
    resistance = float(input("Enter the resistance (R) in ohms: "))
    current = voltage / resistance if resistance != 0 else 0
    print(f"The current (I) is: {current} amperes")

elif option == '3':
    voltage = float(input("Enter the voltage (V) in volts: "))
    current = float(input("Enter the current (I) in amperes: "))
    resistance = voltage / current if current != 0 else 0
    print(f"The resistance (R) is: {resistance} ohms")
else:
    print("Invalid option. Please enter 1, 2, or 3.")

while True:
    repeat = input(
        "Do you want to perform another calculation? (yes/no): ").strip().lower()
    if repeat == 'yes':
        print("\n=== Ohm's Law Calculator ===")
        print("Select an option:")
        print("1. Calculate Voltage (V)")
        print("2. Calculate Current (I)")
        print("3. Calculate Resistance (R)")

        option = input("Enter your choice (1/2/3): ")

        if option == '1':
            current = float(input("Enter the current (I) in amperes: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
            voltage = current * resistance
            print(f"The voltage (V) is: {voltage} volts")

        elif option == '2':
            voltage = float(input("Enter the voltage (V) in volts: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
            current = voltage / resistance if resistance != 0 else 0
            print(f"The current (I) is: {current} amperes")

        elif option == '3':
            voltage = float(input("Enter the voltage (V) in volts: "))
            current = float(input("Enter the current (I) in amperes: "))
            resistance = voltage / current if current != 0 else 0
            print(f"The resistance (R) is: {resistance} ohms")
        else:
            print("Invalid option. Please enter 1, 2, or 3.")
    elif repeat == 'no':
        print("Thank you for using the Ohm's Law Calculator!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
