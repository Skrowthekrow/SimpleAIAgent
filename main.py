# Creating a simple Reflex AI Agent. I originally worked on a much more complex
# AI agent that could be fed a list of T/F from excel and spit out its prediction in a test.
# After re-reading the instructions however I believe I've overthought the assignment.
# Sean Work
# Artificial Intelligence W01
import tkinter
from random import *
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

# config file with key to input
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['hgh']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
# config file with key to input

#global variable to change inside func
curr_weather=''

# func for exit button to call
def turn_off():
    root.destroy()
    root.quit()

# func for Simple Reflex AI
def weather_bot_response():

    if curr_weather == 'Thunderstorm':
        return 'It\'s storming! Head for cover!!'

    elif curr_weather == 'Clouds':
        return'Partly Cloudy! Not much to say on this lol.'

    elif curr_weather == 'Clear':
        return 'It\'s a great day! Put some sunscreen on!'

    else:
        return 'I\'ve never seen this weather before! Be careful looks dangerous!'
# func for advice button that changes output based on city
def onClick():
    global text1
    response.config(text = weather_bot_response())
#api func for getting api return, i commented out the the location label because I wasnt happy with the info provided.
# never worked with an API before
def search():
    city = city_text.get()
    weather = getweather(city)
    global curr_weather
    if weather:
        #location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3])+"   Degree Fahrenheit"
        weather_l['text'] = weather[4]
        curr_weather = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))

# func to collect info in json and return as an array
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_farenht = (temp_kelvin -273.15) * 1.8 + 32
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin,
                 temp_farenht, weather1]
        return final
    else:
        print("NO Content Found")



# gui beginning
root = Tk()
root.geometry("900x300")
root.title("Weather Advice Bot")



welcome = Label(root, text='Hi! I\'m your friendly weather bot! \nProviding you '
      'with helpful advice regarding the weather that my sensors pick up!\n'
      'For the sake of this test my sensors will pick up weather info from the OpenWeatherAPI\n')
welcome.pack()


city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.pack()

Search_btn = Button(root, text="Search Weather",width=12, command=search)
Search_btn.pack()

location_lbl = Label(root, text="Current Weather",font={'bold', 20})
location_lbl.pack()

temperature_label = Label(root, text="")
temperature_label.pack()

weather_l = Label(root, text="")
weather_l.pack()



response = Label(root,text='Get Your Answer by pressing the button above!', font=("Comic-Sans", 16))

pressMe = Button(root, text="Get Weather Tip!", padx=5, pady=5, command=onClick)
endProg = Button(root, text="Exit Program", padx=5, pady=5, command=turn_off)

pressMe.pack()
response.pack()
endProg.pack()

root.mainloop()


