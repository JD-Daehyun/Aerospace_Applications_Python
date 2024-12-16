
import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1d)

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(arr2d)


gravity_acceleration = 9.81  # Constant acceleration due to gravity in m/s^2

# Generate a NumPy array representing time in seconds from t=0 to t=100 seconds with a step size of 1 second.
time = np.arange(0,101,1)
# Generate a NumPy array representing altitude in meters during the launch phase. The altitude should start at 0 meters and increase linearly with time at a constant rate of 100 meters per second.
altitude = time * 100

# Calculate the velocity array using the altitude array. Assume constant acceleration due to gravity (9.81 m/s^2) during the launch phase.
velocity = time * gravity_acceleration 

# Calculate the acceleration array using a constant acceleration value of 9.81 m/s^2.
acceleration = np.full(time.shape, gravity_acceleration)

# Print the shape and data type of each generated NumPy array
print('Shape of time array: ', time.shape)
print('Data Type of time array: ', time.dtype)

print('Shape of altitude array: ', altitude.shape)
print('Data Type of altitude array: ', altitude.dtype)

print('Shape of velocity array: ', velocity.shape)
print('Data Type of velocity array: ', velocity.dtype)

print('Shape of acceleration array: ', acceleration.shape)
print('Data Type of acceleration array: ', acceleration.dtype)



# Mission Profiling
rand_altitude = np.random.uniform(0, 10000, size = 1000)
rand_velocity = np.random.uniform(0, 400, size = 1000)
rand_acceleration = np.random.uniform(-20, 20, size = 1000)

critical_altitude = rand_altitude[rand_altitude>5000]
critical_velocity = rand_velocity[rand_velocity>300]
critical_acceleration = rand_acceleration[rand_acceleration<-9.81]

flight_profile = np.concatenate((critical_altitude, critical_velocity, critical_acceleration))

print("Flight Profile\n")
print(flight_profile)
