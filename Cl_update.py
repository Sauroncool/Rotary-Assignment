# Integrates forces and moments over a complete rotor cycle. Implements the BE Momentum Theory by definition.
import numpy as np
from Airfoil import Airfoil
from Blade import *
from Inflow import *


# from II import Instantaneous_Integrator


class Cyclic_Integrator:
    def __init__(self, theta=3 * np.pi / 180, phi=0.1, sigma=0.1, a=0.1,
                 density=1.225,
                 chord=0.5):
        # Use default parameters if no inflow instance is provided
        self.V = vehicle_velocity
        self.theta = theta
        self.phi = phi  # taninv(lamda)
        self.omega = MR_omega
        self.R_root = MR_root_cutout
        self.R = MR_radius
        self.sigma = sigma
        self.b = MR_nu_blades
        self.a = a  # Dcl/D_alpha
        self.density = density
        self.chord = chord
        # r = R_root

        self.lamda_c = self.V / (self.omega * self.R)
        self.lamda_values = []
        self.stepsize = 0.1
        self.r_values = np.arange(self.R_root, self.R, self.stepsize)

    def Cl(self, r):
        airfoil = Airfoil()  # Create an instance of the Airfoil class
        #AOA = airfoil.AOA(r)
        Cl, Cd = airfoil.get_coeff(r)
        return Cl

    def Cd(self, r):
        airfoil = Airfoil()  # Create an instance of the Airfoil class
        # AOA = airfoil.AOA(r)
        Cl, Cd = airfoil.get_coeff(r)
        return Cd

    def F(self, r, lamda_val):
        f = (self.b / 2) * ((1 - r / self.R) / lamda_val)
        return (2 / np.pi) * np.arccos(np.exp(-f))

    def lamda_func(self, r, F_val):
        lamda_val = np.sqrt(((self.sigma * self.a / (
                16 * F_val)) - self.lamda_c / 2) ** 2 + self.sigma * self.a * self.theta * self.R_root / (
                                    8 * F_val * self.R)) - (
                            self.sigma * self.a / (16 * F_val) - self.lamda_c / 2)
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

        Thrust = self.b * sum((0.5 * self.density * (self.Ut(r) ** 2 + self.Up(r) ** 2) * self.chord *
                              (self.Cl(r) * np.cos(self.phi) - self.Cd(r) * np.sin(self.phi)))*self.stepsize
                              for r in self.r_values)

        Torque = self.b * sum((r * 0.5 * self.density * (self.Ut(r) ** 2 + self.Up(r) ** 2) * self.chord *
                              (self.Cd(r) * np.cos(self.phi) + self.Cl(r) * np.sin(self.phi)))*self.stepsize
                              for r in self.r_values)

        Power = self.omega * Torque

        return Thrust, Torque, Power

        return Thrust, Torque, Power

    def BEMT_Coefficient_Calculator(self, Thrust, Torque, Power, A):
        Ct = Thrust / (self.density * A * (self.omega * self.R) ** 2)
        Cq = Torque / (self.density * A * self.R * (self.omega * self.R) ** 2)
        Cp = Power / (self.density * A * (self.omega * self.R) ** 3)
        return Ct, Cq, Cp
