import matplotlib.pyplot as plt
import numpy as np
import math 
from mpl_toolkits.mplot3d import Axes3D
# # Sample dataset (time points and brightness measurements)
# time_points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Time points
# brightness = [10, 30, 80, 140, 120, 100, 80, 60, 30, 10]  # Brightness measurements

# plt.plot(time_points, brightness, color ='purple', linestyle ='--', marker ='o', markersize=5)
# plt.xlabel('Time')
# plt.ylabel('Brightness')
# plt.title('Brightness of Supernova')

# x = np.linspace(0, 2*math.pi, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Plot of sin(x)')
# plt.grid(True)
# plt.show()

# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# X = np.linspace(-5, 5, 100)
# Y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(X, Y)
# Z = np.sin(np.sqrt(X**2 + Y**2))

# ax.plot_surface(X, Y, Z, cmap='viridis')

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('3D Surface Plot of sin(sqrt(X^2 + Y^2))')

# plt.show()


x = np.linspace(0, 2*math.pi, 50)
y = np.tan(x)
y2 = np.cos(x)
plt.plot(x,y, color='red', label='tan', linestyle='--', marker='o', markersize=5)
plt.plot(x,y2, color='blue', label='cos', linestyle='--', marker='o', markersize=5)
plt.grid(True)

plt.show()