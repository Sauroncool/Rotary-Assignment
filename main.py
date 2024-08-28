from CI import Cyclic_Integrator  # Import the existing Cyclic_Integrator object

def main():
    # Perform the integration to calculate Thrust, Torque, and Power
    Thrust, Torque, Power = Cyclic_Integrator.Cyclic_Integrator()

    # Print the results
    print(f"Thrust: {Thrust} N")
    print(f"Torque: {Torque} Nm")
    print(f"Power: {Power} W")

if __name__ == "__main__":
    main()