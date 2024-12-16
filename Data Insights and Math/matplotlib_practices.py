# import json
# import matplotlib.pyplot as plt


# Plotting Aircraft Telemetry using MatplotLib
# with open("Data Insights and Math/test_adsb_dataset.json", "r") as f:
#     data = json.load(f)['trace']

# # Filter out ones that has flight logs 
# filtered_data = []
# for aircraft in data:
#     if aircraft[8] != None:
#         filtered_data.append(aircraft)

# # True air speed
# airspeeds = []
# for entry in filtered_data:
#     if 'tas' in entry[8]:
#         airspeeds.append(entry[8]['tas'])

# plt.plot(airspeeds)
# plt.xlabel('Data Point Index')
# plt.ylabel('Airspeed (knots)')
# plt.title('Aircraft Airspeed')
# plt.grid(True)
# plt.show()


# Plotting Spacecraft Thurster Telemtry using MatplotLib
# import csv
# from datetime import datetime

# thrust_values = []
# time_values = []

# with open("Data Insights and Math/spacecraft_thruster.csv", "r") as f:
#     reader = csv.reader(f)
#     next(reader) #skips the header row
#     for row in reader:
#         thrust_values.append(float(row[2]))
#         date_obj = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f') # converts it so that python can understand the datetime object
#         time_values.append(date_obj)


# plt.plot(time_values, thrust_values)
# plt.xlabel('Time')
# plt.ylabel('Thrust')
# plt.title('Spacecraft Thrust over Time')
# plt.grid(True)
# plt.show()

# Plotting Black Body Radiation Using Astropy 
import numpy as np 
import matplotlib.pyplot as plt
from astropy.modeling.models import BlackBody
from astropy import units as u
from astropy.visualization import quantity_support

black_body = BlackBody(temperature = 3000*u.K)
wavelengths = np.arange(2000, 200000) * u.AA 
flux = black_body(wavelengths)

with quantity_support():
    plt.figure()
    plt.semilogx(wavelengths, flux)
    plt.axvline(black_body.nu_max.to(u.AA, equivalencies=u.spectral()).value, ls='--')
    plt.show()