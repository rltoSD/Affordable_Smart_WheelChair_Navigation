#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

# called when publisher publishes to topic
def callback(data):
	#subscribes and grabs x,y,z position for Odometry
	x=data.pose.pose.position.x
	y=data.pose.pose.position.y
	z=data.pose.pose.position.z
	#subscribes and gets orientation z,x,y,w data for Odometry
	orientation_x=data.pose.pose.orientation.x
	orientation_y=data.pose.pose.orientation.y
	orientation_w=data.pose.pose.orientation.w
	orientation_z=data.pose.pose.orientation.z
	
	linear_x=data.twist.twist.linear.x
	linear_y=data.twist.twist.linear.y
	linear_z=data.twist.twist.linear.z
	
	angular_x=data.twist.twist.angular.x
	angular_y=data.twist.twist.angular.y
	angular_z=data.twist.twist.angular.z
	
	O=open("OdometryInformation.txt", "r+")
	
	rospy.loginfo(rospy.get_caller_id() + "Information: %s", data.data)

def listener():
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("Chatter", Odometry, callback)

	rospy.spin()

