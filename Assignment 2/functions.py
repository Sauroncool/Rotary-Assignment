import numpy as np

V_inf = 20  # m/s
omega = 100  # rad/s
R = 5
ψ = 75 * 2 * np.p  #degrees
rho = 1.225
C = 1
M = 20  # mass of blade
σ = 0.5  # solidity

theta_0 = 5 * np.pi / 180  #degrees
theta_1c = 2 * np.pi / 180  #degrees
theta_1s = 3 * np.pi / 180  #degrees

theta_tw = 5 * np.pi / 180  # twist

r_values = np.arange(0.5, 5, 0.1)


def Thrust(ρ, A, V_inf, alpha_tpp, v_mean):
    return ρ * A * np.sqrt((V_inf * np.cos(alpha_tpp)) ** 2 + (V_inf * np.sin(alpha_tpp) + v_mean) ** 2) * 2 * v_mean


# def Power(ρ, A, V_inf, α, v, D):
#     parasitic = D * V_inf
#     induced = Thrust(ρ, A, V_inf, α, v) * v
#     #profile =
#     return parasitic + induced  #+ profile


lamda_c = V_inf / (omega * R)

lamda = 0.2
μ = V_inf / (omega * R)
γ = rho * 2 * np.pi * C * R ** 4 / ((M * R ** 2) / 3)
beta_0 = γ * ((theta_0 + 0.8 * theta_tw) * (1 + μ ** 2) / 8 - (theta_tw * μ ** 2) / 60 - (lamda - μ * theta_1s))
beta_1s = theta_1c - (4 * μ * beta_0 / 3) / (1 + 0.5 * μ ** 2)
beta_1c = theta_1s - (8 * μ * (theta_0 + theta_tw * 0.75 - 0.75 * lamda - μ * theta_1s) / 3) / (1 - 0.5 * μ ** 2)
alpha_s = 2 * np.pi / 180  # assumed
alpha_tpp = alpha_s + beta_1c


def lamda_G(v):
    return (V_inf * np.sin(alpha_tpp) + v) / (omega * R)


def lamda_iG(r):
    return np.sqrt((σ * 2 * np.pi / 16 - lamda_c / 2) ** 2 + (σ * 2 * np.pi / 8) * theta_tw * r / R) - (
            σ * 2 * np.pi / 16 - lamda_c / 2)


def lamda_i(r):
    return lamda_iG(r) * (1 + ((4 * μ) / (3 * lamda_G(v))) / (1.2 + μ / lamda_G(v))) * (r / R) * np.cos(ψ)


def v_new(r):
    return lamda_i(r) * omega * R - V_inf


v = 0


def vel(r):
    for i in range(100):
        if v_new(r) - v < 0.1:
            break
        v = v_new(r)
    return v


v_mean = (sum(vel(r) * r ** 2) for r in r_values) / R ** 2

# def Ut(r):
#     return omega * r + V_inf * np.cos(alpha_tpp) * np.sin(ψ)
#
#
# # Approx
# def α(r):
#     return (1 / Ut(r)) * (omega * r * (theta_0 + theta_tw * r / R + (theta_1c - beta_1s) * np.cos(ψ) + (theta_1s + beta_1c) * np.sin(ψ)) + V_inf * (theta_0 + theta_tw * r / R) * np.sin(ψ) + V_inf* (theta_1c - beta_1s) * np.cos(ψ) * np.sin(ψ) + V_inf * (theta_1s + beta_1c) * (np.sin(ψ)) ** 2 - v * beta_0 * np.cos(ψ) - V_inf * alpha_tpp - v)
