import numpy as np
def Thrust(ρ,A,V_inf,α,v):
    return ρ * A * np.sqrt((V_inf*np.cos(α))**2 + (V_inf*np.sin(α))**2) * 2 * v

def Power(ρ,A,V_inf,α,v):
    parasitic= D*V_inf
    induced = Thrust(ρ,A,V_inf,α,v) * v
    profile =
    return parasitic +induced + profile