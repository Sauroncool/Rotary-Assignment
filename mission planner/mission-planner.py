from mission_inputs import *

Thrust = 2000 # N
def fuel_burn_rate(Thrust):
    m_dot = 0.03*Thrust
    return m_dot


def update_weights(fuel_weight, m_dot):
    fuel_weight-=mf_dot*dt
    vehicle_weight-=min_dot+mf0-mf_dot*dt       # min_dot-->inert mass of helicopter, mf_dot=fuel burn weight
    return fuel_weight, vehicle_weight



