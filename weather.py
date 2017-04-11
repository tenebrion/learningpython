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
from datetime import datetime
from misc_stuff import apis
import re

print("Welcome to our weather station.")
print("Would you like the daily weather or a 7 day forecast?")
print("Press 1 for daily or 7 for forecast")
user_want_forecast = False
user_pick = int(input())
print("Please enter the city or zip code you would like to check the current temperatures for:")
original_user_input = input()

if user_pick == 7:
    user_want_forecast = True


def remove_spaces(user_data):
    """
    Simple regex to remove all spaces in the user's input
    :param user_data: city or zip code
    :return: This should return any values without spaces
    """
    fixed_user_input = re.sub(r"\s+", "", user_data)
    return fixed_user_input


user_input = remove_spaces(original_user_input)


def weather_url(user_entry, daily_or_weekly):
    """
    Building out the url since this gets repeated a bit
    :param user_entry: This will either be a city name or zip code
    :param daily_or_weekly: This will determine if the user wants a 1 day forecast or 7 days
    :return:
    """
    daily_partial_url = "http://api.openweathermap.org/data/2.5/weather?"
    forecast_partial_url = "http://api.openweathermap.org/data/2.5/forecast/daily?q="
    # The API key is stored in a separate file using tiny db
    api_key = apis.open_weather()
    zip_code_url = "zip="
    city_url = "q="
    number_forecast_days = "&cnt=7"

    if user_entry.isdigit() and not daily_or_weekly:
        return "{}{}{}{}".format(daily_partial_url, zip_code_url, str(user_entry), api_key)
    elif not daily_or_weekly:
        return "{}{}{}{}".format(daily_partial_url, city_url, str(user_entry), api_key)
    else:
        return "{}{}{}{}".format(forecast_partial_url, str(user_entry), number_forecast_days, api_key)


class WeatherConversion:
    """
    building out the blueprint for the weather values.
    """
    def __init__(self, full_url):
        self.full_url = full_url

    def print_weather(self, days):
        """
        This will use all the methods in the class to print out the relevant temperature information
        :param self:
        :param days: either 1 day forecast or a 7-day forecast
        :return:
        """
        if days == 1:
            open_weather = urlopen(self.full_url).read().decode("utf8")
            read_json = json.loads(open_weather)
            outside = self.get_outside_outlook(read_json["weather"])
            wind_speed = read_json["wind"]["speed"]
            wind_direction = self.deg_to_compass(read_json["wind"]["deg"])
            current_temp = self.convert_temp(read_json["main"]["temp"])
            print("Current Temperature: {:.2f}\xb0\n"
                  "Sky: {}\n"
                  "Wind speed: {} MPH\n"
                  "Wind direction: {}".format(current_temp, outside, wind_speed, wind_direction))
        else:
            open_weather = urlopen(self.full_url).read().decode("utf8")
            read_json = json.loads(open_weather)
            outside = read_json["list"]
            """
            Should be:
            for temp in outside:
                stuff = temp["weather"]
                for i in stuff:
                    print(i['description'])

            Each of these will need to be added to a list or a dictionary to print relationally
            """
            print(outside)

    def get_outside_outlook(self, weather_description):
        """
        Returning the outside weather description (e.g. overcast clouds)
        :return:
        """
        for entries in weather_description:
            return entries["description"]

    def convert_temp(self, temperature):
        """
        Simple kelvin to fahrenheit conversion
        :return:
        """
        return 1.8 * (temperature - 273) + 32

    def deg_to_compass(self, num):
        """
        This will convert wind speed in degrees to the typical 'compass' directions
        :return:
        """
        convert = int((num / 22.5) + .5)
        compass = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                   "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        return compass[(convert % 16)]

    def convert_date_time(self, dt):
        """
        Simple method to convert unix date/time to something more human
        return:
        """
        return datetime.fromtimestamp(dt).strftime("%Y-%m-%d")


full_weather_url = weather_url(user_input, user_want_forecast)
# print(json.dumps(read_json, indent=4, sort_keys=True))
values = WeatherConversion(full_weather_url)
values.print_weather(1)
