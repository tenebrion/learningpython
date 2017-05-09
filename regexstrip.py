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
    strip_spaces = re.compile(r'^\s+|\s+$')
    clean_up = strip_spaces.findall(content)
    good_to_go = strip_spaces.sub("", clean_up)
    return good_to_go

print(strip_string(" Please fix this spacing issue "))
