#Integrates forces and moments over a complete rotor cycle

from II import Instantaneous_Integrator


class Cycle_Integrator:
    def __init__(self, Instantaneous_Integrator: Instantaneous_Integrator):
