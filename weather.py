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
more interesting.
"""
import json
from urllib.request import urlopen
import datetime
from misc_stuff import apis
import re

print("Welcome to our weather station.")
print("Please enter the city or zip code you would like to check the current temperatures for:")
original_user_input = input()


def remove_spaces(user_data):
    """
    Simple regex to remove all spaces in the user's input
    :param user_data: city or zip code
    :return: This should return any values without spaces
    """
    fixed_user_input = re.sub(r"\s+", "", user_data)
    return fixed_user_input


user_input = remove_spaces(original_user_input)


def weather_url(user_entry):
    """
    Building out the url since this gets repeated a bit
    :param user_entry: This will either be a city name or zip code
    :return:
    """
    url = "http://api.openweathermap.org/data/2.5/"
    api_key = apis.open_weather()
    zip_code_url = "weather?zip="
    city_url = "weather?q="

    if user_entry.isdigit():
        return "{}{}{}{}".format(url, zip_code_url, str(user_entry), api_key)
    else:
        return "{}{}{}{}".format(url, city_url, str(user_entry), api_key)


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


def convert_date_time(dt):
    """
    Simple method to convert unix date/time to something more human
    param: dt: stands for date / time in the JSON file I'm reading
    return:
    """
    for stuff in dt:
        return datetime.datetime.fromtimestamp(int(stuff["dt"])).strftime('%Y-%m-%d %H:%M:%S')


def print_weather():
    """
    building out the weather forecast.
    :return:
    """
    weather = weather_url(user_input)
    open_weather = urlopen(weather).read().decode("utf8")
    read_json = json.loads(open_weather)
    # print(json.dumps(read_json, indent=4, sort_keys=True))
    outside = get_outside_outlook(read_json["weather"])
    # min_temp = convert_temp(read_json["main"]["temp_min"])
    # max_temp = convert_temp(read_json["main"]["temp_max"])
    wind_speed = read_json["wind"]["speed"]
    wind_direction = deg_to_compass(read_json["wind"]["deg"])
    current_temp = convert_temp(read_json["main"]["temp"])

    print("Current Temperature: {:.2f}\n"
          "Sky: {}\n"
          "Wind speed: {} MPH\n"
          "Wind direction: {}".format(current_temp, outside, wind_speed, wind_direction))

print_weather()
