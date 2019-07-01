#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

def callback(data):
	label=data.layout.dim[0].label
	size=data.layout.dim[0].size
	stride=data.layout.dim[0].stride
	rospy.loginfo('label: {}, size: {}, stride: {}'.format(label,size,stride))
def main():
	rospy.init_node('TFS_Information')
	rospy.subscriber("/Float64MultiArray", Float64MultiArray, callback)
	rospy.spin()
if __name__== '__main__':
	main()
	
