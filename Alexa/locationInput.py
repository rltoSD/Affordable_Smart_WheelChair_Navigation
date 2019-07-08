#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from alexa_msgs.msgs import move_msg

x = 0.0 
y = 0.0
z = 0.0 

def getOdom(data):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    
def callback(data):
    
    #load the dictionary assuming this file is already created
    locationMap = np.load("dictionary.npy").item()
    
    #seperate string sections to get type of command
    arr = data.data.split(" ")

    #if the string starts with go
    if arr[0] == 'go':
        #check that the location is marked on map
        if arr[2] in locationMap:
            #publish location to be read by SLAM
            #creates a node
            rospy.init_node("input_Node")
            #publishes
            pub1 = rospy.Publisher('MoveTopic',move_msg,queue_size = 1)
            r = rospy.Rate(1)
            #initializes a new move topic message
            msg=move_topic()
            #get location information from dictionary
            array = locationMap[arr[2]]
            msg.x= array[0]
            msg.y= array[1]
            msg.z= array[2]

            #publishes to the topic
            pub1.publish(msg)
            r.sleep()
        else:
            rospy.loginfo("Location not found : %s",arr[2])

    #if command wants to set new location
    else if arr[0] == 'mark':
        #check that its not already marked
        if arr[2] in locationMap:
            rospy.loginfo("Location %s already marked",arr[2])
        else:
            sub = rospy.Subscriber("/odom", Odometry,getOdom)
            #gets odometry information
            arrOdometry = [x,y,z]
            locationMap[arr[2]] = arrOdometry
            np.save("dictionary.npy",locationMap)

    #if command is to delete a saved location
    else if arr[0] == 'delete':
        if arr[2] in locationMap:
            locationMap.pop(arr[2])
            np.save("dictionary.npy",locationMap)
        else:
            rospy.loginfo("Location not found : %s",arr[2])

def listener():

     # In ROS, nodes are uniquely named. If two nodes with the same
     # name are launched, the previous one is kicked off. The
     # anonymous=True flag means that rospy will choose a unique
     # name for our 'listener' node so that multiple listeners can
     # run simultaneously.
     rospy.init_node('listener', anonymous=True)

     rospy.Subscriber("chatter", String, callback)

     # spin() simply keeps python from exiting until this node is stopped
     rospy.spin()

 if __name__ == '__main__':
     listener()
