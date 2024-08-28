import numpy as np
import math
from CI import CI
#MK this is to be updated as airfoil = airfoil (alpha, cl_data, cd_data, cm_data), typically at each 0.5deg

class Airfoil:
    def __init__(self, CI: AOA):
        self.AOA=AOA
        self.Cl=Cl
        self.Cd=Cd
        Cl=2*math.pi*AOA
        Cd=0.35
        return Cl, Cd
        

# DO NOT TOUCH, INITIAL SET OF DATA FOR THE FIRST ITERATION
# 
#  class Airfoil:
#     def _init_(self, cl_data: dict, cd_data: dict, cm_data: dict):
#         self.cl_data = cl_data
#         self.cd_data = cd_data
#         self.cm_data = cm_data

#     cl_data = {'alpha': [0, 5, 10, 15], 'Cl': [0.0, 0.5, 1.0, 0.8]}
#     cd_data = {'alpha': [0, 5, 10, 15], 'Cd': [0.01, 0.015, 0.02, 0.025]}
#     cm_data = {'alpha': [0, 5, 10, 15], 'Cm': [0.0, -0.02, -0.04, -0.03]}

#     def get_cl(self, AOA: float):
#         return np.interp(AOA, self.cl_data['alpha'], self.cl_data['Cl'])
    
#     def get_cd(self, AOA: float):
#         return np.interp(AOA, self.cd_data['alpha'], self.cd_data['Cd'])

#     def get_cm(self, AOA: float):
#         return np.interp(AOA, self.cm_data['alpha'], self.cm_data['Cd'])



# Addition of Some code to fetch airfoil data. Fetch cl, cd and cm of an airfoil
# say sample data is # Sample data
