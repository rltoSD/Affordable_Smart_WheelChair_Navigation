#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32, String

# Import the Nodes and the states
from Nodes.state_machine import StateMachine
from Nodes.start_state import StartState
from Nodes.mapping_state import MappingState
from Nodes.logging_state import LoggingState
from Nodes.nav_ready_state import NavigationReadyState
from Nodes.navigating_state import NavigatingState

# action = (start_mapping, start_logging, map_built, goal_received, goal_reached)
# indices for the events
IND_START_MAPPING = 0
IND_START_LOGGING = 1
IND_MAP_BUILT     = 2
IND_GOAL_RECEIVED = 3
IND_GOAL_REACHED  = 4

# Global variables storing current action
start_mapping = False
start_logging = False
map_built = False
goal_received = False
goal_reached = False


if __name__ == '__main__':
    rospy.init_node('fsm_node', anonymous=True)
    fsm = StateMachine()

    rospy.Subscriber("start_mapping", Float32,
                        lambda data:fsm.curr_action[IND_START_MAPPING] = data.data==1.0)
    rospy.Subscriber("start_logging", Float32, 
                        lambda data:fsm.curr_action[IND_START_LOGGING] = data.data==1.0)
    rospy.Subscriber("map_built", Float32,
                        lambda data:fsm.curr_action[IND_MAP_BUILT] = data.data==1.0)
    rospy.Subscriber("goal_received", Float32,
                        lambda data:fsm.curr_action[IND_GOAL_RECEIVED] = data.data==1.0)
    rospy.Subscriber("goal_reached", Float32,
                        lambda data:fsm.curr_action[IND_GOAL_REACHED] = data.data==1.0)

    
    fsm.add_state("start", StartState(), start_state=True)
    fsm.add_state("mapping", MappingState())
    fsm.add_state("logging", LoggingState())
    fsm.add_state("navigation_ready", NavigationReadyState())
    fsm.add_state("navigating", NavigatingState())
    fsm.run()
