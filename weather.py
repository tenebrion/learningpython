"""
What's the Weather?

Goal
Create a program that pulls data from OpenWeatherMap.org that prints out information about the current weather,
such as the high, the low, and the amount of rain for wherever you live. Depending on how skilled you are,
you can actually do some neat stuff with this project.

Subgoals
Print out data for the next 5-7 days so you have a 5 day/week long forecast.
Print the data to another file that you can open up and view at, instead of viewing the
information in the command line.
If you know html, write a file that you can print information to so that your project is
more interesting. Here is an example of the results from what I threw together.

Tips
APIs that are in Json are essentially lists and dictionaries. Remember that to reference something in a list,
you must refer to it by what number element it is in the list, and to reference a key in a dictionary,
you must refer to it by it's name.
Don't like Celsius? Add &units=imperial to the end of the URL of the API to receive your data in Fahrenheit.


"""
import json
from urllib.request import urlopen

url = "http://api.openweathermap.org/data/2.5/"
api_key = "&APPID=e98088861de4eec95eff5e86adaae2b2"
current_weather_zip = "weather?zip="
current_weather_city = "weather?q="
user_city = input("What city would you like to get the current weather for? : ")
user_zip = input("What zip code would you like to get the current weather for? : ")

test = urlopen(url + current_weather_zip + "85226" + api_key).read().decode("utf8")
obj = json.loads(test)

print(obj)