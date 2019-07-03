#!/usr/bin/env python
import rospy
#import the message file so we can store it into the Float
from std_msgs.msg import Float64MultiArray

def callback(data):
	#stores data into variables
	label=data.layout.dim[0].label
	size=data.layout.dim[0].size
	stride=data.layout.dim[0].stride
	#prints it out to terminal
	rospy.loginfo('label: {}, size: {}, stride: {}'.format(label,size,stride))
def main():
	#creates a new node
	rospy.init_node('TFS_Information')
	#subscribes to the topic "tof_sensor" so we can receive information
	rospy.subscriber("/tof_sensor", Float64MultiArray, callback)
	rospy.spin()
if __name__== '__main__':
	main()
	
