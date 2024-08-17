#Integrates the thrust, power, and torque equations for each blade. This class implements the Blade element theory.
from Blade import Blade
from Airfoil import Airfoil
from Atmosphere import Atmosphere
import math

class Instantaneous_Integrator:
    # integrates instantaneous forces and moments on individual blades
    def __init__(self, Blade: Blade, Inflow: Inflow, Airfoil: Airfoil):
        self.Blade=Blade
        self.Inflow=Inflow
        self.Airfoil=Airfoil
        
    interval=(R-Rrc)/99
    r=Rrc
    Thrust_per_blade=0
    Torque_per_blade=0
    Power_per_blade=0
    def Blade_Thrust_Calculator:
        for i in range(100):
            dTdr = 0.5*density*(Up**2+Ut**2)*chord*(Cl*math.cos(phi)-Cd*math.sin(phi)                # For Rrc
            dr = Rrc + interval*i
            dT   = dTdr * dr                                        
            Thrust_per_blade += dT
        Thrust = Thrust_per_blade * blade_frequency

    def Blade_Torque_Calulator:
        # Similarly
        for i in range(100):
            dQdr = Rrc*0.5*density*(Up**2+Ut**2)*chord*(Cl*math.cos(phi)-Cd*math.sin(phi)            # For Rrc
            dr = Rrc + interval*i
            dQ   = dQdr * dr                                        
            Torque_per_blade += dQ
        Torque = Torque_per_blade * blade_frequency

    def Blade_Power_Calulator:
        # Similarly
        for i in range(100):
            dPdr = omega*Rrc*0.5*density*(Up**2+Ut**2)*chord*(Cl*math.cos(phi)-Cd*math.sin(phi)       # For Rrc
            dr = Rrc + interval*i
            dP   = dPdr * dr                                        
            Power_per_blade += dP
        Power = Power_per_blade * blade_frequency

    # Calculating thrust, torque, and power coefficients
    def BET_Coefficient_Calculator:
        Ct = Thrust/(density*A*(omega*R)**2)
        Cq = Torque/(density*A*R(omega*R)**2)
        Cp = Power/(density*A(omega*R)**3)
