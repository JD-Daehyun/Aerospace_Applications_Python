import tkinter 
from tkinter import ttk
import sv_ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import csv


root = tkinter.Tk()
root.title('Line Graph Export')
root.geometry('600x600')


sv_ttk.set_theme('light')

# Create a slider
slope_slider = tkinter.Scale(root, from_=1, to=10, tickinterval=1, orient=tkinter.HORIZONTAL, length=400)
slope_slider.set(1)
slope_slider.pack()

fig =Figure(figsize=(8,6), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)

style = ttk.Style()
style.configure('Padding.TLabel', padding=(0,10,0,5))

def create_plot(canvas, fig):
    if fig:
        fig.clear()
    m = int(slope_slider.get())
    x = np.linspace(0,10,100)
    y = m * x 
    plot = fig.add_subplot(111)
    plot.plot(x,y)
    canvas.draw()
    

create_button = ttk.Button(root, text='Create Graph', command=lambda: create_plot(canvas, fig), style= 'Padding.TLabel')
create_button.pack()


def download_data():
    m = int(slope_slider.get())
    x = np.linspace(0, 10, 100)

    with open('slope.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['x', 'y'])
        writer.writeheader()
        for i in range(len(x)):
           y = m * x[i] 
           writer.writerow({'x': x[i], 'y': y})
    file.close()

download_button = ttk.Button(root, text='Download CSV File', command=download_data, style='Padding.TLabel')
download_button.pack()

canvas.get_tk_widget().pack() # pack entire widgets onto the window
create_plot(canvas, fig) #call the function to make sure there is a graph when we first open the window

root.mainloop()



