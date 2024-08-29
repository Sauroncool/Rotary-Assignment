# Integrates forces and moments over a complete rotor cycle. Implements the BE Momentum Theory by definition.
import numpy as np
from Airfoil import *
from Blade import *
from Inflow import *


class Cyclic_Integrator:
    def __init__(self, sigma=0.08, density=1.225):
        self.V = vehicle_velocity
        self.omega = MR_omega
        self.R_root = MR_root_radius
        self.R = MR_radius
        self.b = MR_nu_blades  # no of blades

        self.sigma = sigma
        self.density = density

        self.lamda_c = self.V / (self.omega * self.R)
        self.lamda_values = []
        self.stepsize = 0.1
        self.r_values = np.arange(self.R_root, self.R, self.stepsize)

    def chord(self, r, taper=MR_taper):
        chord = MR_root_chord*(1 + ((taper-1) / (MR_radius - MR_root_radius)) * (r-MR_root_radius)) # Modify as needed based on your formula
        return chord

    def phi(self, r):  # In degrees
        phi = np.arctan((self.V + self.v(r)) / (self.omega * r)) * 180 / np.pi
        return phi

    def theta(self, r):  # In degrees
        theta = MR_cyclic_a1 + MR_cyclic_a2 + MR_collective + MR_twist * (r-MR_root_radius)/(MR_radius-MR_root_radius)
        return theta

    def AOA(self, r):  # Angle of Attack as a function of r (in degrees)
        AOA = self.theta(r) - self.phi(r)
        return AOA

    polar_data = read_polar_data()

    def Cl(self, aoa, data=polar_data):  # Cl as a function of AOA
        alphas = [entry['aoa'] for entry in data]
        cls = [entry['cl'] for entry in data]
        # Convert lists to numpy arrays for interpolation
        alphas = np.array(alphas)
        cls = np.array(cls)
        # Use numpy to interpolate CL at the requested AOA
        cl_interp = np.interp(aoa, alphas, cls)
        return cl_interp

    def Cd(self, aoa, data=polar_data):  # Cd as a function of AOA
        alphas = [entry['aoa'] for entry in data]
        cds = [entry['cd'] for entry in data]
        # Convert lists to numpy arrays for interpolation
        alphas = np.array(alphas)
        cds = np.array(cds)
        # Use numpy to interpolate CD at the requested AOA
        cd_interp = np.interp(aoa, alphas, cds)
        return cd_interp

    def a(self, aoa, h=1e-2):  # dcl/d_alpha as a function of AOA
        cl_plus = self.Cl(aoa + h)
        cl_minus = self.Cl(aoa - h)

        dcl_dalpha = ((cl_plus - cl_minus) / (2 * h)) * np.pi / 180  # aoa is in degrees thus multiplying by this factor
        return dcl_dalpha

    def F(self, r, lamda_val):
        f = (self.b / 2) * ((1 - r / self.R) / lamda_val)
        return (2 / np.pi) * np.arccos(np.exp(-f))

    def lamda_func(self, r, F_val):
        lamda_val = np.sqrt(((self.sigma * self.a(r) / (
                16 * F_val)) - self.lamda_c / 2) ** 2 + self.sigma * self.a(r) * self.theta(r) * self.R_root / (
                                    8 * F_val * self.R)) - (
                            self.sigma * self.a(r) / (16 * F_val) - self.lamda_c / 2)

        return lamda_val

    def solve_interdependent(self, r, tol=1e-8, max_iter=100):
        lamda_val = self.lamda_c
        for i in range(max_iter):
            F_val = self.F(r, lamda_val)
            new_lamda_val = self.lamda_func(r, F_val)
            if np.abs(new_lamda_val - lamda_val) < tol:
                break  # convergence reached
            self.lamda_val = new_lamda_val
        return F_val, new_lamda_val

    # Call the function for each R_root and store the result
    def calculate_lamda_values(self):
        for r in self.r_values:
            F_val, lamda_val = self.solve_interdependent(r)
            self.lamda_values.append((r, lamda_val))  # storing lamda_val for corresponding r

    # As we have now have lamda value for each descrete r we will make a function out of this
    def lamda(self, r):
        for r_val, lamda_val in self.lamda_values:
            if r_val == r:
                return lamda_val

    def v(self, r):
        v = self.lamda(r) * self.omega * self.R - self.V
        return v

    def Ut(self, r):
        return self.omega * r

    def Up(self, r):
        return self.V + self.v(r)

    def calculate_thrust_torque_power(self):
        self.calculate_lamda_values()

        Thrust = self.b * sum((0.5 * self.density * (self.Ut(r) ** 2 + self.Up(r) ** 2) * self.chord(r) *
                               (self.Cl(self.AOA(r)) * np.cos(self.phi(r) * np.pi / 180) - self.Cd(
                                   self.AOA(r)) * np.sin(
                                   self.phi(r) * np.pi / 180))) * self.stepsize
                              for r in self.r_values)

        Torque = self.b * sum((r * 0.5 * self.density * (self.Ut(r) ** 2 + self.Up(r) ** 2) * self.chord(r) *
                               (self.Cd(self.AOA(r)) * np.cos(self.phi(r) * np.pi / 180) + self.Cl(
                                   self.AOA(r)) * np.sin(
                                   self.phi(r) * np.pi / 180))) * self.stepsize
                              for r in self.r_values)

        Power = self.omega * Torque

        return Thrust, Torque, Power

    def BEMT_Coefficient_Calculator(self, Thrust, Torque, Power):
        Ct = Thrust / (self.density * (np.pi * self.R ** 2) * (self.omega * self.R) ** 2)
        Cq = Torque / (self.density * (np.pi * self.R ** 2) * self.R * (self.omega * self.R) ** 2)
        Cp = Power / (self.density * (np.pi * self.R ** 2) * (self.omega * self.R) ** 3)
        return Ct, Cq, Cp
