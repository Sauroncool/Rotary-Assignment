import math
#MK this is correct, note altitude is in metres
class Atmosphere:
    def __init__(self, altitude: float=0.0):
        self.altitude=altitude
        #Taking standard ISA conditions
        self.temperature=288.15
        self.pressure=101325
        self.density=1.225

    def calc_conditions(altitude:float):
        # Calculates variations in atmospheric properties with altitude
        altitude = altitude
        temperature = 288.15-0.0065*altitude
        pressure = 101325*(1-0.0065*altitude/288.15)**5.2561
        density = 1.225*(1-0.0065*altitude/288.15)**4.2561
        return temperature, pressure, density
        
