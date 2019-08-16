import os
from os import path

class MappingState:
    def __init__(self):
        self.name = "mapping"

    def run(self):
        """
        Code to be executed when in start state
        """
	Exist = true

	for File in os.listdir('~/Navigation/'):
		if File.endswith('.yaml'):
		print("map exists")
		break
	else:
		print("map does not exist")
		Exist = false
	if not Exist: 
		print("starting mapping software")
		os.system("roslaunch robot_setup_tf convert.launch")
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
