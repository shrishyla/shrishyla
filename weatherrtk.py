import tkinter as tk
from tkinter import *
from weather import Weather,Unit

win=tk.Tk()

weather = Weather(unit=Unit.CELSIUS)
z=input("enter location")
location=weather.lookup_by_location(z)
condition=location.condition
label=Label(text=condition.text)
label.pack()

win.mainloop()