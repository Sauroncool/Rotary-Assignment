from Cl_update import Cyclic_Integrator

def main():
    # Create an instance of the Cyclic_Integrator class
    integrator = Cyclic_Integrator()

    # Call a method on the instance to perform the integration and calculate Thrust, Torque, and Power
    Thrust, Torque, Power = integrator.calculate_thrust_torque_power()

    # Print the results
    print(f"Thrust: {Thrust} N")
    print(f"Torque: {Torque} Nm")
    print(f"Power: {Power} W")

    Ct, Cq, Cp = integrator.BEMT_Coefficient_Calculator(Thrust, Torque, Power)
    # Print the results
    print(f"Ct: {Ct}")
    print(f"Cq: {Cq}")
    print(f"Cp: {Cp}")

if __name__ == "__main__":
    main()
