#Fetches input from the user input file and specifies blade geometry and parameters as per the instructions.
#from FS_user_inputs import get_pilot_inputs 
from FS_user_inputs import get_user_inputs

#MR_cyclic_pitch = theta      #Defining theta here to import in the II and CI for later.

# ADD MORE ROTOR SPECIFIC STUFF
#MK defined
user_inputs = get_user_inputs()
MR_radius = user_inputs['main_radius']          # main rotor blade radius, in metres
MR_nu_blades = user_inputs['main_number']       # number of blades in main rotor
MR_omega = user_inputs['main_omega']            # main rotor rotation rate, in rpm
MR_root_cutout = user_inputs['main_root_cutout']# main rotor root cutout, in metres
MR_taper = user_inputs['main_taper']            # main rotor taper, defined as taper = (chord_tip - chord_root) / (R_tip - R_root)
MR_twist = user_inputs['main_twist']            # main rotor twist, defined as twist = (theta_tip - theta_root) / (R_tip - R_root)
MR_collective = user_inputs['main_collective']  # main rotor collective theta input by pilot
MR_cyclic_a1 = user_inputs['main_cyclic_a1']    # main rotor cyclic theta - a1 input
MR_cyclic_a2 = user_inputs['main_cyclic_a2']    # main rotor cyclic theta - a2 input 
TR_radius       = user_inputs['tail_radius']      # tail rotor blade radius, in metres
TR_nu_blades    = user_inputs['tail_number']      # number of blades in tail rotor
TR_omega        = user_inputs['tail_omega']  # tail rotor rotation rate, in rpm
TR_root_cutout  = user_inputs['tail_root_cutout'] # tail rotor root cutout, in metres
TR_taper        = user_inputs['tail_taper']    # tail rotor taper, defined as taper = (chord_tip - chord_root) / (R_tip - R_root)
TR_twist        = user_inputs['tail_twist']    # tail rotor twist, defined as twist = (theta_tip - theta_root) / (R_tip - R_root)
TR_collective   = user_inputs['tail_collective'] # tail rotor collective theta input by pilot
