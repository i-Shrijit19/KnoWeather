from tkinter import *
from customtkinter import *
from tkinter import messagebox
import requests as req
from PIL import Image, ImageTk

#functional part

def search():
    cityname= city.get()
    update= get_update(cityname)
    if update is NONE:
        return NONE
    else:
        # If the city is found, unpack the weather information
        icon_id, temperature_data, city_name, country_name, description_data= update

        #configure the location
        location.configure(text=f"{city_name}, {country_name}")

        # Update the temperature and description labels
        temperature.configure(text=f"Temperature: {temperature_data}°C")
        description.configure(text=f"Description: {description_data}")


def get_update(city):
    api= "f90095bccbd3cbf778645bbea098ded2"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
    response= req.get(url).json()

    icon_id= response['weather'][0]['icon']
    temperature_data= int(response['main']['temp']- 273.15)
    city_name= response['name']
    country_name = response['sys']['country']
    description_data=response['weather'][0]['description']

    return (icon_id, temperature_data, city_name, country_name, description_data)


#base of root
    
set_appearance_mode("dark")
set_default_color_theme("green")
root= CTk()
root.geometry("400x500")
root.maxsize(400, 500)
root.minsize(400, 500)
root.title("KnoWeather")

#Upper Portion

img= Image.open("C:\\Users\\91905\\Code\\Pinnacle Weather Forecast\\pinlogo.png")
showimage= ImageTk.PhotoImage(img)

f1= Frame(root, width=400, height=80, background="black")

logo= Label(image=showimage, width=100, height=93, background="black")
logo.pack(side=LEFT, anchor="nw", pady=0)

title= Label(f1, background="black", fg="lime", text="KnowWeather", font="Georgia 20 bold")
title.pack(side=RIGHT, pady=30, padx=20)

extra= Label(f1, background="black", width=200)
extra.pack(pady=36)

f1.pack()


#main body
searchframe= CTkFrame(root, width=400, fg_color="transparent")

city= StringVar()

searchbar= CTkEntry(searchframe, textvariable=city, corner_radius=5)
searchbar.pack(side=LEFT, padx=10)

enter= CTkButton(searchframe, command= search, width=10, text="Search",fg_color="lime", font=("Helvetica", 14, "bold"), text_color="black", border_color="black", border_width=2, corner_radius=25)
enter.pack(side=RIGHT, anchor=NE)

searchframe.pack(side= LEFT, pady=15, anchor= NW)

#Output Portion
outframe=CTkFrame(root, height=200, width=350, corner_radius=10)

# Create a label widget -> to show the weather icon
# icon = Label(outframe)
# icon.pack()

# Create a label widget -> to show the city/country name
location = CTkLabel(outframe, text="This is Your city" ,font=("Poppins", 35, "bold"))
location.pack(pady=30)


# Create a label widget -> to show the temperature
temperature = CTkLabel(outframe,text="Is it too hot? Or, freezing?", font=("Poppins", 25, "bold"))
temperature.pack(pady=10)

# Create a label widget -> to show the weather description
description = CTkLabel(outframe,text="Search to know", font=("Poppins", 20, "bold"))
description.pack(pady=10)


outframe.place(relx=0.5, rely=0.5, anchor=CENTER)
outframe.pack_propagate(FALSE)

#lower bannner
lowerframe=CTkFrame(root, height=100, width=300, corner_radius=12, fg_color="black")

banner= Image.open("C:\\Users\\91905\\Code\\Pinnacle Weather Forecast\\missminutes.png")
bannerimg= ImageTk.PhotoImage(banner)
lowerbanner= Label(lowerframe, image= bannerimg, background="black")
lowerbanner.pack()
lowerframe.place(relx=0.5, rely=0.85, anchor=CENTER)
lowerframe.pack_propagate(FALSE)


root.mainloop()