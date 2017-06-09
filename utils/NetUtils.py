import serial
import os
from configure.Configure import port


# headers class
class Headers:

    TIME_REQUEST = b'\1'
    TIME_HEADER = b'\2'
    TIME_SET = b'\3'


# set serial connection
ser = serial.Serial(port, baudrate=9600, timeout=1)


# time sync
def time_sync():
    while True:
        read = ser.read()
        if read == Headers.TIME_REQUEST:
            ser.write(Headers.TIME_HEADER)
            os.system('date +%s > /dev/ttyACM0')
            read = ser.read()

        if read == Headers.TIME_SET:
            break
