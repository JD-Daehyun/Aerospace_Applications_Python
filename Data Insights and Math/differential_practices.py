# import numpy as np 
# from scipy.integrate import odeint
# import matplotlib.pyplot as plt

# def differential_equation(y,t):
#     dydt = y**2*t + (8*t)
#     return dydt

# t = np.linspace(1,2)

# y0 = 1

# y = odeint(differential_equation, y0, t)

# plt.plot(t,y)
# plt.xlabel('Time')
# plt.ylabel('Y')
# plt.title('Visualizing dydt ODE')
# plt.show()

# Model Rocket Horizontal Motion ODE
# import numpy as np
# from scipy.integrate import solve_ivp
# import matplotlib.pyplot as plt

# # Constants
# m = 1000  # Mass of the rocket (kg)
# T = 20000  # Thrust of the rocket (N)

# v0 = 0
# state0 = [v0]
# t_span = (0, 100)


# def rocket_motion_ode(t, state):
#     v = state[0]
#     D = 500*t  # Drag force as a function of time (N)
#     a = (T - D)/m
#     return [a]


# sol = solve_ivp(rocket_motion_ode, t_span, state0, t_eval=np.linspace(t_span[0], t_span[1], 1000))

# plt.plot(sol.t, sol.y[0])
# plt.xlabel('Time(s)')
# plt.ylabel('Horizontal Velocity (m/s)')
# plt.title('Rocket Horizontal Motion')
# plt.grid(True)
# plt.show()


# Partial Differential Equation Practice 
# The Laplace Equation
import numpy as np
from pde import CartesianGrid, solve_laplace_equation

# setting up the stage
cart_grid = CartesianGrid([[0, 2 * np.pi]] * 2, 64)
boundaries = [{"value": "sin(y)"}, {"value": "sin(x)"}]


result = solve_laplace_equation(cart_grid, boundaries)
result.plot()