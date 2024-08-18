#Integrates forces and moments over a complete rotor cycle
import numpy as np
from Airfoil import Airfoil
from Blade import Blade
from Inflow import Inflow
from II import Instantaneous_Integrator


class Cyclic_Integrator:
    def __init__(self, Airfoil: Cl, Cd, chord, Instantaneous_Integrator: Instantaneous_Integrator, Inflow: V, lamda_val, omega, Blade: theta, Rrc, R, sigma, A, Atmosphere: density):
        self.Instantaneous_Integrator=Instantaneous_Integrator
        self.lamda_val=lamda_val
        self.omega=omega
        self.Rrc=Rrc
        self.R=R
        self.sigma=sigma
        self.V=V
        self.blade_frequency=blade_frequency
        self.A=A
        self.Cl=Cl
        self.Cd=Cd
        r=Rrc

        self.lamda_c=V/(omega*R)
        self.lamda_values=[]
        self.r_values=np.arrange(Rrc, R, 0.1)        # 0.1 --> step-size

    def F(self, Rrc, lamda_val):
        f = (self.blade_frequency/2) * ((1-self.Rrc/self.R)/self.lamda_val)
        return (2/np.pi) * np.arccos(np.exp(-f))

    def lamda_func(self, Rrc, F_val):
        self.lamda_val=np.sqrt(((self.sigma * self.a / (16 * F_val)) - self.lamda_c / 2) ** 2 + self.sigma * self.A * self.theta * self.Rrc / (8 * F_val * self.R)) - (self.sigma * self.A / (16 * F_val) - self.lamda_c / 2)
        return lamda_val

    def solve_interdependent(self, Rrc, tol=1e-8, max_iter=100)
        self.lamda_val=self.lamda_c
        for i in range(max_iter):
            F_val = self.F(Rrc, lamda_val)
            new_lamda_val = self.lamda_func(Rrc, F_val)
            if np.abs(new_lamda_val-self.lamda_val)<tol:
                 break #convergence reached
            self.lamda_val=new_lamda_val
        return F_val, new_lamda_val


    # Call the function for each Rrc and store the result
    F_val, lamda_val = solve_interdependent(Rrc)
    lamda_values.append((Rrc, lamda_val)) # storing lamda_val for corresponding r


# As we have now have lamda value for each descrete r we will make a function out of this
def lamda(R):
    for Rrc_val, lamda_val in lamda_values:
        if Rrc_val == Rrc:
            return lamda_val


def v(self, Rrc):
    v = self.lamda(r) * self.omega * self.R - self.V
    return v


def Ut(self, Rrc):
    return self.omega * self.Rrc


def Up(self, Rrc):
    return self.V + self.v(Rrc)

def integrate_forces_and_moments(self):
    self.calculate_lamda_values()

    thrust = self.blade_frequency * sum(0.5 * self.density * (self.Ut(r) ** 2 + self.Up(r) ** 2) * self.chord *
                              (self.Airfoil.Cl * np.cos(self.Airfoil.phi) - 
                               self.Airfoil.Cd * np.sin(self.Airfoil.phi))
                              for Rrc in self.r_values)

    torque = self.b * sum(r * 0.5 * self.rho * (self.Ut(r) ** 2 + self.Up(r) ** 2) * self.chord *
                              (self.Airfoil.Cd * np.cos(self.Airfoil.phi) + 
                               self.Airfoil.Cl * np.sin(self.Airfoil.phi))
                              for Rrc in self.r_values)

    power = self.omega * torque

    return thrust, torque, power

