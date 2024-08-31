# Ref. 1. User Inputs: Allows users to specify geometric, aerodynamic, structural, and functional 
# details of the helicopter rotors (main and tail), fuselage, engine, etc.
import numpy as np
def get_user_inputs():
    user_inputs = {
        'main_radius': 2, # 0.762
        'main_number': 3, # 3
        'main_omega': 960*2*np.pi/60,
        'main_root_radius': 0.125, # 0.125
        'main_root_chord': 0.0508, # 0.0508
        'main_taper': 1,
        'main_twist': 0,
        'main_collective': 5,
        'main_cyclic_a1': 0,
        'main_cyclic_a2': 0,
        'tail_radius': 0.5,
        'tail_number': 2,
        'tail_omega': 960*2*np.pi/60,
        'tail_root_radius': 0.05,
        'tail_root_chord': 0.2,
        'tail_taper': 1,
        'tail_twist': 0,
        'tail_collective': 10,
    }
    return user_inputs
    # Input parameter stuff

# def get_pilot_inputs():
#     MR_collective      =float(input("Main Rotor Collective pitch (Degrees): "))        # Altitude control
#     MR_cyclic_pitch    =float(input("Main Rotor Cyclic pitch (Degrees): "))            # Helicopter Pitch control/ theta
#     MR_cyclic_roll     =float(input("Main Rotor Cyclic Roll (Degrees): "))             # Helicopter Roll/sideway tilt
#     TR_collective      =float(input("Tail Rotor Collective pitch (Degrees): "))        # Yaw control
#     return MR_collective, MR_cyclic_pitch, MR_cyclic_roll, TR_collective
