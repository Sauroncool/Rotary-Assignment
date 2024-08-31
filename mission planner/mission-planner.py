from mission_inputs import *
from CI import *
from FS_user_inputs2 import *
from Atmosphere import *


rho=Atmosphere.calc_conditions(tk_off_altitude).density
AOA_stall=14
Blade_Area=0.8                                                      #Blade width*Blade length
initial_omega=user_inputs.main_omega
theta=Cyclic_Integrator().theta

def Lift_Calculator(Cl, Blade_velocity):
    Lift=0.5*rho*Blade_velocity**2*Cl*Blade_Area
    return Lift


for omega in np.linspace(initial_omega, initial_omega+100, 50):
    for theta in np.linspace(theta, theta+15, 15):
        alpha=Cyclic_Integrator.AOA
        if alpha==AOA_stall:
            Cl=2*np.pi*alpha
            Blade_velocity=omega*user_inputs.r
            Lift=Lift_Calculator(Cl, Blade_velocity)
            print(f"The maximum take off lift is {Lift}")
            break


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
SFC = 0.35/3600                  # From engine specifications

if Power_available>Power_required:
    mf_dot=SFC*Power_required                              # The TSFC here will vary as per the engine specification
    # fuel_flow=mf_dot/fuel_density
else:
    print("Insufficient Power")

   
def update_weights(mf_dot):
    fuel_weight-=mf_dot*dt
    vehicle_weight-=m_in+mf0-mf_dot*dt       # min_dot-->inert mass of helicopter, mf_dot=fuel burn weight
    if fuel_weight==0:
        dt=(m_in-vehicle_weight)/mf_dot
    return fuel_weight, vehicle_weight

# def feasibility_check():                        # accounts for insufficient engine power/ potential stall/ insufficient fuel 





