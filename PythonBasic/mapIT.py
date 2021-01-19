#! python

import webbrowser, sys, pyperclip

if len(sys.argv) > 1: 
    # Get Address from command line input
    address = ' '.join(sys.argv[1:]) #以' '作為合併間隔
else:
    # Get Address from clipboard
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)


