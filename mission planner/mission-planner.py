from mission_inputs import *

Thrust = 2000 # N
def fuel_burn_rate(Thrust):
    m_dot = 0.03*Thrust
    return m_dot

def fuel_weight(w_0,t):
    w_f = w_0 - fuel_burn_rate(Thrust) * t
    return w_f