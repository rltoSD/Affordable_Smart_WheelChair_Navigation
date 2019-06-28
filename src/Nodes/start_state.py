

class StartState:
    def __init__(self):
        self.name = "start"

    def run(self):
        """
        Code to be executed when in start state
        """
        print("start_state::body")

    def next_state(self, data):
        # decompose the data tuple
        (start_mapping,
        start_logging,
        map_built,
        goal_received,goal_reached) = data

        if start_logging:
            return "logging"
        elif start_mapping:
            return "mapping"
        else:
            return self.name