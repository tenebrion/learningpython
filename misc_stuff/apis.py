from tinydb import TinyDB
from tinydb import Query


db = TinyDB(r'C:\Users\michael.f.koegel\Documents\Python\api.json')
api = Query()

if not db.search(api.name == 'OpenWeather'):
    db.insert({'name': 'OpenWeather', 'key': '&APPID=e98088861de4eec95eff5e86adaae2b2'})

if not db.search(api.name == 'slack'):
    db.insert({'name': 'slack', 'key': 'token=xoxp-8994446855-8994371508-35172505877-b6710faf39'})

if not db.search(api.name == 'RLSBot'):
    db.insert({'name': 'RLSBot', 'key': 'token=xoxb-35770302082-eiN6XauYmB7oyPBu8CrFti5g'})


def open_weather():
    """
    Returning OpenWeather API key
    :return:
    """
    weather_key = db.search(api.name == 'OpenWeather')
    for items in weather_key:
        return items['key']


def slack():
    """
    returning slack API key
    :return:
    """
    slack_key = db.search(api.name == 'slack')
    for items in slack_key:
        return items['key']


def rls():
    """
    returning slack API key
    :return:
    """
    rls_key = db.search(api.name == 'RLSBot')
    for items in rls_key:
        return items['key']