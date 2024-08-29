import tkinter as tk
from tkinter import ttk

'''
User I/Ps (to be) taken (For my reference):

bld_main_radius
bld_main_rootchord
bld_main_nublades
bld_main_rootcut
bld_main_taper
bld_main_twist
bld_tail_radius
bld_tail_chord
bld_tail_nublades
bld_tail_rootcut
bld_tail_taper
bld_tail_twist

'''

def get_user_inputs():
    # takes User inputs from the entry fields.
    user_inputs = {
        'MR_radius': float(main_radius_entry.get()),
        'MR_nu_blades': int(main_number_entry.get()),
        'MR_omega': float(main_omega_entry.get()),
        'MR_root_cutout': float(main_rc_entry.get()),
        'MR_taper': float(main_taper_entry.get()),
        'MR_twist': float(main_twist_entry.get()),
        'MR_collective': float(main_collective_entry.get()),
        'MR_cyclic_a1': float(main_cyclic_a1_entry.get()),
        'MR_cyclic_a2': float(main_cyclic_a2_entry.get()),
        'TR_radius': float(tail_radius_entry.get()),
        'TR_nu_blades': int(tail_number_entry.get()),
        'TR_omega': float(tail_omega_entry.get()),
        'TR_root_cutout': float(tail_root_cutout_entry.get()),
        'TR_taper': float(tail_taper_entry.get()),
        'TR_twist': float(tail_twist_entry.get()),
        'TR_collective': float(tail_collective_entry.get())
    }
    print(user_inputs)  # For debugging, print the inputs
    return user_inputs

# Function to get pilot inputs
def get_pilot_inputs():
    MR_collective = float(MR_collective_entry.get())
    MR_cyclic_pitch = float(MR_cyclic_pitch_entry.get())
    MR_cyclic_roll = float(MR_cyclic_roll_entry.get())
    TR_collective = float(TR_collective_entry.get())
    print(MR_collective, MR_cyclic_pitch, MR_cyclic_roll, TR_collective)
    return MR_collective, MR_cyclic_pitch, MR_cyclic_roll, TR_collective

# Main window
root = tk.Tk()
root.title("Helicopter Flight Simulator")

# Input fields for the main rotor I/Ps
tk.Label(root, text="Main Rotor Radius").grid(row=0, column=0)
main_radius_entry = ttk.Entry(root)
main_radius_entry.grid(row=0, column=1)

tk.Label(root, text="Main Rotor Frequency").grid(row=1, column=0)
main_number_entry = ttk.Entry(root)
main_number_entry.grid(row=1, column=1)

tk.Label(root, text="Main Rotor Omega").grid(row=2, column=0)
main_omega_entry = ttk.Entry(root)
main_omega_entry.grid(row=2, column=1)

tk.label(root, text="Main Rotor Root Cutout").grid(row=3, column=0)
main_rc_entry = ttk.entry(root)
main_rc_entry.grid(row=3, column=1)

tk.label(root, text="Main Rotor Taper").grid(row=4, column=0)
main_taper_entry = ttk.entry(root)
main_taper_entry.grid(row=4, column=1)

tk.label(root, text="Main Rotor Twist").grid(row=5, column=0)
main_twist_entry = ttk.entry(root)
main_twist_entry.grid(row=5, column=1)

# Tail rotor I/P parameters
        # for my reference      
        # 'TR_radius': float(tail_radius_entry.get()),
        # 'TR_nu_blades': int(tail_number_entry.get()),
        # 'TR_omega': float(tail_omega_entry.get()),
        # 'TR_root_cutout': float(tail_root_cutout_entry.get()),
        # 'TR_taper': float(tail_taper_entry.get()),
        # 'TR_twist': float(tail_twist_entry.get()),
tk.label(root, text="Tail Rotor radius").grid(row=6, column=0)
tail_radius_entry = ttk.entry(root)
tail_radius_entry.grid(row=6, column=1)




# Input fields for the pilot controls
tk.Label(root, text="Main Rotor Collective Pitch (Degrees)").grid(row=10, column=0)
main_collective_entry = ttk.Entry(root)
main_collective_entry.grid(row=10, column=1)

tk.Label(root, text="Main Rotor Cyclic Pitch (Degrees)").grid(row=11, column=0)
main_cyclic_a1_entry = ttk.Entry(root)
main_cyclic_a1_entry.grid(row=11, column=1)

tk.Label(root, text="Main Rotor Cyclic Roll (Degrees)").grid(row=12, column=0)
main_cyclic_a2_entry = ttk.Entry(root)
main_cyclic_a2_entry.grid(row=12, column=1)

tk.Label(root, text="Tail Rotor Collective Pitch (Degrees)").grid(row=13, column=0)
tail_collective_entry = ttk.Entry(root)
tail_collective_entry.grid(row=13, column=1)

# Button to submit the inputs
submit_button = ttk.Button(root, text="Submit", command=get_user_inputs)
submit_button.grid(row=20, column=0)

pilot_button = ttk.Button(root, text="Get Pilot Inputs", command=get_pilot_inputs)
pilot_button.grid(row=20, column=1)

# Start the GUI event loop
root.mainloop()
