import numpy as np
from Atmosphere import Atmosphere

atmos = Atmosphere()
rho = atmos.density

# Placeholder Values
a = 1.5
V = 15
omega = 400 * 2 * np.pi / 60
R = 10
R_root = 1.5
theta = 5 * np.pi / 180
sigma = 0.1
c = 0.5
b = 3
phi = np.pi / 6
Cl = 1.2
Cd = 0.4

# Equations
lamda_c = V / (omega * R)


# From here we will calculate and iterate lamda
def F(r, lamda_val):
    f = (b / 2) * ((1 - r / R) / lamda_val)
    return (2 / np.pi) * np.arccos(np.exp(-f))


def lamda_func(r, F_val):
    lamda_val = np.sqrt(((sigma * a / (16 * F_val)) - lamda_c / 2) ** 2 + sigma * a * theta * r / (8 * F_val * R)) - (
            sigma * a / (16 * F_val) - lamda_c / 2)
    return lamda_val


# List to store lamda_val for each r
lamda_values = []

step = 0.1
r_values = np.arange(R_root, R, step)  # Generate the r values

for r in r_values:
    def solve_interdependent(r, tol=1e-6, max_iter=100):  # Using it to solve interdependent lamda_func and F functions.
        lamda_val = lamda_c  # Initial guess for lamda
        for i in range(max_iter):
            F_val = F(r, lamda_val)
            new_lamda_val = lamda_func(r, F_val)

            if np.abs(new_lamda_val - lamda_val) < tol:
                break  # Convergence reached

            lamda_val = new_lamda_val

        return F_val, lamda_val


    # Call the function for each r and store the result
    F_val, lamda_val = solve_interdependent(r)
    lamda_values.append((r, lamda_val))


# As we have now have lamda value for each descrete r we will make a function out of this
def lamda(r):
    for r_val, lamda_val in lamda_values:
        if r_val == r:
            return lamda_val


def v(r):
    v = lamda(r) * omega * R - V
    return v


def U_T(r):
    return omega * r


def U_P(r):
    return V + v(r)


thrust = b * sum(0.5 * rho * (U_T(r) ** 2 + U_P(r) ** 2) * c * (Cl * np.cos(phi) - Cd * np.sin(phi)) for r in
                 r_values)

torque = b * sum(r * 0.5 * rho * (U_T(r) ** 2 + U_P(r) ** 2) * c * (Cd * np.cos(phi) + Cl * np.sin(phi)) for r in
                 r_values)

power = omega * torque

print(power)
