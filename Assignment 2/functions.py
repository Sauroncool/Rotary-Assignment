import numpy as np
def Thrust(ρ,A,V_inf,α,v):
    return ρ * A * np.sqrt((V_inf*np.cos(α))**2 + (V_inf*np.sin(α))**2) * 2 * v

def Power(ρ,A,V_inf,α,v, D):
    parasitic= D*V_inf
    induced = Thrust(ρ,A,V_inf,α,v) * v
    #profile =
    return parasitic +induced #+ profile


Up = V_inf * np.sin(alpha_tpp) + v + r*(dβ/dt) + V_inf * np.sin(β) *  np.cos(Ψ)
Ut = omega*r + V_inf*np.cos(alpha_tpp) np.sin(Ψ)

α = θ - np.arctan(Up/Ut)


# Approx
α = (1/Ut)*(omega*r(theta_0 + theta_tw * r/R + (theta_1c-beta_1s) * cos(ψ) + (tehta_1s + beta_1c)*sin(ψ)) + V*( theta_0 + theta_tw*r/R )*np.sin(ψ) + V
            *(theta_1c - beta_1s)*np.cos(ψ)*np.sin(ψ) + V * (theta_1s + beta_1c)*(np.sin(ψ))**2 - v* beta_0* np.cos(ψ) - V * alpha_tpp - v)