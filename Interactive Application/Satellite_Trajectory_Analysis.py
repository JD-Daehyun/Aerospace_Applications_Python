import tkinter 
from tkinter import ttk
import sv_ttk
import csv
import numpy as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sgp4.api import Satrec
from sgp4.api import jday

# Create window
root = tkinter.Tk()
root.title('Satellite Trajectory Analysis')
root.geometry('1200x900')


# Configure Styling
sv_ttk.set_theme('dark')
plt.style.use('dark_background')


style = ttk.Style()
# Reminder that this styling is for that particular widget's padding not the margin 
style.configure('Margin.TLabel', padding =(0,20,0,5))  # (left, top, right, bottom) => Clockwise
style.configure('Custom.TButton', padding=(20,10), background='#222222', foreground='#ffffff')




# Create Side-by-Side Frame
 # Create frames
left_frame = tkinter.Frame(root, width=500, height=600)
right_frame = tkinter.Frame(root, width=300, height=600)

# Pack frames side by side
left_frame.pack(side="left", fill="both", expand=True)
right_frame.pack(side="left", fill="both", expand=True) # Place right next to the left frame

# 6 Sliders for Keplarian  Elements 
semi_major_axis_label = ttk.Label(right_frame, text='Semi-Major Axis: ', style='Margin.TLabel')
semi_major_axis_label.pack()
semi_major_axis_slider = tkinter.Scale(right_frame, from_=2000, to=50000, tickinterval=10000, orient=tkinter.HORIZONTAL, length=400)
semi_major_axis_slider.pack()

eccentricity_label = ttk.Label(right_frame, text="Eccentricity: ", style='Margin.TLabel')
eccentricity_label.pack()
eccentricity_slider = tkinter.Scale(right_frame, from_=0, to=1, resolution=0.01, tickinterval=0.1, orient=tkinter.HORIZONTAL, length=400)
eccentricity_slider.pack()

inclination_label = ttk.Label(right_frame, text="Inclination: ", style='Margin.TLabel')
inclination_label.pack()
inclination_slider = tkinter.Scale(right_frame, from_=0, to=360, tickinterval=40, orient=tkinter.HORIZONTAL, length=400)
inclination_slider.pack()

right_ascension_label = ttk.Label(right_frame, text='RAAN', style='Margin.TLabel')
right_ascension_label.pack()
right_ascension_slider = tkinter.Scale(right_frame, from_=0, to=360, tickinterval=40, orient=tkinter.HORIZONTAL, length=400)
right_ascension_slider.pack()

argument_of_perigee_label = ttk.Label(right_frame, text='Argument of Perigee', style='Margin.TLabel')
argument_of_perigee_label.pack()
argument_of_perigee_slider = tkinter.Scale(right_frame, from_=1, to=360, tickinterval=40, orient=tkinter.HORIZONTAL, length=400)
argument_of_perigee_slider.pack()

mean_anomaly_label = ttk.Label(right_frame, text="Mean Anomaly", style='Margin.TLabel')
mean_anomaly_label.pack()
mean_anomaly_slider = tkinter.Scale(right_frame, from_=1, to=360, tickinterval=40, orient=tkinter.HORIZONTAL, length=400)
mean_anomaly_slider.pack()

def display_sliders(a, e, i, o, w, v):
    semi_major_axis_slider.set(a)
    eccentricity_slider.set(e)
    inclination_slider.set(i)
    right_ascension_slider.set(o)
    argument_of_perigee_slider.set(w)
    mean_anomaly_slider.set(v)


# Default Settings

# Semi-Major Axis: 10000
# Eccentricity: 0.1
# Inclination: 90
# RAAN: 40
# Argument of Periapsis: 1
# Mean Anamoly: 1
display_sliders(10000, 0.1, 90, 40, 1, 1)


