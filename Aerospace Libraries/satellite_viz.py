# Project: Satellite Tracker
## Create a Python program to create two visualizations for satellite tracking
## Use online data sources like Celestrak to gather TLE data
## Create a 2D visualization of a satellite's ground track
## Create a polar coordinate plot of the satellite
## Utilize libraries such as skyfield, numpy, and matplotlib


import ephem
import matplotlib.pyplot as plt
from datetime import datetime
from skyfield.api import utc, load, Topos

# Instead of returning the raw TLE data as a string, it parses and processes the TLE to create an object that contains:
# Metadata, like the satellite name and catalog number.
# Useful orbital parameters derived from the TLE, such as the epoch.
station_data = load.tle('https://celestrak.com/NORAD/elements/stations.txt')
iss = station_data['ISS (ZARYA)']
print(iss)

# Set the time range
time_scale = load.timescale()
minutes = range(60 * 2)
time_range = time_scale.utc(2024, 12, 6, 15, minutes)


altitudes = []
azimuths = []

for t in time_range:
    # Calculate satellite position at each time step
    ventura = Topos(latitude='34.2746 N', longitude='119.2290 W')
    orbit = (iss - ventura).at(t)
    altitude, azimuth, distance = orbit.altaz()
    
    # Append the altitude and azimuth values to the lists
    altitudes.append(altitude.degrees)
    azimuths.append(azimuth.degrees)


plt.figure(figsize=(10, 5))
plt.plot(azimuths, altitudes, marker='o', linestyle='-')
plt.title("Satellite Path - ISS")
plt.xlabel("Azimuth (degrees)")
plt.ylabel("Altitude (degrees)")
plt.grid(True)
plt.show()