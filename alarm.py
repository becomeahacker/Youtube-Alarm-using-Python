import requests 
import webbrowser
import sys
import string
from time import sleep

playlist = """https://www.youtube.com/watch?v=JRfuAukYTKg&list=PLU-xowTNQLqjCOqVO25wqXG8j0rsvBsYX"""



sa = sys.argv
lsa = len(sys.argv)
if lsa != 2:
    print("Usage:alarm_clock.py duration_in_minutes")
    print("Example:alarm_clock.py 10")
    sys.exit(1)
try:
    minutes = int(sa[1])
except ValueError:
    print("Invalid numeric value (%s) for minutes" % sa[1])
    print("Should be an integer >= 0")
    sys.exit(1)
if minutes < 0:
    print("Invalid value for minutes, should be >= 0")
    sys.exit(1)
seconds = minutes * 60
if minutes == 1:
    unit_word = " minute"
else:
    unit_word = " minutes"

try:
    if minutes > 0:
        print ("Sleeping for " + str(minutes) + unit_word)
        sleep(seconds)
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(playlist)
except KeyboardInterrupt:
    print("Interrupted by user")
    sys.exit(1)
