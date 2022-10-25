print("canvas-assistant")
print("Written with <3 by TheMemeSniper")
print("Linux v1.0.0")

# Import dependencies
from colorama import Fore
from canvasapi import Canvas
import os
from datetime import datetime
import time
# We do not use the notify2 module, since it's broken on Crostini. We will use the notify-send command instead.

### FUNCTIONS START ###
def get_part_of_day(h):
    return (
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 22
        else "night"
    )

### FUNCTIONS END ###

# Check if url.txt exists, if it does, set API_URL to the provided URL
if os.path.exists("url.txt"):
    with open("url.txt","r") as f:
        API_URL = f.readline()
else:
    print(f"{Fore.RED}CA: Critical error")
    print(f"{Fore.RED}CA: url.txt not found")
    exit()
# Check if token.txt exists, if it does, set API_KEY to the user's Canvas API token
if os.path.exists("token.txt"):
    with open("token.txt","r") as f:
        API_KEY = f.readline()
else:
    print(f"{Fore.RED}CA: Critical error")
    print(f"{Fore.RED}CA: token.txt not found")
    exit()
canvas = Canvas(API_URL, API_KEY)
# Check if a name.txt exists, and if it does, use that instead of the name provided by Canvas
if os.path.exists("name.txt"):
    with open("name.txt","r") as f:
        uname = f.readline()
else:
    rawname = canvas.get_current_user()
    uname = str(rawname).split('(')[0]
# Check the time so we can tell the user good morning/afternoon/evening
part = get_part_of_day(datetime.now().hour)
os.system(f'notify-send "canvas-assistant" "Good {part}, {uname}."')
# Get values for our stuff

unread = canvas.conversations_unread_count()["unread_count"]
events = canvas.get_calendar_events()
for item in events:
    print(item)

# Check for new assignments, messages, and all that good stuff every 5 minutes.
while True:
    if int(canvas.conversations_unread_count()["unread_count"]) >= 1:
       os.system(f'notify-send "canvas-assistant" "You have {unread} unread Canvas message(s)."')
    
    time.sleep(300)
