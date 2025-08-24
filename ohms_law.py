# Ask the user to input current and resistance
try:
    current = float(input("Enter the current (I) in amperes: "))
    resistance = float(input("Enter the resistance (R) in ohms: "))

    # Calculate voltage using Ohm's Law: V = I * R
    voltage = current * resistance

    # Print the result
    print(f"The voltage (V) is: {voltage} volts")

except ValueError:
    print("Please enter valid numerical values for current and resistance.")

    