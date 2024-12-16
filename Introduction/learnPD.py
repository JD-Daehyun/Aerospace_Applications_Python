import pandas as pd
import numpy as np

# data = np.array([10,20,30,40])
# series = pd.Series(data)
# print('\nSeries From Numpy Array\n')
# print(series)

# planet_distances = {
#     'Mercury': 57.9,
#     'Venus': 108.2,
#     'Earth': 149.6,
#     'Mars': 227.9,
#     'Jupiter': 778.6,
#     'Saturn': 1433.5,
#     'Uranus': 2872.5,
#     'Neptune': 4495.1,
#     'Pluto': 5906.4
# }

# moon_data = {
#     'Planet': ['Jupiter', 'Jupiter', 'Saturn', 'Saturn', 'Uranus', 'Neptune'],
#     'Moon': ['Io', 'Ganymede', 'Titan', 'Rhea', 'Titania', 'Triton'],
#     'Diameter (km)': [3642, 5262, 5150, 1528, 1578, 2707],
#     'Orbital Period (days)': [1.77, 7.15, 15.95, 4.52, 8.71, 5.88]
# }

# # Create a Pandas Series representing distances of planets from the Sun (in million kilometers)

# distances = pd.Series(planet_distances)
# print('\nPlanet Distances From the Sun\n')
# print(distances)

# # Create a Pandas DataFrame representing characteristics of moons of the outer planets
# moons = pd.DataFrame(moon_data)
# print('\nCharactersitic of Moons of the Outer Planets\n')
# print(moons)

# # Average Distance From the Sun
# print('\nAverage Distance of Planets From the Sun\n')
# avg_distance = distances.mean()
# print(avg_distance)

# # Define the number of moons for each outer planet
# print('\nNumber of Moons for Each Outer Planet\n')
# outer_planets = ['Jupiter', 'Saturn', 'Uranus', 'Neptune']

# for planet in outer_planets:
#     num_moons = moons[moons['Planet'] == planet].shape[0]
#     print(f'{planet}: {num_moons}')

# # Find the largest Moon for each planet
# for planet in outer_planets:    
#     largest_moon = moons[moons['Planet'] == planet].sort_values(by='Diameter (km)', ascending=False).iloc[0]
#     print(f"{planet}: {largest_moon['Moon']}")

# Read Real Data 
space_x_missions_csv = "https://raw.githubusercontent.com/BriantOliveira/SpaceX-Dataset/master/dataset/SpaceX-Missions.csv"
launches_dataset = pd.read_csv(space_x_missions_csv)
# print(launches_dataset.head())
# print(pd.unique(launches_dataset['Customer Country']))

launches_by_country = launches_dataset.groupby('Customer Country')
# print(launches_by_country.head())

# print(launches_dataset[launches_dataset['Payload Mass (kg)']< 4000])

# print(launches_dataset[launches_dataset['Customer Country'] =='United States']['Payload Mass (kg)'].median())

launch_groups = launches_dataset.groupby("Launch Site")
print(launch_groups.head())