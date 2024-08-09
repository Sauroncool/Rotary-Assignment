# Trial
# For Hover
import numpy as np

T = 100  # N
rho = 1.14  # kg/m^3
A = 10  # m^2
# Induced velocity
v = np.sqrt(T / (2 * rho * A))  # m/s
# power
P = T * v  # J/s
print('Power = ',P, 'J/s')
