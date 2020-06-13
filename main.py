from blessings import Terminal
import psutil_data as data
import psutil
from time import sleep
from os import system
from datetime import datetime
import platform

system("clear")
t = Terminal()
memory_history = []
while True:


    # Print titlebar with date, time, etc
    for i in range(0, t.width):
        with t.location(i,0):
            print("{t.bold}█{t.normal}".format(t=t), end='')
    print('\n')
    with t.location(1,0):
        print('{t.bold}{t.black}{t.on_white}pytop{t.normal}'.format(t=t))
    with t.location(t.width-1-len(str(datetime.now())),0):
        print( ("{t.bold}{t.black}{t.on_white}"+ str(datetime.now()) + "{t.normal}").format(t=t))
    print('\n')
    with t.location(t.width-1-len("Uptime: " + str(data.uptime())),2):
        print(("{t.bold}" + "Uptime: " + str(data.uptime()) + "{t.normal}").format(t=t))
    with t.location(t.width-1-len(str(platform.system()) + " | " + platform.release()),1):
        print(str("{t.bold}" + platform.system() + " | " + platform.release()  + "{t.normal}").format(t=t))
    print('\n')

    # Get current CPU data and add to history
    # If the history is storing more items than the terminal width, remove extra items
    # cpu_percents = data.cpu_percent_ints()
    # cpu_percents_history.insert(0, cpu_percents)
    # del cpu_percents_history[t.width:len(cpu_percents_history)-1]

    # Print CPU usage charts - probs bar graphs like htop because braille lines are more effort than they are worth tbh
    currentThread = 0
    cpu_percents = data.cpu_percent_ints()
    while currentThread <= data.cpu_threads():
        w = 1
        h = 2 + (2 * currentThread)
        if currentThread < 4:
            w = 1
        elif 4 <= currentThread < 8:
            w = 5

        with t.location(w, h):
            print(str(currentThread) + ": [", end='')
            for j in range (1, int(round(list(map((lambda x: x/100 * ((t.width/2)-12)), cpu_percents))[currentThread]))):
                print("-", end='')


        currentThread += 1
        print('\n')
        
    print('\n')

    # Memory usage chart? Or just number
    # PID list
    # Historical graph of network usage - probs bar graph
    
    sleep(0.5)
    system("clear")