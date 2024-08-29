**Rotary-Assignment:** <br>
*The program has been made modular. The following classes have been created as per the instructions given:*<br>
0. FS_user_inputs (user inputs to be taken for the flight simulator)
1. Airfoil
2. Atmosphere
3. CI (Cyclic Integrator)
4. II (Instantaneous Integrator)
5. Inflow

Variables (Putting it out here for uniform use everywhere):

1. BLADE(S)

MR_radius          -->    main rotor blade radius, in metres<br>
MR_nu_blades       -->    number of blades in main rotor<br>
MR_omega           -->    main rotor rotation rate, in rpm<br>
MR_root_cutout     -->    main rotor root cutout, in metres<br>
MR_taper           -->    main rotor taper, defined as taper    (chord_tip - chord_root) / (R_tip - R_root)<br>
MR_twist           -->    main rotor twist, defined as twist    (theta_tip - theta_root) / (R_tip - R_root)<br>
MR_collective      -->    main rotor collective theta input by pilot<br>
MR_cyclic_a1       -->    main rotor cyclic theta - a1 input<br>
MR_cyclic_a2       -->    main rotor cyclic theta - a2 input <br>
TR_radius          -->    tail rotor blade radius, in metres<br>
TR_nu_blades       -->    number of blades in tail rotor<br>
TR_omega           -->    tail rotor rotation rate, in rpm<br>
TR_root_cutout     -->    tail rotor root cutout, in metres
TR_taper           -->    tail rotor taper, defined as taper    (chord_tip - chord_root) / (R_tip - R_root)<br>
TR_twist           -->    tail rotor twist, defined as twist    (theta_tip - theta_root) / (R_tip - R_root)<br>