# Plot Altitude vs time using SGP4 propagation in respect to the surface of the Earth
def trace_altitude_graph(tle_one, tle_two):
    satellite = Satrec.twoline2rv(tle_one, tle_two)

    # Define the time range
    start_time = 0
    end_time = 24 * 3600 # one day
    step = 60 # Every minute
    times = np.arange(start_time, end_time, step)

    # Calculate the altitude at each time step
    altitudes = []
    for t in times:
        jd, fr = jday(2024,12,13,0,0,t) #Julian date and fraction of a day
        e,r,v = satellite.sgp4(jd,fr)
        altitude = (r[0]**2 + r[1]**2 + r[2]**2)**0.5 - 6378.135 # this number is Earth's mean radius
        altitudes.append(altitude)

    # Initialize a figure and add it within a canvas
    fig = Figure(figsize=(6,4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=left_frame)
    canvas.get_tk_widget().pack(pady=15)

    plot = fig.add_subplot(111)
    plot.plot(times, altitudes)
    plot.set_xlabel('Time(s)')
    plot.set_ylabel('Altitude (km)')
    plot.set_title('ISS Altitude Plot')
    plot.grid(True)


    canvas.draw()


# Default TLE: ISS
# 1 25544U 98067A   21257.91276829  .00000825  00000-0  24323-4 0  9990
# 2 25544  51.6461  89.6503 0003031 120.4862 259.0942 15.4888108230711
trace_altitude_graph("1 25544U 98067A   21257.91276829  .00000825  00000-0  24323-4 0  9990", "2 25544  51.6461  89.6503 0003031 120.4862 259.0942 15.48881082307117")

# Plotting an 3D Orbit using pysal library
fig2 = Figure(figsize=(6,3), dpi=100)
canvas2 = FigureCanvasTkAgg(fig2, master=left_frame)

def visualize_3d_orbit(a,p,e,o,i,w,fig_vis):
    # Find the x,y,z at each timestamp
    orbit = pyasl.KeplerEllipse(a=a, per=p, e=e, Omega=o, i=i, w=w)
    t = np.linspace(0, 4, 300)
    pos = orbit.xyzPos(t)
    # print(pos[:5, ::])
    # If there is a figure, clear it
    if fig_vis:
        fig_vis.clear()
    
    canvas2.get_tk_widget().pack(pady=15)
    plot2 = fig_vis.add_subplot(111, projection='3d')
    # Plots the Earth, trajectory path, and periapsis point of trajectory
    plot2.plot(0, 0, 'bo', markersize=9, label="Earth")
    plot2.plot(pos[::, 0], pos[::, 1], 'k-', label="Satellite Trajectory")
    plot2.plot(pos[0, 0], pos[0, 1], 'g*', label="Periapsis")

    canvas2.draw()


#Default Setting 
visualize_3d_orbit(1.0, 1.0, 0.5, 0.0, 30.0, 0.0, fig2)


# Create a Retrace Orbit Button
def retrace_orbit(): 
    a = semi_major_axis_slider.get()
    p = mean_anomaly_slider.get()
    e = eccentricity_slider.get()
    o = right_ascension_slider.get()
    i = inclination_slider.get()
    w = argument_of_perigee_slider.get()

    visualize_3d_orbit(a,p,e,o,i,w,fig2)


retrace_orbit = ttk.Button(left_frame, text='Retrace Orbit', command=retrace_orbit, style='Custom.TButton')
retrace_orbit.pack(pady=10)

# Download CSV Button 
def download_csv():
    with open('satellite_orbit_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["A", "E", "I", "O", "W", "V"])
        writer.writeheader()
        writer.writerow({
            "A": semi_major_axis_slider.get(), 
            "E": eccentricity_slider.get(), 
            "I": inclination_slider.get(), 
            "O": right_ascension_slider.get(), 
            "W": argument_of_perigee_slider.get(), 
            "V": mean_anomaly_slider.get()  
        })



download_button = ttk.Button(left_frame, text='Download CSV', command=download_csv, style='Custom.TButton')
download_button.pack()


root.mainloop()
    