import numpy as np

T = 100  # N
rho_inf = 1.14  # kg/m^3
A = 10  # m^2
V = 5  # Climb Speed

# Induced velocity
v = np.sqrt((V / 2) ** 2 + (T / (2 * rho_inf * A))) - V / 2  # m/s
# Power
P = T * (V + v)

# T = P * A * (V + v) * 2 * v
# m_dot = P * A * (V + v)


