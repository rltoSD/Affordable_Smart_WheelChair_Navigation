class NavigatingState:
    def __init__(self):
        self.name = "navigating"

    def run(self):
        print("navigating_state::body")

    def next_state(self, data):
        # decompose the data tuple
        (start_mapping,
        start_logging,
        map_built,
        goal_received,goal_reached) = data
        if goal_reached:
            return "navigation_ready"
        else:
            return self.name