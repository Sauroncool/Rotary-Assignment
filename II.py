#Integrates the thrust, power, and torque equations for each blade. This class implements the Blade element theory.
from Blade import Blade
from Airfoil import Airfoil
from Atmosphere import Atmosphere
from Inflow import Inflow
import math

class Instantaneous_Integrator:
    # integrates instantaneous forces and moments on individual blades
    def __init__(self, Blade: Blade, blade_frequency, R, Rrc, Inflow: Inflow, omega, Airfoil: Airfoil, Atmosphere: density):
        self.Blade=Blade
        self.Inflow=Inflow
        self.Airfoil=Airfoil
        self.density=density
        self.R=R
        self.Rrc=Rrc
        self.omega=omega
        self.blade_frequency=blade_frequency
        
        self.interval=(R-Rrc)/99
        self.Thrust_per_blade=0
        self.Torque_per_blade=0
        self.Power_per_blade=0
        
    def Blade_Thrust_Calculator(self):
        for i in range(100):
            dTdr = 0.5*self.density*(self.Blade.Up**2+self.Blade.Ut**2)*self.Airfoil.chord*(self.Airfoil.Cl*math.cos(self.Airfoil.phi)-self.Airfoil.Cd*math.sin(self.Airfoil.phi)  )              # For Rrc
            dr = self.Rrc + self.interval*i
            dT   = dTdr * dr                                        
            self.Thrust_per_blade += dT
        Thrust = self.Thrust_per_blade * self.blade_frequency
        return Thrust

    def Blade_Torque_Calculator(self):
        # Similarly
        for i in range(100):
            dQdr = self.Rrc*0.5*self.density*(self.Blade.Up**2+self.Blade.Ut**2)*self.Airfoil.chord*(self.Airfoil.Cl*math.cos(self.Airfoil.phi)-self.Airfoil.Cd*math.sin(self.Airfoil.phi)   )         # For Rrc
            dr = self.Rrc + self.interval*i
            dQ   = dQdr * dr                                        
            self.Torque_per_blade += dQ
        Torque = self.Torque_per_blade * self.blade_frequency
        return Torque

    def Blade_Power_Calculator(self):
        # Similarly
        for i in range(100):
            dPdr = self.omega*self.Rrc*0.5*self.density*(self.Blade.Up**2+self.Blade.Ut**2)*self.Airfoil.chord*(self.Airfoil.Cl*math.cos(self.Airfoil.phi)-self.Airfoil.Cd*math.sin(self.Airfoil.phi)  )     # For Rrc
            dr = self.Rrc + self.interval*i
            dP   = dPdr * dr                                        
            self.Power_per_blade += dP
        Power = self.Power_per_blade * self.blade_frequency
        return Power

    # Calculating thrust, torque, and power coefficients
    def BET_Coefficient_Calculator(self, Thrust, Torque, Power, A):
        Ct = Thrust/(self.density*A*(self.omega*self.R)**2)
        Cq = Torque/(self.density*A*self.R*(self.omega*self.R)**2)
        Cp = Power/(self.density*A*(self.omega*self.R)**3)
        return Ct, Cq, Cp
