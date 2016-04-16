"""
My aim with this is to create a simple slackbot chat script. I'm not talking artificial
intelligence here. I'm talking a user entering a certain question / phrase and an action happening.
For example, what's the weather today 90210 (or a variation of that) and it printing out the weather
forecast for that zip code.
"""
from urllib.request import urlopen


class ChatBot:
    """
    Building out the foundations for a simple chat bot.
    """
    slack_url = "https://slack.com/api/"
    token = "?token=xoxp-8994446855-8994371508-35172505877-b6710faf39"
    pretty_print = "&pretty=1"

    def __init__(self, chat_type, channel, message, user="&username=Super%20Bot"):
        self.chat_type = chat_type
        self.message = message
        self.channel = channel
        self.user = user

    def build_url(self):
        """
        Building out the url to use
        :return:
        """
        if self.chat_type == "chat.postMessage":
            url = urlopen(self.slack_url + self.chat_type + self.token +
                          self.channel, self.user, self.pretty_print).read().decode("utf8")
            self.send_message(url)
        else:
            url = urlopen(self.slack_url + self.chat_type + self.token +
                          self.channel, self.user, self.pretty_print).read().decode("utf8")
            self.read_message(url)

    @staticmethod
    def send_message(link):
        """
        This will send the message to slack
        :param link:
        :return:
        """
        print(link)

    @staticmethod
    def read_message(link):
        """
        Reading messages
        :param link: url for Slack
        :return:
        """
        print(link)


general = "rtm.start"
channels = "channels.join"
channel_name = "&name=general"
msg = "Testing%20with%20a%20pretty%20python%20class!"
msg_channel = "chat.postMessage"
chat_channel = "&channel=general"

# info = urlopen(slack_url + general + token + pretty_print).read().decode("utf8")
# open_general_channel = urlopen(slack_url + channels + token + channel_name + pretty_print).read().decode("utf8")
# test_chat = urlopen(slack_url + msg_channel + token + chat_channel + msg + user + pretty_print).read().decode("utf8")

create_life = ChatBot(msg_channel, chat_channel, msg)
create_life.build_url()
