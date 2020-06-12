from blessings import Terminal
import psutil_data as data
import psutil
from time import sleep
from os import system
from datetime import datetime

t = Terminal()
cpu_percents_history = []
memory_history = []
while True:


    # Print titlebar with date and time
    for i in range(0, t.width):
        with t.location(i,0):
            print("{t.bold}█{t.normal}".format(t=t), end='')
    print('\n')
    with t.location(1,0):
        print('{t.bold}{t.black}{t.on_white}pytop{t.normal}'.format(t=t))
    with t.location(t.width-1-len(str(datetime.now())),0):
        print( ("{t.bold}{t.black}{t.on_white}"+ str(datetime.now()) + "{t.normal}").format(t=t))
    print('\n')

    # Get current CPU data and add to history
    # If the history is storing more items than the terminal width, remove extra items
    cpu_percents = data.cpu_percent_ints()
    cpu_percents_history.insert(0, cpu_percents)
    del cpu_percents_history[t.width:len(cpu_percents_history)-1]

    # Print CPU usage chart
    for i in range (1, t.width-2):
        if i < len(cpu_percents_history):
            thread_values = cpu_percents_history[i]
            with t.location(t.width - 1 - i, 20 - int(round(list(map((lambda x: x/100 * (20)), thread_values))[0]))):
                if int(round(list(map((lambda x: x/100 * (20)), cpu_percents_history[i]))[0])) < int(round(list(map((lambda x: x/100 * (20)), cpu_percents_history[i]))[0])):
                    print("⠢")
                else:
                    print(".")
    print('\n')

    # Memory usage chart 
    

    sleep(0.5)
    system("clear")