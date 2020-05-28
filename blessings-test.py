#!/usr/bin/env python3 

from blessings import Terminal
import psutil_data as data
import psutil
from time import sleep
from os import system

t = Terminal()

with t.location(t.width//2, t.height - 1):
    print('This is at the bottom.')

threads = data.cpu_threads()
currentWidth = 0
currentHeight = 0
while True:
    cpu_percents = data.cpu_percent_ints()
    
    # Print bars representing thread usage
    for i in range (0, threads):
        with t.location(1, 1 + i):
            if i < 9:
                print("CPU thread " + str(i+1) + "  [", end='')
            else:
                print("CPU thread " + str(i+1) + " [", end='')
            for j in range (1, cpu_percents[i]):
                print("=", end='')
            for k in range (cpu_percents[i], 100):
                print("-", end='')
            print("]")

    sleep(1)
    system("clear")