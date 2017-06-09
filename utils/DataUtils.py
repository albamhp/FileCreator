from .NetUtils import ser
from data.Holes import holes
from data.HoleState import HoleState
from data.serialize.SerializableHole import SerializableHole
from data.serialize.Output import Output
from configure.Configure import rows, cols
import jsonpickle



# read serial and process data
def process_data(t):
    data = ser.readline().decode()
    if data != '':
        holes[int(data[:2])].add_state(HoleState(int(data[2:-11]), int(data[-11:]) - int(t)))


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
