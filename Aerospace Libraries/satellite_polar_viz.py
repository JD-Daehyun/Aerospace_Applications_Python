from skyfield import api
from pytz import timezone
import numpy as np
import matplotlib.pyplot as plt
time_zone = timezone('US/Pacific')

station_data = api.load.tle('https://celestrak.com/NORAD/elements/stations.txt')
iss = station_data['ISS (ZARYA)']
print(iss)

# rather than 2 hours, it is in two days
minutes = range(60 * 24 * 2)
time_scale = api.load.timescale()

time_range = time_scale.utc(2024, 12, 6, 15, minutes)


# Very similar to the previous project but without looping 
ventura = api.Topos(latitude='34.2746 N', longitude='119.2290 W')
orbit = (iss - ventura).at(time_range)
altitude, azimuth, distance = orbit.altaz()

print(f"Altitudes: {altitude}")
print(f"Azimuth: {azimuth}")
print(f"Distance: {distance}")

# Check whether the satellite is visible through altitude > 0 
visible_pass = altitude.degrees > 0 # Creates a boolean array where each element corresponds to whether the satellite is visible at a given time.
indicies, = visible_pass.nonzero() # Returns the indices of True values in visible_pass
boundaries, = np.diff(visible_pass).nonzero() # Computes the difference between consecutive elements in visible_pass.
# Transition types:
# True -> False results in -1 (satellite goes below the horizon).
# False -> True results in 1 (satellite rises above the horizon).
# nonzero(): Returns the indices where these transitions occur.

# print(boundaries) 
boundaries = boundaries
passes = boundaries.reshape(len(boundaries) // 2, 2) # create pairs [when the sat becomes visible, when the sat becomes invisible]
# print(passes)

# Side not to undestand the time of the passes in my time zone
pass_to_observe = 0
specific_pass = passes[pass_to_observe]
rise, set = specific_pass
print(f'ISS Rises at {time_range[0].astimezone(time_zone)}')
print(f'ISS Sets at {time_range[1].astimezone(time_zone)}')


# Visualizing the Polar Plot 
ax = plt.subplot(111, projection='polar')
plt.title("ISS Pass Polar Chart")
ax.set_rlim([0, 100])
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)


θ = azimuth.radians
r = 90 - altitude.degrees
ax.plot(θ[rise:set], r[rise:set], 'bo--')

for k in range(rise, set):
    text = time_range[k].astimezone(time_zone).strftime('%H:%M')
    ax.text(θ[k], r[k], text, ha='right', va='bottom')


plt.show()