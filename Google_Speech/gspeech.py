#!/usr/bin/env python

import rospy
import numpy as np 
import os
from gspeech_input_msg import input
from google.cloud import speech
from std_msgs.msg import String, Header
from nav_msgs.msg import Odometry
#magic numbers
minConfidence = 0.98
saveTranscript = ""
saveConfidence = 0.0
inputTuple = (saveTranscript, saveConfidence)
storage = []
#method to set global variables
def setVar(data):
	global saveTranscript
	global saveConfidence
	global inputTuple
	#saves and initializes global variables
	saveTranscript=input.transcript
	saveConfidence=input.confidence
	inputTuple=(saveTranscript, saveConfidence)
#saves the data inputted to a text and numpy file
def save(data):
	#opens the output.txt file for edit
	text_file=open("output.txt", "w")
	#writes the confidence and transcript
	text_file.write(saveTranscript)
	text_file.write(saveConfidence)
	text_file.close()
	storage.append(inputTuple)
	#save the array to numpy
	np.save('transcript_history.npy',storage)

def callback(data):
	setVar(data)
	locationMap = np.load("dictionary.npy").item()
	arr=data.transcript.split(" ")
	while saveConfidence < minConfidence:
		os.system("say 'Please repeat your command'")
		r = rospy.Rate(10)
		r.sleep()
		setVar(data)
		arr = data.transcript.split(" ")
	 save(data)
	 if arr[0] == 'go':
		if arr[2] in locationMap:
            		rospy.init_node("input_Node")
            		pub1 = rospy.Publisher('MoveTopic',move_msg,queue_size = 1)
            		r = rospy.Rate(1)
            		msg = move_topic()
            		array = locationMap[arr[2]]
            		msg.x= array[0]
            		msg.y= array[1]
            		msg.z= array[2]
            		msg.ax= array[3]
            		msg.ay= array[4]
            		msg.az= array[5]
            		pub1.publish(msg)
			r.sleep()
	else:
			 rospy.loginfo("Location %s is not found : %s",arr[2])	        
	else if arr[0] == 'mark':
		if arr[4] in locationMap:
			rospy.loginfo("Location %s exists", arr[4])
		else:
			arrOdometry = [data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.position.z,data.twist.twist.angular.x, data.twist.twist.angular.y, data.twist.twist.angular.z]
            		locationMap[arr[4]] = arrOdometry
            		np.save("dictionary.npy",locationMap)
	else if arr[0] == 'delete':
        	if arr[2] in locationMap:
            		locationMap.pop(arr[2])
            		np.save("dictionary.npy",locationMap)
    	 	else:
        		rospy.loginfo("Location not found : %s",arr[2])
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()
if __main__=='__main__':
	listener()
