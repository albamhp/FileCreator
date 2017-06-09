

# hole state class contains: state and time

class HoleState:
    EMPTY = 0b00
    ERROR = 0b01
    SMALL = 0b10
    BIG = 0b11

    def __init__(self, state, time):
        self.time = time
        self.state = state
