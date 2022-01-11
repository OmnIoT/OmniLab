import UPS
import time
from datetime import datetime

ups_lite = UPS.MAX17043()

while True:
    log = open("charging_log.txt","a")
    voltage = ups_lite.read_voltage()
    capacity = ups_lite.read_capacity()
    line = ("[%s] voltage=%s, capacity=%s" % (datetime.now(),voltage,capacity))
    print(line)
    log.write(line + "\n")
    log.close()
    time.sleep(60)