#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from gspeech_input_msg import move_msgs

x = 0.0
y = 0.0
z = 0.0
text = ""
textArr = []
pub = rospy.Publisher('/moveTopic', move_msgs, queue_size = 1)

def callbackOdom(data):
	global x
	global y
	global z
 	x = data.pose.pose.position.x
    	y = data.pose.pose.position.y	
    	z = data.pose.pose.position.z	

def callbackString(data):
	location = np.load("storage.npy").item()
	global text
	global textArr
	text = data.data
	textArr = data.data.split(" ")
	if textArr[0] == 'go':
		if textArr[2] in location:
			move = move_msgs()
			array = location[textArr[2]]
			move.x = array[0]
			move.y = array[1]
			move.z = array[2]
			pub.publish(move)
		else
			print "Location not found"
	else if textArr[0] == 'mark'
		if textArr[2] in location:
			print "Location already marked"
		else:
			arrOdom = [x,y,z]
			location[arr[2]] = arrOdom
			np.save("storage.npy", location)
	else if textArr[0] == 'remove'
		if textArr[2] in location:
			location.pop(textArr[2])
			np.save("storage.npy", locationMap)
		else:
			print "Location not found"

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("/odom", Odometry, callbackOdom)
	rospy.Subscriber("chatter", String, callbackString)
	rospy.spin()

if __name__ == '__main__':
	listener()
