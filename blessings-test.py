#!/usr/bin/env python3 
from __future__ import print_function
from blessings import Terminal
import psutil_data as data
import psutil
from time import sleep
from os import system
from drawille import Canvas, line, animate
import math


# t = Terminal()

# threads = data.cpu_threads()
# currentWidth = 0
# currentHeight = 0

# max_history = 2 * t.width-2
# cpu_percents_history = []

# t.color(0)
# t.on_color(1)
# for i in range(0, t.width):
#     with t.location(i,0):
#         print(" ", end='')

# with t.location(0,0):
#     print("pytop", end = '')

# sleep(1)

# while True:
    # cpu_percents = data.cpu_percent_ints()
    # cpu_percents_history.insert(0, cpu_percents)
    # del cpu_percents_history[t.width:len(cpu_percents_history)-1]
    
    # Print bars representing thread usage
    # for i in range (0, threads):
    #     with t.location(1, 1 + i):
    #         if i < 9:
    #             print("Thread " + str(i+1) + "  ", end='')
    #         else:
    #             print("Thread " + str(i+1) + " ", end='')

    #         for j in range (1, int(round(list(map((lambda x: x/100 * ((t.width/2)-12)), cpu_percents))[i]))):
    #             print("█", end='')

    #         # for k in range (cpu_percents[i], 100):
    #         #     print("-", end='')
    #         # print("]")

    #         # int(round(list(map((lambda x: x/100 * ((t.width/2)-12)), cpu_percents))[i]))
    #         # int(round(list(map((lambda x: x/100 * (<max_scale>), <thread_array>))[<thread_index>]))
    
    
    

    # for i in range (1, t.width-2):
    #     if i < len(cpu_percents_history):
    #         thread_values = cpu_percents_history[i]
    #         with t.location(t.width - 1 - i, 20 - int(round(list(map((lambda x: x/100 * (20)), thread_values))[0]))):
    #             print(".")

    # with t.location(10, 20):
    #     print("test")

    # i += 2

    # sleep(0.5)
    # system("clear")

def __main__():
    i = 0
    height = 40

    while True:
        frame = []

        frame.extend([coords for coords in
                      line(0,
                           height,
                           180,
                           math.sin(math.radians(i)) * height + height)])

        frame.extend([(x/2, height + math.sin(math.radians(x+i)) * height)
                      for x in range(0, 360, 2)])

        yield frame

        i += 2

if __name__ == '__main__':
    animate(Canvas(), __main__, 1./60)