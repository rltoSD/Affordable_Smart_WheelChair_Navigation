#!/usr/bin/env python
import rospy
from encoder_msg.msg import Encoder

def callback(data):
	#calls and stores encoder left and right 
	Encoder_left=data.Encoder.left
	Encoder_right=data.Encoder.right
        rospy.loginfo('Encoder_left: {}, Encoder_right: {}'.format(Encoder_left,Encoder_right))
def main():
	#create a new node
        rospy.init_node('Encoder_Information')
        #subscribe to topic
        rospy.Subscriber("/Encoder", Encoder, callback)
        rospy.spin()
if __name__== '__main__':
	main()
