import time
import bluetooth
import re
from MindwaveDataPoints import RawDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader


if __name__ == '__main__':
    mac = '9C:B7:0D:72:CD:02'
    print "do you want to use the default MAC address?(Y/n):"
    mac_yn = raw_input().lower()
    while not (mac_yn=='' or mac_yn.startswith('y')):
        print "What mac address would you like to use?:"
        mac = raw_input().lower()
        if re.match(r'[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]',mac):
            mac_yn = 'y'
        else:
            print "A valid mac address is something like 9C:B7:0D:72:CD:02." 
            print "Try again?"
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start(mac)
    
    while(True):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        if (not dataPoint.__class__ is RawDataPoint):
            print dataPoint

        
