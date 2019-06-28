class MappingState:
    def __init__(self):
        self.name = "mapping"

    def run(self):
        """
        Code to be executed when in start state
        """
        print("mapping_state::body")

    def next_state(self, data):
        # decompose the data tuple
        (start_mapping,
        start_logging,
        map_built,
        goal_received,goal_reached) = data
        if map_built:
            return "navigation_ready"
        else:
            return self.name