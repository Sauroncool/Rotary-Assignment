# Ref. 1. User Inputs: Allows users to specify geometric, aerodynamic, structural, and functional 
# details of the helicopter rotors (main and tail), fuselage, engine, etc.

def get_user_inputs():
    inputs = {}
    # Input parameter stuff

def get_pilot_inputs():
    MR_collective      =float(input("Main Rotor Collective pitch (Degrees): "))        # Altitude control
    MR_cyclic_pitch    =float(input("Main Rotor Cyclic pitch (Degrees): "))            # Helicopter Pitch control/ theta
    MR_cyclic_roll     =float(input("Main Rotor Cyclic Roll (Degrees): "))             # Helicopter Roll/sideway tilt
    TR_collective      =float(input("Tail Rotor Collective pitch (Degrees): "))        # Yaw control
    return MR_collective, MR_cyclic_pitch, MR_cyclic_roll, TR_collective
