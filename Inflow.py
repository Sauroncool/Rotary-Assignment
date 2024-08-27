class Inflow:
  #calculates the induced, vehicle and wind velocities for each blade section
  def __init__(self, vehicle_velocity, wind_velocity):
    self.vehicle_velocity = [0,5,0]
    self.wind_velocity = [0,0,0]
    
