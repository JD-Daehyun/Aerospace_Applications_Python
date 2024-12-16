# import tkinter as tk

# hello world 
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=4, row=4)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()


# Simple User Input Display
# window = tk.Tk()
# window.title('User Form')

# tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
# tk.Label(window, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

# name_entry = tk.Entry(window)
# name_entry.grid(row=0, column=1, padx=10, pady=5)
# age_entry = tk.Entry(window)
# age_entry.grid(row=1, column=1, padx=10, pady=5)

# info_label = tk.Label(window, text="")
# info_label.grid(row=3, column=0, columnspan=2)

# def print_info():
#     info_label.config(text=f"Name: {name_entry.get()}, Age: {age_entry.get()}")

# tk.Button(window, text="Submit", command=print_info).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# window.mainloop()


# Addition Calculator 
# window = tk.Tk()
# window.title('Addition Calculator')

# number_1 = tk.Entry(window)
# number_1.grid(row = 0, column = 1, padx= 10, pady= 5)
# tk.Label(window, text= "+").grid(row = 0, column= 2, padx= 10, pady=5)
# number_2 = tk.Entry(window)
# number_2.grid(row = 0, column= 3, padx=10, pady=5)


# addition = tk.Label(window, text='')
# addition.grid(row= 2, column=1, columnspan=2)

# def print_result():
#     addition.config(text=f"Total = {int(number_1.get())+int(number_2.get())}")
# tk.Button(window, text='Submit', command=print_result).grid(row= 0, column= 4, padx=10, pady= 5)


# tk.mainloop()

# Alternative Version

# window = tk.Tk()
# window.title("Addition Calculator")

# # Add label for the calculator title
# title_label = tk.Label(window, text="Addition Calculator")
# title_label.pack(pady=10)

# # Create the main form contents 
# number1_label = tk.Label(window, text="Number 1:")
# number1_label.pack(padx=10, pady=5)
# number1_entry = tk.Entry(window)
# number1_entry.pack(padx=10, pady=5)

# number2_label = tk.Label(window, text="Number 2:")
# number2_label.pack(padx=10, pady=5)
# number2_entry = tk.Entry(window)
# number2_entry.pack(padx=10, pady=5)

# # Define the addition function
# def add_numbers():
#     result = int(number1_entry.get()) + int(number2_entry.get())
#     result_label.config(text=f"Sum: {result}")

# # Add button to perform addition
# add_button = tk.Button(window, text="Add", command=add_numbers)
# add_button.pack(pady=10)

# # Add label to display result
# result_label = tk.Label(window, text="")
# result_label.pack()

# # Display the window
# window.mainloop()


#Matplotlib Embedded
# import tkinter as tk
# from matplotlib.figure import Figure 
# from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
# NavigationToolbar2Tk) 

# window = tk.Tk()
# window.title('Line Graph using Matplotlibe and Tkinter')
# window.geometry('600x600')


# # Creating a Figure 
# fig = Figure(figsize=(5,5), dpi= 100)
# x = range(101)
# y = [i**2 for i in x]

# plot1 = fig.add_subplot(111)
# plot1.plot(x,y)

# canvas = FigureCanvasTkAgg(fig, master = window)   
# canvas.draw() 

# # placing the canvas on the Tkinter window 
# canvas.get_tk_widget().pack() 


# # Initialize Matplotlib toolbar 
# toolbar = NavigationToolbar2Tk(canvas, 
#                                window) 
# toolbar.update() 

# # Place toolbar within the window 
# canvas.get_tk_widget().pack()
# window.mainloop()


# Simulating Mathematical Models for Harmonic Oscillator
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 

# def harmonic_oscillator(state_vectors,t,omega):
#     x,v =state_vectors #position and velocity
#     dydt = [v, -omega**2*x] # These equations tell the solver how x and v change over time, enabling it to compute their values at each step.
#     return dydt

# omega = 2*np.pi
# y0 = [1.0, 0.0]
# t = np.linspace(0,10,1000)

# solution = odeint(harmonic_oscillator, y0, t, args=(omega,))

# x= solution[:,0]
# y = solution[:,1]

# window = tk.Tk() 
# window.title('Simple Harmonic Oscillator Solution') 
# # Setting the dimensions of the window to be 600px by 600px
# window.geometry("600x600") 

# fig = Figure(figsize = (8, 6), 
#                  dpi = 100) 

# # Add a subplot to the figure
# plot1 = fig.add_subplot(111)

# # Plot the line graph
# plot1.plot(t, x, label='Position (x)')
# plt.xlabel('Time')
# plt.ylabel('Position')
# plt.title('Position vs Time for Harmonic Oscillator')
# plt.legend()
# plt.grid(True)

