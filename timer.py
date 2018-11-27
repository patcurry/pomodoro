#!/usr/bin/env python3
import time
import sys
import os

def how_long():
    try:
        t = int(input('So, how long do you want to work, in minutes? '))
    except:
        # if they give an invalid response... well then it's beer time!
        return 0
    if t == 1:
        print(t, 'minute')
    elif t < 1:
        t = 1
        print(t, 'minute')
    else:
        print(t, 'minutes')
    return t * 60


def counting_increment():
    try:
        t = int(input('What should the counting increment be, in seconds? '))
    except:
        return 1
    if t == 1:
        print(t, 'second')
    elif t < 1:
        t = 1
        print(t, 'second')
    else:
        print(t, 'seconds')
    return t

def timer(minutes_to_seconds, inc):
    print("Get to work!")
    os.system('say "Get to work!"')

    for remaining in range(minutes_to_seconds, 0, -inc):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(inc)

    sys.stdout.flush()
    print("\nBeer time!")
    os.system('say "Beer time!"')
    os.system('afplay ./sounds/techno.mp3')

# call everything
minutes_to_seconds = how_long()
increment = counting_increment()
timer(minutes_to_seconds, increment)
