from time import sleep

class StateMachine:
    def __init__(self):
        self.start_state_name = None
        self.end_state_name = None
        self.states = {}
        self.curr_action = (False, False, False, False, False)

    def add_state(self, name, state_obj, end_state=False, start_state=False):
        if start_state:
            self.start_state_name = name
        if end_state:
            self.end_state_name = name
        self.states[name] = state_obj

    # Get the next state based on the current state and the data
    def get_next_state(self, curr_state, data):
        # if it is in the end state, stay there
        if curr_state.name == self.end_state_name:
            return curr_state.name
        return curr_state.next_state(data)

    # update_data - function that returns the current
    #               inputs to the FSM
    def run(self):
        curr_state = self.states[self.start_state_name]
        while True:
            curr_state.run()
            sleep(1)
            data = self.curr_action
            next_state_name = self.get_next_state(curr_state, data)
            if next_state_name != curr_state.name:
                print("state transitioned from %s to %s"%(curr_state.name, next_state_name))
            curr_state = self.states[next_state_name]