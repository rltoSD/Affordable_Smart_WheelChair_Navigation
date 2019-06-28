class NavigationReadyState:
    def __init__(self):
        self.name = "navigation_ready"

    def run(self):
        """
        Code to be executed when in start state
        """
        print("navigation_ready_state::body")

    def next_state(self, data):
        # decompose the data tuple
        (start_mapping,
        start_logging,
        map_built,
        goal_received,goal_reached) = data
        if goal_received:
            return "navigating"
        else:
            return self.name