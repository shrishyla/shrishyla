import tkinter as tk
from PIL import ImageTk , Image

#This creates the main window of an application
window = tk.Tk()
window.title("Satellite Control Center")
window.geometry("1000x800")
window.configure(background='grey')

#Imports the pictures.
pic1 = "Globeview.png"
pic2 = "MercatorView.png"
pic3 = "currentweathercroppedsmall.png"
pic4 = "GECurrentcroppedsmall.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(pic1))
img2 = ImageTk.PhotoImage(Image.open(pic2))
img3 = ImageTk.PhotoImage(Image.open(pic3))
img4 = ImageTk.PhotoImage(Image.open(pic4))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
globeview = tk.Label(window, image = img1)
mercatorview = tk.Label(window, image = img2)
currentweather= tk.Label(window, image = img3)
gearth = tk.Label(window, image = img4)

#The Pack geometry manager packs widgets in rows or columns.
globeview.pack(side = "top", fill = "both", expand = "yes")
mercatorview.pack(side = "top", fill = "both", expand = "yes")
currentweather.pack(side = "bottom", fill = "both", expand = "yes")
gearth.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()