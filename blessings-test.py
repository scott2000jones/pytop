#!/usr/bin/env python3 

from blessings import Terminal
import psutil_data as data
import psutil
from time import sleep
from os import system

t = Terminal()

threads = data.cpu_threads()
currentWidth = 0
currentHeight = 0

max_history = 2 * t.width-2
cpu_percents_history = []

while True:
    cpu_percents = data.cpu_percent_ints()
    cpu_percents_history.insert(0, cpu_percents)
    del cpu_percents_history[t.width:len(cpu_percents_history)-1]
    
    # Print bars representing thread usage
    for i in range (0, threads):
        with t.location(1, 1 + i):
            if i < 9:
                print("Thread " + str(i+1) + "  ", end='')
            else:
                print("Thread " + str(i+1) + " ", end='')

            for j in range (1, int(round(list(map((lambda x: x/100 * ((t.width/2)-12)), cpu_percents))[i]))):
                print("█", end='')

            # for k in range (cpu_percents[i], 100):
            #     print("-", end='')
            # print("]")

            # int(round(list(map((lambda x: x/100 * ((t.width/2)-12)), cpu_percents))[i]))
            # int(round(list(map((lambda x: x/100 * (<max_scale>), <thread_array>))[<thread_index>]))
    
    for i in range (1, t.width-2):
        if i < len(cpu_percents_history):
            thread_values = cpu_percents_history[i]
            # print(type(thread_values))
            with t.location(t.width - 1 - i, 20 - int(round(list(map((lambda x: x/100 * (20)), thread_values))[0]))):
                print(".")

    with t.location(10, 20):
        print("test")

    sleep(1.5)
    system("clear")