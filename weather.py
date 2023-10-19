from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city = textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)

# icon
image_icon = PhotoImage(file="./Assets/images/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="./Assets/images/Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=115)

# label
label1 = Label(root, text="Temperature", font=(
    'Poppins', 9), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=(
    'Poppins', 9), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=(
    'Poppins', 9), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=(
    'Poppins', 9), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=(
    'Poppins', 9), fg="white", bg="#203243")
label5.place(x=50, y=200)

# search box
Search_image = PhotoImage(file="./Assets/images/Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file='./Assets/images/Layer 7.png')
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=290, y=127)

textfield = tk.Entry(root, justify='center', width=15, font=(
    'Poppins', 20, 'bold'), bg="#203243", border=0, fg='white')
textfield.place(x=355, y=127)
textfield.focus()

Search_icon = PhotoImage(file="./Assets/images/Layer 6.png")
myimage_icon = Button(image=Search_icon, borderwidth=0,
                      cursor="hand2", bg="#203243",command=getWeather)
myimage_icon.place(x=645, y=125)


# Bottom Box
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# bottom boxes
firstbox = PhotoImage(file="./Assets/images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="./Assets/images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

# clock
clock = Label(root, font=("Poppins", 25, "bold"), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# timezone
timezone = Label(root, font=("Poppins", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Poppins", 15), fg="white", bg="#57adff")
long_lat.place(x=700, y=20)

root.mainloop()
