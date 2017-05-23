#! python3
"""
map_it.py - Launches a map in the browser using an address from the command line or clipboard
"""
import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = " ".join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/{}".format(address))
