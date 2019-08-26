#! /usr/bin/env python
import rospy
import time
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback

#feedback to be called when received feedback to indicate success  
def feedback_callback(feedback):
    
    print('[Feedback] Going to Goal Pose...')

# initializes the action client node
rospy.init_node('move_base_action_client')

# create the connection to the action server
client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)

# waits until the action server is up and running
client.wait_for_server()

# user input a location name
name = input()

# set the path to the saved file 
path = 'location.txt'

# open the txt file
f = open(path, "r")

#read every line to check if the input match any of them
for line in f:
	x = name in line
	if x:
		#if match, extract the position and orientation data and send them into goal
		a = line.split()
		goal = MoveBaseGoal()
		goal.target_pose.header.frame_id = 'map'
		goal.target_pose.pose.position.x = float(a[1])
		goal.target_pose.pose.position.y = float(a[2])
		goal.target_pose.pose.position.z = float(a[3])
		goal.target_pose.pose.orientation.x = float(a[4])
		goal.target_pose.pose.orientation.y = float(a[5])
		goal.target_pose.pose.orientation.z = float(a[6])
		goal.target_pose.pose.orientation.w = float(a[7])

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)


# wait until the result is obtained
client.wait_for_result()

# print the result
print('[Result] State: %d'%(client.get_state()))
