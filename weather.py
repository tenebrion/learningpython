"""
What's the Weather?

Goal:
Create a program that pulls data from OpenWeatherMap.org that prints out information about the current weather,
such as the high, the low, and the amount of rain for wherever you live. Depending on how skilled you are,
you can actually do some neat stuff with this project.

Sub-goals:
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

print("Welcome to our weather station.")
print("Please enter the city or zip code you would like to check the current temperatures for:")
user_input = input()
zip_code_url = "weather?zip="
city_url = "weather?q="


def weather_url(user_weather_url, user_location):
    """
    Building out the url since this gets repeated a bit
    :param user_weather_url: This will be a zip code url or a city url (for the API query)
    :param user_location: This will be a zip code or a city name
    :return:
    """
    url = "http://api.openweathermap.org/data/2.5/"
    api_key = "&APPID=e98088861de4eec95eff5e86adaae2b2"

    return "{}{}{}{}".format(url, user_weather_url, str(user_location), api_key)


def get_outside_outlook(weather_description):
    """
    Returning the outside weather description (e.g. overcast clouds)
    :param weather_description: This should be a list with a dictionary inside it
    :return:
    """
    for entries in weather_description:
        return entries["description"]


def convert_temp(temperature):
    """
    Simple kelvin to fahrenheit conversion
    :param temperature: passing in a kelvin temperature
    :return:
    """
    return 1.8 * (temperature - 273) + 32


def deg_to_compass(num):
    """
    This will convert wind speed in degrees to the typical 'compass' directions
    :param num: This will be the degrees in which the wind is blowing
    :return:
    """
    convert = int((num / 22.5) + .5)
    compass = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
               "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return compass[(convert % 16)]


if user_input.isdigit():
    weather = weather_url(zip_code_url, user_input)
    open_weather = urlopen(weather).read().decode("utf8")
    read_json = json.loads(open_weather)
    # print(json.dumps(read_json, indent=4, sort_keys=True))
    outside = get_outside_outlook(read_json["weather"])
    # min_temp = convert_temp(read_json["main"]["temp_min"])
    # max_temp = convert_temp(read_json["main"]["temp_max"])
    wind_speed = read_json["wind"]["speed"]
    wind_direction = deg_to_compass(read_json["wind"]["deg"])
    current_temp = convert_temp(read_json["main"]["temp"])
    print("Current Temperature: {0:.2f}\n"
          "Sky: {}\n"
          "Wind speed: {} MPH\n"
          "Wind direction: {}".format(current_temp, outside, wind_speed, wind_direction))
else:
    weather = weather_url(city_url, user_input)
    open_weather = urlopen(weather).read()
    read_json = json.loads(open_weather)
    # print(json.dumps(read_json, indent=4, sort_keys=True))
    outside = get_outside_outlook(read_json["weather"])
    # min_temp = convert_temp(read_json["main"]["temp_min"])
    # max_temp = convert_temp(read_json["main"]["temp_max"])
    wind_speed = read_json["wind"]["speed"]
    wind_direction = deg_to_compass(read_json["wind"]["deg"])
    current_temp = convert_temp(read_json["main"]["temp"])
    print("Current Temperature: {0:.2f}\n"
          "Sky: {}\n"
          "Wind speed: {} MPH\n"
          "Wind direction: {}".format(current_temp, outside, wind_speed, wind_direction))
