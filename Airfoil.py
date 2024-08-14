import numpy as np
class Airfoil:
    def _init_(self, cl_data: dict, cd_data: dict, cm_data: dict):
        self.cl_data = cl_data
        self.cd_data = cd_data

# Addition of Some code to fetch airfoil data

    # def get_cl(self, aoa: float):
    #     return np.interp(aoa, self.cl_data['alpha'], self.cl_data['cl'])
    
    # def get_cd(self, aoa: float):
    #     return np.interp(aoa, self.cd_data['alpha'], self.cd_data['cd'])
