from main import *
from main_tail import *
z_trcg = 0.5
z_mrcg = 1.5
x_mrcg = 0.5
x_trcg = 3
T_tail = main_tail()[0]  # Tail Thrust
T_main = main()[0]  # Thrust main
M_main = main()[1]  # Moment main
M_tail = main_tail()[1]  # tail Moment

Mx_cg = -T_tail * z_trcg
My_cg = -T_main * x_mrcg - M_tail
Mz_cg = -T_tail * x_trcg + M_main

Fx_cg = 0
Fy_cg = -T_tail
Fz_cg = T_main

# Print the results
print(f"Mx: {Mx_cg} ")
print(f"My: {My_cg} ")
print(f"Mz: {Mz_cg} ")

print(f"Fx: {Fx_cg} ")
print(f"Fy: {Fy_cg} ")
print(f"Fz: {Fz_cg} ")
