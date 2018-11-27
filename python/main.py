import time
import os

def how_long():
    try:
        t = int(input('So, how long do you want to work, in minutes? '))
    except:
        # if they give an invalid response... well then it's beer time!
        return 0

    if t == 1:
        print(t, 'minute')
    else:
        print(t, 'minutes')
    return t * 60

def stopwatch(seconds):
    #start = time.time()
    #time.perf_counter()
    #elapsed = 0
    #while elapsed < seconds:
    #    elapsed = time.time() - start
    #    #print("loop cycle time: %f, seconds count: %02d") % (time.clock() , elapsed) 
    #    #print(time.perf_counter())
    #    print(f'{elapsed:.0f}')
    #    time.sleep(1)  

    # I don't really need to print anything out... I just need to wait, right?
    print("Get to work!")
    os.system('say "Get to work!"')
    time.sleep(seconds)
    print("Beer time!")
    os.system('say "Beer time!"')
    os.system('afplay ./sounds/techno.mp3')

# call the functions
minutes = how_long()
stopwatch(minutes)
