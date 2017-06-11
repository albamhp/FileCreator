from configure.Configure import raspberry
from utils.DataUtils import *
from utils.NetUtils import *
from utils.CameraUtils import *
import threading
import os
import sys
import time
from data.Holes import createHoles

# time sync
t = int(time.time())
createHoles()


if raspberry:
    from utils.RaspberrySetup import *
    rasp_setup()
    while GPIO.input(16):
        t_stop = threading.Event()
        camera_thread = threading.Thread(target=camera_record, args=(t, t_stop))
        t = int(time.time())
        camera_thread.start()

        start = 0
        while GPIO.input(16) and GPIO.input(18):
            header = ser.read()
            if header == Headers.TIME_REQUEST:
                time_sync()
            elif header == Headers.DATA:
                process_data(t)

                #print (time.time()-start)
                start = time.time()

        t_stop.set()
        json_write(get_serialized(t), t)
        createHoles()
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
