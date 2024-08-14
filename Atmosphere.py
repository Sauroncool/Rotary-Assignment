import math
class Atmosphere:
    def __init__(self, altitude: float=0.0):
        self.altitude=altitude
        #Taking standard ISA conditions
        self.temperature=288.15
        self.pressure=101325
        self.density=1.225

    def calc_conditions(self, altitude:float):
        # Calculates variations in atmospheric properties with altitude
        self.altitude = altitude
        self.temperature = 288.15-0.0065*altitude
        self.pressure = 101325*(1-0.0065*altitude/288.15)**5.2561
        
