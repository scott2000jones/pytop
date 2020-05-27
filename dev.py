#!/usr/bin/env python3
import psutil
from os import system
import time
from time import sleep
import datetime

def uptime():
    return datetime.timedelta(seconds=int(time.time() - psutil.boot_time()))


# CPU usage + graph
# Memory usage + graph
# Disk space usage
# Temps
# Network usage (least important)
# List of processes

while True:
    print("---- SYSTEM DATA ----")

    print(psutil.cpu_count(False)) # physical cores
    print(psutil.cpu_count(True)) # threads

    # cpu percentage
    print(psutil.cpu_percent(None, True))

    # memory 
    print(psutil.virtual_memory())
    print(psutil.swap_memory()) # swap

    # disk partitions
    print(psutil.disk_partitions(all=False))
    for i in psutil.disk_partitions(all=False):
        print(i.mountpoint + " | " + str(psutil.disk_usage(i.mountpoint).total))

    # processes list
    # for proc in psutil.process_iter(['pid', 'name', 'username']):
    #    print(proc.info)

    # uptime
    print("")
    print("uptime: " + str(uptime()))

    # network data
    print(psutil.net_io_counters(pernic=False, nowrap=True)) # first two items in tuple are bytes sent and bytes received

    sleep(1)
    system("clear")