# canvas = FigureCanvasTkAgg(fig, master = window)   
# canvas.draw() 

# # placing the canvas on the Tkinter window 
# canvas.get_tk_widget().pack() 

# toolbar = NavigationToolbar2Tk(canvas, window)
# toolbar.update()

# # Place the toolbar on the Tkinter window
# canvas.get_tk_widget().pack()


# window.mainloop()


# Example for Object in Free Fall 
# def free_fall_equation(state_vectors,t):
#     y, v = state_vectors
#     return [v, g]

# g = -9.81  # Acceleration due to gravity (m/s^2)
# t = np.linspace(0, 10, 1000)  # Time 
# y0 = [1000, 0] # initial condition

# solution = odeint(free_fall_equation, y0, t)

# y = solution[:,0]
# print(y[:10])
# v = solution[:,1]

# window = tk.Tk()
# window.title('Free Fall Object Solution')
# window.geometry('600x600')

# fig = Figure(figsize = (8, 6), dpi = 100) 

# # Add a subplot to the figure
# plot1 = fig.add_subplot(111) 

# plot1.plot(t, y, label='Vertical Position')
# plt.xlabel('Time (s)')
# plt.ylabel('Vertical Position (m)')
# plt.title('Solution to Free-Fall ODE using odeint')
# plt.legend()
# plt.grid(True)


# canvas = FigureCanvasTkAgg(fig, master=window)
# canvas.draw()

# canvas.get_tk_widget().pack()

# toolbar = NavigationToolbar2Tk(canvas, window)
# toolbar.update()

# canvas.get_tk_widget().pack()


# window.mainloop()


# Sun Valley Themed
import tkinter
from tkinter import ttk
import sv_ttk

# root = tkinter.Tk()
# label = ttk.Label(root, text='Hello World!')
# button = ttk.Button(root, text='Click Button')
# label.pack()
# button.pack()

# sv_ttk.set_theme('dark')
# root.mainloop()

# root = tkinter.Tk()
# root.title("User Form")
# root.geometry('500x300')

# sv_ttk.set_theme('dark')

# style = ttk.Style() # Create a Style Instance 

# style.configure('Margin.TLabel', padding =(0,10,0,0)) # Create a class name with custom styling 

# # Create First Name Label
# first_name_label = ttk.Label(root, text="First Name:", style='Margin.TLabel')
# first_name_label.pack()

# # Create Input for First Name
# first_name_entry = ttk.Entry(root)
# first_name_entry.pack()

# # Create Last Name Label
# last_name_label = ttk.Label(root, text="Last Name:", style='Margin.TLabel')
# last_name_label.pack()

# # Create Input for Last Name
# last_name_entry = ttk.Entry(root)
# last_name_entry.pack()

# # Create Email Label
# email_label = ttk.Label(root, text="Email:", style='Margin.TLabel')
# email_label.pack()

# # Create Input for Email
# email_entry = ttk.Entry(root)
# email_entry.pack()

# # Create a Label for Result Output
# result_label = ttk.Label(root, text="Output: ", style='Margin.TLabel')
# result_label.pack()

# def create_account():
#     # Extract input from the fields 
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     email = email_entry.get()

#     output = f"First Name: {first_name}, Last Name: {last_name}, Email: {email}" 
#     result_label.configure(text=output)

# register_button = ttk.Button(root, text="Create Account", command=create_account)
# register_button.pack()

# root.mainloop()

# Rocketship Form with Sun Valley

root = tkinter.Tk()
root.title('Rocketship Form')
root.geometry('500x300')

sv_ttk.set_theme('dark')

style = ttk.Style()
style.configure('Padding.TLabel', padding=(0,10,0,5))


name_label = ttk.Label(root, text='Rocketship Name', style='Padding.TLabel')
name_label.pack()
name_entry = ttk.Entry(root)
name_entry.pack()


destination_label = ttk.Label(root, text='Rocketship Destination', style='Padding.TLabel')
destination_label.pack()
destination_entry = ttk.Entry(root)
destination_entry.pack()

mass_label = ttk.Label(root, text='Rocketship Mass', style='Padding.TLabel')
mass_label.pack()
mass_entry = ttk.Entry(root)
mass_entry.pack()

result_label = ttk.Label(root, text="Output: ", style='Padding.TLabel')
result_label.pack()

def blast_off():
    name = name_entry.get()
    destination = destination_entry.get()
    mass = mass_entry.get()

    output = f"{name} is heading to the {destination} and weighs {mass} kg!" 
    result_label.configure(text=output)


button = ttk.Button(root, text='Blast Off', style='Padding.TLabel', command=blast_off)
button.pack()

root.mainloop()