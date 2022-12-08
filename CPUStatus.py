from __future__ import print_function

import sys

import psutil

from psutil._common import bytes2human
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)
def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))


def main():
    print("********************Welcome To MY programe**********")
    print("\n ")
    print("Your RAM status is := ")
    
    r=pprint_ntuple(psutil.virtual_memory())
    print("\n ")
    print("Your SWAP Memory status is :=  ")
    vm=pprint_ntuple(psutil.swap_memory())
    print("\n ")
    print("Your Memory status is :=  ")
    mem=pprint_ntuple(psutil.disk_usage("/"))
    
#  THRESHOLD = 100 * 1024 * 1024  # 100MB
#  if mem.available <= THRESHOLD:
#      print("warning")

   
    
    
    
   
   
    
    
    if not hasattr(psutil, "sensors_battery"):
        return sys.exit("\nplatform not supported")
    batt = psutil.sensors_battery()
    if batt is None:
        return print("\nno battery is installed")

    print("\ncharge:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        print("status:     %s" % (
            "charging" if batt.percent < 100 else "fully charged"))
        print("plugged in: yes")
    else:
        print("left:       %s" % secs2hours(batt.secsleft))
        print("status:     %s" % "discharging")
        print("plugged in: no")


if __name__ == '__main__':
    main()