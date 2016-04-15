"""
My aim with this is to create a simple slackbot chat script. I'm not talking artificial
intelligence here. I'm talking a user entering a certain question / phrase and an action happening.
For example, what's the weather today 90210 (or a variation of that) and it printing out the weather
forecast for that zip code.
"""
from urllib.request import urlopen


# TODO: Turn this into a class since it has a lot of different parts
class ChatBot:
    """
    Building out the foundations for a simple chat bot.
    """
    slack_url = "https://slack.com/api/"
    token = "?token=xoxp-8994446855-8994371508-35172505877-b6710faf39"

    def __init__(self, chat_type, channel, message, chat_option, user="&username=Super%20Bot"):
        self.chat_type = chat_type
        self.message = message
        self.channel = channel
        self.chat_option = chat_option
        self.user = user

    def build_url(self, message, channel, user):
        """
        Building out the URL / link to use for our chat bot
        :param message: Message to post to the channel (e.g. Good morning!)
        :param channel: what channel should we join (e.g. general
        :param user: what user name is joining the channel? (e.g. Super Bot)
        :return:
        """


general = "rtm.start"
pretty_print = "&pretty=1"
channels = "channels.join"
channel_name = "&name=general"
msg = "&text=Building a class to chat!".replace(" ", "%20")
msg_channel = "chat.postMessage"
chat_channel = "&channel=general"

info = urlopen(slack_url + general + token + pretty_print).read().decode("utf8")
open_general_channel = urlopen(slack_url + channels + token + channel_name + pretty_print).read().decode("utf8")
test_chat = urlopen(slack_url + msg_channel + token + chat_channel + msg + user + pretty_print).read().decode("utf8")

ChatBot(msg_channel, chat_channel, )
