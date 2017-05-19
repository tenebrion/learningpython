#! python3
"""
Automate the boring stuff - ch. 8
Saves and loads pieces of text to the clipboard
Usage: py.exe multiclipboard.py save <keyword> - loads keyword to clipboard
       py.exe multiclipboard.py <keyword> - Loads keyword to clipboard
       py.exe multiclipboard.py list - loads all keywords to clipboard
"""
import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    # Delete a keyword from the shelf
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        # Delete all keywords
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
