import numpy as np

# Placeholder Values
a = 1.5
V = 15
omega = 400*2*np.pi/60
R = 10
R_root = 1.5
theta = 5*np.pi/180
sigma = 0.1
rho = 1.14
c = 0.5
b = 3
phi = np.pi / 6
Cl = 1.2
Cd = 0.4

# Equations
lamda_c = V / (omega * R)


def lamda(r):
    lamda = np.sqrt((sigma * a / 16 - lamda_c / 2) ** 2 + sigma * a * theta * r / (8 * R)) - (
            sigma * a / 16 - lamda_c / 2)
    return lamda


def v(r):
    v = lamda(r) * omega * R - V
    return v


def U_T(r):
    return omega * r


def U_P(r):
    return V + v(r)


step = 0.01
thrust = b * sum(0.5 * rho * (U_T(r) ** 2 + U_P(r) ** 2) * c * (Cl * np.cos(phi) - Cd * np.sin(phi)) for r in
                 np.arange(R_root, R, step))

torque = b * sum(r * 0.5 * rho * (U_T(r) ** 2 + U_P(r) ** 2) * c * (Cd * np.cos(phi) + Cl * np.sin(phi)) for r in
                 np.arange(R_root, R, step))

power = omega * torque

print(power)
