import numpy as np
#MK this is to be updated as airfoil = airfoil (alpha, cl_data, cd_data, cm_data), typically at each 0.5deg

class Airfoil:
    def _init_(self, cl_data: dict, cd_data: dict, cm_data: dict):
        self.cl_data = cl_data
        self.cd_data = cd_data
        self.cm_data = cm_data

# Addition of Some code to fetch airfoil data. Fetch cl, cd and cm of an airfoil
# say sample data is # Sample data
# cl_data = {'alpha': [0, 5, 10, 15], 'cl': [0.0, 0.5, 1.0, 0.8]}
# cd_data = {'alpha': [0, 5, 10, 15], 'cd': [0.01, 0.015, 0.02, 0.025]}
# cm_data = {'alpha': [0, 5, 10, 15], 'cm': [0.0, -0.02, -0.04, -0.03]}

    def get_cl(self, aoa: float):
        return np.interp(aoa, self.cl_data['alpha'], self.cl_data['cl'])
    
    def get_cd(self, aoa: float):
        return np.interp(aoa, self.cd_data['alpha'], self.cd_data['cd'])

    def get_cm(self, aoa: float):
        return np.interp(aoa, self.cm_data['alpha'], self.cm_data['cd'])
