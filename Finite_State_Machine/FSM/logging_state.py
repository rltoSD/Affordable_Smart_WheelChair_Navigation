import os
  
class LoggingState:
    def __init__(self):
        self.name = "logging"

    def run(self):
        os.system("rosbag record Odometry")
        os.system("rosbag record tf")
        print("logging_state::body")

    def next_state(self, data):
        # decompose the data tuple
        (start_mapping,
        start_logging,
        map_built,
        goal_received,goal_reached) = data
        return self.name
