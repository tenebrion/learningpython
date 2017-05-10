"""
Simple regex task from Automate the boring stuff
Build a regex function that mimics the strip() skill.
If no options are passed to the function, just remove leading and ending blank spaces.
Otherwise, strip the string based on options sent to the function
"""
import re


def strip_string(content, parameter=None):
    """
    
    :param content: 
    :param parameter: 
    :return: 
    """
    if parameter is None:
        strip_spaces = re.compile(r'^\s+|\s+$')
        good_to_go = strip_spaces.sub('', content)
        return good_to_go
    else:
        strip_stuff = re.compile(parameter)
        finished_product = strip_stuff.sub('', content)
        return finished_product

remove_stuff = str('Spam')
print(strip_string("SpamSpamBaconSpamEggsSpamSpam", remove_stuff))
