#!/usr/bin/env python3
import psutil
from os import system
import os
import time
from time import sleep
import datetime

def uptime():
    return datetime.timedelta(seconds=int(time.time() - psutil.boot_time()))

def cpu_percent_ints():
    return [int(i) for i in psutil.cpu_percent(None, True)]

def cpu_cores():
    return psutil.cpu_count(False)

def cpu_threads():
    return psutil.cpu_count(True)

def memory_percentage():
    return 0

def swap_memory_percentage():
    return 0

def disk_partition_totals():
    return 0

def disk_partition_used_totals():
    return 0

def process_list():
    return psutil.process_iter(['pid', 'name', 'username'])

def pid_cpu_usage(pid):
    process = psutil.Process(os.getpid())
    return process.cpu_percent()

def pid_memory_usage(pid):
    process = psutil.Process(os.getpid())
    return process.memory_percent()

def network_bytes_sent():
    return 0

def network_bytes_received():
    return 0

def network_bytes_sent_persec():
    return 0

def network_bytes_received_persec():
    return 0

def average_temp():
    return psutil.sensors_temperatures(fahrenheit=False)

# CPU usage + graph
# Memory usage + graph
# Disk space usage
# Temps
# Network usage (least important)
# List of processes

# while True:
#     print("---- SYSTEM DATA ----")

#     print(psutil.cpu_count(False)) # physical cores
#     print(psutil.cpu_count(True)) # threads

#     # cpu percentage
#     print(psutil.cpu_percent(None, True))

#     # memory 
#     print(psutil.virtual_memory())
#     print(psutil.swap_memory()) # swap

#     # disk partitions
#     print(psutil.disk_partitions(all=False))
#     for i in psutil.disk_partitions(all=False):
#         print(i.mountpoint + " | " + str(psutil.disk_usage(i.mountpoint).total))

#     # processes list
#     # for proc in psutil.process_iter(['pid', 'name', 'username']):
#     #    print(proc.info)

#     # uptime
#     print("")
#     print("uptime: " + str(uptime()))

#     # network data
#     print(psutil.net_io_counters(pernic=False, nowrap=True)) # first two items in tuple are bytes sent and bytes received

#     print("")
#     print("temps")
#     print(psutil.sensors_temperatures(fahrenheit=False))

#     print(pid_memory_usage(20339))

#     sleep(1)
#     system("clear")
