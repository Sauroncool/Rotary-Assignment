# Ref. 1. User Inputs: Allows users to specify geometric, aerodynamic, structural, and functional 
# details of the helicopter rotors (main and tail), fuselage, engine, etc.

def get_user_inputs():
    user_inputs = {
        'main_radius': 10,
        'main_number': 3,
        'main_omega': 200,
        'main_root_cutout': 1,
        'main_taper': 0.5,
        'main_twist': 5,
        'main_collective': 10,
        'main_cyclic_a1': 0,
        'main_cyclic_a2': 0,
        'tail_radius': 1,
        'tail_number': 2,
        'tail_omega': 100,
        'tail_root_cutout': 0.1,
        'tail_taper': 0.75,
        'tail_twist': 2,
        'tail_collective': 3,
    }
    return user_inputs
    # Input parameter stuff

# def get_pilot_inputs():
#     MR_collective      =float(input("Main Rotor Collective pitch (Degrees): "))        # Altitude control
#     MR_cyclic_pitch    =float(input("Main Rotor Cyclic pitch (Degrees): "))            # Helicopter Pitch control/ theta
#     MR_cyclic_roll     =float(input("Main Rotor Cyclic Roll (Degrees): "))             # Helicopter Roll/sideway tilt
#     TR_collective      =float(input("Tail Rotor Collective pitch (Degrees): "))        # Yaw control
#     return MR_collective, MR_cyclic_pitch, MR_cyclic_roll, TR_collective
