import psutil
from os import system
from time import sleep

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



    sleep(1)
    system("clear")
