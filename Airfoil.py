def read_polar_data(file_path = 'NACA0015.txt'):
    """
    Reads the polar data from a file and stores AOA, CL, and CD in a list of dictionaries.

    :param file_path: Path to the file containing polar data.
    :return: List of dictionaries with each dictionary containing 'aoa', 'cl', and 'cd'.
    """
    data_list = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Skip lines until we reach the header of the data table
        for i, line in enumerate(lines):
            if line.strip().startswith('alpha'):
                start_index = i + 1
                break

        # Iterate through the data lines and store AOA, CL, CD
        for line in lines[start_index:]:
            data = line.split()
            if len(data) < 3:  # Ensure the line contains sufficient data
                continue

            try:
                alpha = float(data[0])
                cl = float(data[1])
                cd = float(data[2])

                data_list.append({'aoa': alpha, 'cl': cl, 'cd': cd})

            except ValueError:
                continue  # If conversion fails, skip this line

    return data_list

# Example usage:
file_path = 'NACA0012.txt'
polar_data = read_polar_data(file_path)
        

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
