class Inflow:
  # Calculates the induced, vehicle, and wind velocities for each blade section
  def __init__(self, vehicle_velocity=5, wind_velocity=0):
    self.vehicle_velocity = vehicle_velocity
    self.wind_velocity = wind_velocity


# Define the inflow conditions here
inflow_conditions = Inflow(vehicle_velocity=5, wind_velocity=0)

