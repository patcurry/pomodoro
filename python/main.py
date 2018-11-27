import time
import os

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
    time.sleep(seconds)
    print("Beer time!")
    os.system('say "Beer time!"')
    os.system('afplay ./sounds/techno.mp3')

one_minute = 60
five_minutes = 60 * 5
ten_minutes = 60 * 10
fifteen_minutes = 60 * 15
twenty_minutes = 60 * 20 
twenty_five_minutes = 60 * 25
thirty_minutes = 60 * 30

stopwatch(one_minute)

