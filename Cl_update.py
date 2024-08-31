# Integrates forces and moments over a complete rotor cycle. Implements the BE Momentum Theory by definition.
import numpy as np
from Airfoil import *
from Blade import *
from Inflow import *

V = vehicle_velocity
omega = MR_omega
R_root = MR_root_radius
R = MR_radius
b = MR_nu_blades  # no of blades
density = 1.225

#sigma = (0.5 * (MR_radius-MR_root_radius)*(MR_root_chord + MR_taper*MR_root_chord))*b/(np.pi*MR_radius**2)
sigma = 0.0636

lamda_c = V / (omega * R)
lamda_values = []
stepsize = 0.01
r_values = np.arange(R_root, R, stepsize)


def chord(r, taper=MR_taper):
    chord = MR_root_chord * (1 + ((taper - 1) / (MR_radius - MR_root_radius)) * (
                r - MR_root_radius))  # Modify as needed based on your formula
    return chord


def phi(r):  # In degrees
    phi = np.arctan((V + v(r)) / (omega * r)) * 180 / np.pi
    #print(phi)
    return phi


def theta(r):  # In degrees
    theta = MR_cyclic_a1 + MR_cyclic_a2 + MR_collective + MR_twist * (r - MR_root_radius) / (MR_radius - MR_root_radius)
    #print(theta)
    return theta


def AOA(r):  # Angle of Attack as a function of r (in degrees)
    AOA = theta(r) - phi(r)
    return AOA


polar_data = read_polar_data()


def Cl(aoa, data=polar_data):  # Cl as a function of AOA
    alphas = [entry['aoa'] for entry in data]
    cls = [entry['cl'] for entry in data]
    # Convert lists to numpy arrays for interpolation
    alphas = np.array(alphas)
    cls = np.array(cls)
    # Use numpy to interpolate CL at the requested AOA
    #cl_interp = np.interp(aoa, alphas, cls)
    cl_interp = 5.75 * aoa * np.pi / 180
    return cl_interp


def Cd(aoa, data=polar_data):  # Cd as a function of AOA
    alphas = [entry['aoa'] for entry in data]
    cds = [entry['cd'] for entry in data]
    # Convert lists to numpy arrays for interpolation
    alphas = np.array(alphas)
    cds = np.array(cds)
    # Use numpy to interpolate CD at the requested AOA
    #cd_interp = np.interp(aoa, alphas, cds)
    cd_interp = 0.0113 + 1.25 * (aoa * np.pi / 180) ** 2
    return cd_interp


def a(aoa, h=1e-2):  # dcl/d_alpha as a function of AOA (per radian)
    cl_plus = Cl(aoa + h)
    cl_minus = Cl(aoa - h)

    #dcl_dalpha = ((cl_plus - cl_minus) / (2 * h)) * 180/np.pi  # aoa is in degrees thus multiplying by this factor
    dcl_dalpha = 5.75
    #print(dcl_dalpha)
    return dcl_dalpha


def F(r, lamda_val):
    f = (b / 2) * ((1 - r / R) / lamda_val)
    return (2 / np.pi) * np.arccos(np.exp(-f))


def lamda_func(r, F_val):
    lamda_val = np.sqrt(((sigma * a(r) / (
            16 * F_val)) - lamda_c / 2) ** 2 + sigma * a(r) * theta(r) * np.pi / 180 * r / (
                                8 * F_val * R)) - (
                        sigma * a(r) / (16 * F_val) - lamda_c / 2)

    return lamda_val


def solve_interdependent(r, tol=1e-8, max_iter=100):
    lamda_val = 0.02  # Initialisation
    for i in range(max_iter):
        F_val = F(r, lamda_val)
        new_lamda_val = lamda_func(r, F_val)
        if np.abs(new_lamda_val - lamda_val) < tol:
            break  # convergence reached
        lamda_val = new_lamda_val
    return F_val, new_lamda_val


# Call the function for each R_root and store the result
def calculate_lamda_values():
    for r in r_values:
        F_val, lamda_val = solve_interdependent(r)
        lamda_values.append((r, lamda_val))  # storing lamda_val for corresponding r


# As we have now have lamda value for each descrete r we will make a function out of this
def lamda(r):
    for r_val, lamda_val in lamda_values:
        if r_val == r:
            #print(lamda_val)
            return lamda_val


def v(r):
    v = lamda(r) * omega * R - V
    #print(v)
    return v


def Ut(r):
    return omega * r


def Up(r):
    return V + v(r)


def calculate_thrust_torque_power():
    calculate_lamda_values()

    Thrust = b * sum((0.5 * density * (Ut(r) ** 2 + Up(r) ** 2) * chord(r) *
                      (Cl(AOA(r)) * np.cos(phi(r) * np.pi / 180) - Cd(
                          AOA(r)) * np.sin(
                          phi(r) * np.pi / 180))) * stepsize
                     for r in r_values)

    Torque = b * sum((r * 0.5 * density * (Ut(r) ** 2 + Up(r) ** 2) * chord(r) *
                      (Cd(AOA(r)) * np.cos(phi(r) * np.pi / 180) + Cl(
                          AOA(r)) * np.sin(
                          phi(r) * np.pi / 180))) * stepsize
                     for r in r_values)

    Power = omega * Torque
    # print(sigma)
    return Thrust, Torque, Power


def BEMT_Coefficient_Calculator(Thrust, Torque, Power):
    Ct = Thrust / (density * (np.pi * R ** 2) * (omega * R) ** 2)
    Cq = Torque / (density * (np.pi * R ** 2) * R * (omega * R) ** 2)
    Cp = Power / (density * (np.pi * R ** 2) * (omega * R) ** 3)
    return Ct, Cq, Cp

    # def plot(self):
    #     plt.plot(r_values, thrust(r_values))
    #     plt.xlabel("r_values")
    #     plt.ylabel("Thrust")
    #     plt.title("Thrust vs r_values")
    #     plt.show()
