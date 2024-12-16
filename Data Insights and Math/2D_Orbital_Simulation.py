import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Simulating 2D Orbital Mechanics for Earth

def orbit_equations_de(state_vectors, t, G, M):
    dxdt = state_vectors[2]
    dydt = state_vectors[3]
    dvxdt = -G * M * state_vectors[0] / (np.sqrt(state_vectors[0]**2 + state_vectors[1]**2))**3
    dvydt = -G * M * state_vectors[1] / (np.sqrt(state_vectors[0]**2 + state_vectors[1]**2))**3
    return [dxdt, dydt, dvxdt, dvydt]

# initial values
y0 = [0.0, 400e3, 7800, 0.0]

# Gravitational Constant
G = 6.67430e-11

# Mass of Earth
M = 5.972e24

# timestamp 
t = np.linspace(0,10, 1000)

solution = odeint(orbit_equations_de, y0, t, args=(G,M))

# print(solution[:5, :])
plt.figure(figsize=(8,8))
plt.plot(solution[:,0], solution[:,1])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Orbit Simulation Around Earth')
plt.grid(True)
plt.axis('equal')
plt.show()