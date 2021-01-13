# stopwatch.py

import time

# Display the program's instructions.

print('Press Enter to begin. Afterwards, press ENTER to "Click" the stopwatch.')
input()
startTime = time.time()
lastTime = startTime
lapNum = 1

# Tracking time
try:
    while True:
        input()
        laptime = round(time.time() - lastTime,2)
        total_time = round(time.time() - startTime,2)
        print("Lap #%s: %s (%s)" % (lapNum,total_time,laptime))
        lapNum +=1
        lastTime = time.time()
except:
    print('Done!')