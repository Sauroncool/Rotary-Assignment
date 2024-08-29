**Rotary-Assignment: **
*The program has been made modular. The following classes have been created as per the instructions given:*
0. FS_user_inputs (user inputs to be taken for the flight simulator)
1. Airfoil
2. Atmosphere
3. CI (Cyclic Integrator)
4. II (Instantaneous Integrator)
5. Inflow

Variables (Putting it out here for uniform use everywhere):

1. BLADE(S)

a. MR_radius          -->    main rotor blade radius, in metres
b. MR_nu_blades       -->    number of blades in main rotor
c. MR_omega           -->    main rotor rotation rate, in rpm
d. MR_root_cutout     -->    main rotor root cutout, in metres
e. MR_taper           -->    main rotor taper, defined as taper    (chord_tip - chord_root) / (R_tip - R_root)
f. MR_twist           -->    main rotor twist, defined as twist    (theta_tip - theta_root) / (R_tip - R_root)
g.MR_collective      -->    main rotor collective theta input by pilot
MR_cyclic_a1       -->    main rotor cyclic theta - a1 input
MR_cyclic_a2       -->    main rotor cyclic theta - a2 input 
TR_radius          -->    tail rotor blade radius, in metres
TR_nu_blades       -->    number of blades in tail rotor
TR_omega           -->    tail rotor rotation rate, in rpm
TR_root_cutout     -->    tail rotor root cutout, in metres
TR_taper           -->    tail rotor taper, defined as taper    (chord_tip - chord_root) / (R_tip - R_root)
TR_twist           -->    tail rotor twist, defined as twist    (theta_tip - theta_root) / (R_tip - R_root)
