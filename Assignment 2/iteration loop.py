import numpy as np

# Initial values
alpha_f= 0
alpha_tpp = # something

# Fixed Quantity
GW = # something fixed

for i in range (0,100):
    Lf = # from table
    Df = # from table
    Hm = 0
    Ht = 0
    T = # some formula
    alpha_tpp = np.atan((Df+Hm+Ht)/(GW-Lf))
    
    new_alpha_f = alpha_tpp - beta_1c - i_s + v/V_inf

    if (new_alpha_f - alpha_f) < 10e-4:
        break
    alpha_f = new_alpha_f
