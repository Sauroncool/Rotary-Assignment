# function that returns dx_0dt & dx_1dt
# def f(x, t):
#     k = 3.6
#     m = 8.1
#     c = 0.3 * math.sqrt(4 * k * m)
#     x_0 = x[0]
#     x_1 = x[1]
#     dx_1dt = -(c / m) * x_1 - (k / m) * x_0
#     dx_0dt = x_1
#     return dx_0dt, dx_1dt
#
#
# # initial condition
# x0 = [1, 2]
#
# # time points
# t = np.arange(0, 50, 0.01)
#
# # solve ODE
# x = odeint(f, x0, t)