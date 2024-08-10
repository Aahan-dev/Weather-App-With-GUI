import tkinter as tk
import requests
import time
def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"# YOUR API KEY HERE"
    json_data = requests.get(api).json()
    
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    feels_like = int(json_data['main']['feels_like'] - 273.15)
    minimum_temp = int(json_data['main']['temp_min'] - 273.15)
    maximum_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    visibility = json_data['visibility']
    wind_speed = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset =  time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))
    
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(maximum_temp) + "C" + "\n" + "Min Temp: " + str(minimum_temp) 
    label1.config(text = final_info)
    label2.config(text = final_data)
    
canvas = tk.Tk()
canvas.geometry("700x600")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, justify='center', width = 20, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()
canvas.mainloop()