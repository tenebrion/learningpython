"""
My aim with this is to create a simple slackbot chat script. I'm not talking artificial
intelligence here. I'm talking a user entering a certain question / phrase and an action happening.
For example, what's the weather today 90210 (or a variation of that) and it printing out the weather
forecast for that zip code.
"""
from urllib.request import urlopen
from misc_stuff import apis


slack_api = "https://slack.com/api/"
post_msg = "chat.postMessage?"
token = apis.slack()
rlsbot = apis.rls()
chat_channel = "&channel=C08V8D4RM"
message = "&text=Why doesn't anyone respond to emails these days?".replace(" ", "%20")
user = "&username=Super Bot".replace(" ", "%20")
pretty_print = "&pretty=1"
# general = "rtm.start"
# channels = "channels.join"
# channel_name = "&name=general"


def build_url(api, msg_format, slack_token, channel, msg, bot_user, printing):
    """
    Creating the format for the URL
    :param api: This is the api URL to call
    :param msg_format: Currently set to postMessage, but there is also a getMessage to read messages
    :param slack_token: My unique token
    :param channel: General chat channel, but I could set it to the Github channel I have.
    :param msg: Message for the room. Make sure to include %20 for spaces
    :param bot_user: currently set to Super Bot
    :param printing: This prints out the response neatly. A future use is to check for errors..
    :return:
    """
    if msg_format == "chat.postMessage":
        url = urlopen(api + msg_format + slack_token +
                      channel + msg + bot_user + printing).read().decode("utf8")
        send_message(url)
    else:
        url = urlopen(api + msg_format + slack_token +
                      channel + msg + bot_user + printing).read().decode("utf8")
        read_message(url)


def send_message(link):
    """
    This will send the message to slack
    :param link:
    :return:
    """
    print(link)


def read_message(link):
    """
    Reading messages
    :param link: url for Slack
    :return:
    """
    print(link)


build_url(slack_api, post_msg, token, chat_channel, message, user, pretty_print)
