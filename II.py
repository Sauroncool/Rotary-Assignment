from Blade import Blade
from Airfoil import Airfoil

class Instantaneous_Integrator:
    # integrates instantaneous forces and moments on individual blades
    def __init__(self, blade_geometry: BladeGeometry, inflow: Inflow, airfoil: Airfoil):
        