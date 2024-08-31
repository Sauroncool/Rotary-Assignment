from Cl_update import calculate_thrust_torque_power, BEMT_Coefficient_Calculator,plotter

def main():

    # Call a method on the instance to perform the integration and calculate Thrust, Torque, and Power
    Thrust, Torque, Power = calculate_thrust_torque_power()
    plotter()

    # Print the results
    print(f"Thrust: {Thrust} N")
    print(f"Torque: {Torque} Nm")
    print(f"Power: {Power} W")

    Ct, Cq, Cp = BEMT_Coefficient_Calculator(Thrust, Torque, Power)
    # Print the results
    print(f"Ct: {2*Ct}")
    print(f"Cq: {2*Cq}")
    print(f"Cp: {2*Cp}")
    return Thrust, Torque

    #plotting=integrator.plot()

if __name__ == "__main__":
    main()
    #print(main())


