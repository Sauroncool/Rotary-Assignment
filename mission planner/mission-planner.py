from mission_inputs import *

Thrust = 2000 # N
fuel_density=0.804
def fuel_burn_rate(Thrust):
    m_dot = 0.03*Thrust
    return m_dot


Power_required = 75         # P=T*omega, Pmr+Ptr, From Flight simulator
Power_available = 93.43     # From the engine specifications
SFC = 0.35                  # From engine specifications

if Power_available>Power_required:
    mf_dot=SFC*Power_required                              # The TSFC here will vary as per the engine specification
    fuel_flow=mf_dot/fuel_density
else:
    print("Insufficient Power")

   
def update_weights(mf_dot):
    fuel_weight-=mf_dot*dt
    vehicle_weight-=min_dot+mf0-mf_dot*dt       # min_dot-->inert mass of helicopter, mf_dot=fuel burn weight
    if fuel_weight==0:
        dt=(tk_off_weight-vehicle_weight)/mf_dot
    return fuel_weight, vehicle_weight

def feasibility_check():                        # accounts for insufficient engine power/ potential stall/ insufficient fuel 





