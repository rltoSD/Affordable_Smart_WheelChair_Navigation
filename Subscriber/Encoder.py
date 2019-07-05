#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback(data):
	data=data.data
        rospy.loginfo('Encoder_Left: {}'.format(data.data))
def callback_two(data):
	data=data.data
        rospy.loginfo('Encoder_Right: {}'.format(data.data))
def main():
	rospy.init_node('Encoder Information')
	rospy.subscriber("/encoder_left", Float64, callback)
	rospy.subscriber("/encoder_right", Float64, callback_two)
	rospy.spin()
if __name__== '__main__':
	main()
