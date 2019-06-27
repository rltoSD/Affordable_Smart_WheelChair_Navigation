#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
from nav_msgs.msg import Odometry

def callback(data):

    try:
        #load the dictionary or create
        d1 = np.load("dictionary.npy")

    except FileNotFoundError:
        #make expandable hashtable
        new_dict = dict()
        np.save("dictionary.npy",new_dict)
        d1 = np.load("dictionary.npy")      

    #seperate string sections to get type of command
    arr = data.data.split(" ")
    
    if(arr[0] == 'go')
        if arr[2] in locationMap
            #publish to move
        else
            #do nothing

    else if(arr[0] == 'mark')
        if arr[2] in locationMap
	    arrOdometry = [data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.position.z]
            locationMap[arr[2]i] = arrOdometry
            #publish to map
        else
            #do nothing
    else if(arr[0] == 'delete')
        if arr[2] in locationMap
            del locationMap[arr2]
            #publish to removeMap

    #publish location to be read by      
    pub = rospy.Publisher('Move',String,queue_size = 2)
    p.publish()

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
