from Cl_update import Cyclic_Integrator  # Import the Cyclic_Integrator class

def main():
    # Create an instance of the Cyclic_Integrator class
    integrator = Cyclic_Integrator()

    # Call a method on the instance to perform the integration and calculate Thrust, Torque, and Power
    Thrust, Torque, Power = integrator.Cyclic_Integrator()

    # Print the results
    print(f"Thrust: {Thrust} N")
    print(f"Torque: {Torque} Nm")
    print(f"Power: {Power} W")

if __name__ == "__main__":
    main()
