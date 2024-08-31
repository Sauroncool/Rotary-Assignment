from mission_inputs import *
from Cl_update import AOA
from FS_user_inputs2 import *
from Atmosphere import *
from Blade import *

T, P, rho=Atmosphere.calc_conditions(tk_off_altitude)
print(f"density= {rho} kg/m^3")
# rho=1.225
AOA_stall=10
Blade_Area=0.8
# initial_omega=MR_omega
# main_collective=MR_collective

def Lift_Calculator(Cl, Blade_velocity):
    Lift=0.5*rho*Blade_velocity**2*Cl*Blade_Area
    return Lift


def MTOW_calculator(MR_omega, MR_collective, AOA_stall, MR_root_radius, MR_radius):
    r_values = np.arange(MR_root_radius, MR_radius, 0.01)
    for omega in np.linspace(MR_omega, MR_omega+500, 50):
        for MR_collective in np.linspace(MR_collective, MR_collective+15, 15):
            alpha=AOA(r_values)
            # print(alpha)
            alpha_max=max(alpha)
            r_max = r_values[np.argmax(alpha)]
            if alpha_max>=AOA_stall:
                Cl=2*np.pi*alpha_max*np.pi/180
                print(f"Cl Value= {Cl}")
                Blade_velocity=omega*r_max
                print(f"Blade velocity= {Blade_velocity} m/s")
                Lift=Lift_Calculator(Cl, Blade_velocity)
                Weight=Lift/9.81
                # print(f"The maximum take off Weight is {Weight} kg.")
                break
        break
    return Weight

MTOW=MTOW_calculator(MR_omega, MR_collective, AOA_stall, MR_root_radius, MR_radius)
print(f"The maximum take off Weight is {MTOW} kg.")
# while alpha1<AOA_stall:
#     alpha1=Cyclic_Integrator.AOA
#     if alpha1==AOA_stall:
#         break
#     omega+=1
#     while alpha2<AOA_stall:
#         alpha2=Cyclic_Integrator.AOA
#         if alpha2==AOA_stall:
#             break
#         twist+=1

# Thrust = 2000 # N
Qf     = 43.124             #MJ/kg
fuel_density=0.804          #kg/L

#     Not using this anymore
#     def fuel_burn_rate(Thrust):
#     m_dot = 0.03*Thrust
#     return m_dot


Power_required = 75         # P=T*omega, Pmr+Ptr, From Flight simulator
Power_available = 93.43     # From the engine specifications
SFC = 0.35                  # From engine specifications

if Power_available>Power_required:
    mf_dot=SFC*Power_required                # The TSFC here will vary as per the engine specification
    # fuel_flow=mf_dot/fuel_density
    print(f"Fuel burn rate: {mf_dot}")
else:
    print("Insufficient Power")

   
def update_weights(mf_dot):
    dt=200
    fuel_weight=mf0-mf_dot*dt
    
    vehicle_weight=m_in+mf0-mf_dot*dt       # min_dot-->inert mass of helicopter, mf_dot=fuel burn weight
    if fuel_weight==0:
        dt=(mf0)/mf_dot
        print(f"Time of flight: {dt}")
    return fuel_weight, vehicle_weight

FW, VW =update_weights(mf_dot)
print(f"Fuel weight: {FW} kg")
print(f"Vehicle Weight: {VW}")
# def feasibility_check():                        # accounts for insufficient engine power/ potential stall/ insufficient fuel 





