from configure.Configure import raspberry
from utils.DataUtils import *
from utils.NetUtils import ser, time_sync
from utils.CameraUtils import *
import threading
import os
import sys
import time

# time sync
time_sync()
t = int(time.time())

if raspberry:
    from utils.RaspberrySetup import *
    rasp_setup()
    while GPIO.input(16):
        t = int(time.time())
        t_stop = threading.Event()
        camera_thread = threading.Thread(target=camera_record, arg  s=(t, t_stop))
        camera_thread.start()
        while GPIO.input(16) and GPIO.input(18):
            process_data(t)
        t_stop.set()
        json_write(get_serialized(t), t)
    GPIO.cleanup()
    ser.close()
    #  Shutdown
    # os.system('shutdown now -h')

else:
    # get serial data and process
    for x in range(0, 64):
        process_data(t)

    # write data into file
    json_write(get_serialized(t))
    ser.close()
