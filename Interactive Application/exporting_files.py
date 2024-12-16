import csv
import json
import tkinter
from tkinter import ttk
import sv_ttk


telemetry = [
    {
        "timestamp": "2024-03-30T07:58:27.999065",
        "temperature": 24.15,
        "pressure": 1082.28,
        "velocity": 2157.35,
        "altitude": 579.64,
        "power_level": 68.97,
        "orientation": {
            "roll": 63.34,
            "pitch": -174.83,
            "yaw": 220.57
        }
    },
    {
        "timestamp": "2024-03-30T07:47:56.999065",
        "temperature": -35.17,
        "pressure": 892.84,
        "velocity": 9366.16,
        "altitude": 821.66,
        "power_level": 25.56,
        "orientation": {
            "roll": -48.75,
            "pitch": -167.37,
            "yaw": 181.04
        }
    },
    {
        "timestamp": "2024-03-30T07:53:45.999065",
        "temperature": -5.28,
        "pressure": 1028.31,
        "velocity": 6538.57,
        "altitude": 729.16,
        "power_level": 88.36,
        "orientation": {
            "roll": 160.25,
            "pitch": 101.33,
            "yaw": 16.67
        }
    }
]


with open('telemetry.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=telemetry[0].keys())
    writer.writeheader()
    writer.writerows(telemetry)


with open('telemetry.json', 'w') as file: 
    json.dump(telemetry, file)


rockets = [
    {
        'Name': 'Atlas V',
        'Operator': 'United Launch Alliance'
    },
    {
        'Name': 'Delta IV',
        'Operator': 'United Launch Alliance'
    }
]

root = tkinter.Tk()
root.title('Download Json File')
root.geometry('600x600')

sv_ttk.set_theme('light')

def download_csv_file():
    with open('rocket.json', 'w') as file:
        json.dump(rockets, file)

button = ttk.Button(root, text='Download JSON File', command=download_csv_file)
button.pack()


root.mainloop()