from .HoleState import HoleState


# hole class contains: oldstate and list of states
class Hole:

    def __init__(self):
        self.oldState = HoleState(0, 0)
        self.states = []    # creates a new empty list for each hole

    def add_state(self, newState, time):
        # self.oldState comparar a newState, dependiendo de cosas, o añades el viejo, y el nuevo se guarda en el viejo
        # o simplemente matas el viejo y el nuevo se guarda ahi
        # no change in state
        if self.oldState.state == newState:
            return
        # coming from empty to any state save changes
        if self.oldState.state == HoleState.EMPTY:
            self.replace_state(newState, time)
        # coming from error to empty only
        elif self.oldState.state == HoleState.ERROR and newState == HoleState.EMPTY:
            self.replace_state(newState, time)
        # coming form small to empty or error
        elif self.oldState.state == HoleState.SMALL:
            if newState != HoleState.BIG:
                self.replace_state(newState, time)
            else:
                self.oldState.state = newState
        # coming from big to empty or error
        elif self.oldState.state == HoleState.BIG and newState != HoleState.SMALL:
            self.replace_state(newState, time)

    def add_last_state(self):
        if len(self.states) == 0 or self.oldState.state != self.states[len(self.states)-1].state:
            self.replace_state(0, 0)

    def replace_state(self, newState, time):
        self.states.append(self.oldState)
        self.oldState = HoleState(newState, time)
