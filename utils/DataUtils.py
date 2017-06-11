from .NetUtils import ser, Headers
from data.Holes import holes
from data.HoleState import HoleState
from data.serialize.SerializableHole import SerializableHole
from data.serialize.Output import Output
from configure.Configure import rows, cols

import jsonpickle
import time



# read serial and process data

def process_data(t):

    tim = ser.readline().decode()
    if tim != '':
        actual_tim = int(tim) - t
        data = ser.read(16)
        state = 0
        for y in range(int(rows * cols)):
            if y % 4 == 0:
                state = data[y>>2]
            curr_state = int((state & 0b11000000) >> 6)
            holes[y].add_state(curr_state, actual_tim*1000)
            state <<= 2
    time.sleep(0.5)
    ser.flushInput()


# serialize
def get_serialized(t):
    serializable_holes = []
    for x in range(0, rows * cols):
        holes[x].add_last_state()
        serializable_holes.append(SerializableHole(holes[x]))
    return Output(t, rows, cols, serializable_holes)


# json and write to file
def json_write(serialized, t):
    file = open('output/' + str(int(t)) + '.json', 'a')
    file.write(jsonpickle.encode(serialized, unpicklable=False))
    file.close()
