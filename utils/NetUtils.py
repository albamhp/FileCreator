import serial
import os
import serial.tools.list_ports

# headers class
class Headers:
    TIME_REQUEST = b'\1'
    TIME_HEADER = b'\2'
    TIME_SET = b'\3'
    DATA = b'\4'


def get_serial_port():
    seri = "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()
    return seri

# set serial connection
ser = serial.Serial(get_serial_port(), baudrate=9600, timeout=1)


# time sync
def time_sync():
    while True:

        ser.write(Headers.TIME_HEADER)
        os.system('date +%s > ' + get_serial_port())
        read = ser.read()
        #print(read)
        if read == Headers.TIME_SET:
            break
