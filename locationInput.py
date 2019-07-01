#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from move_topic.msg import float64

def callback(data):
    #try to get our dictionary with locations and coordinates
    try:
        #load the dictionary or create
        locationMap = np.load("dictionary.npy")
    #handle if there is no saved dictionary
    except FileNotFoundError:
        #make expandable hashtable
        new_dict = dict()
        np.save("dictionary.npy",new_dict)
        locationMap = np.load("dictionary.npy")

    #seperate string sections to get type of command
    arr = data.data.split(" ")

    #if the string starts with go
    if(arr[0] == 'go')
        #check that the location is marked on map
        if arr[2] in locationMap
            #publish location to be read by SLAM
            pub1 = rospy.Publisher('MoveTopic',float64,queue_size = 1)
            r = rospy.Rate(1)
            msg=move_topic()
            msg.x=locationMap[data.data[0]]
            msg.y=locationMap[data.data[1]]
            msg.z=locationMap[data.data[2]]
            pub1.publish(msg)
            r.sleep()
        else:
            rospy.loginfo("Location not found : %s",arr[2])

    #if command wants to set new location
    else if(arr[0] == 'mark')
        #check that its not already marked
        if arr[2] in locationMap
            rospy.loginfo("Locatio %s already marked",arr[2])
        else:
            arrOdometry = [data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.position.z]
            locationMap[arr[2]] = arrOdometry

    #if command is to delete a saved location
    else if(arr[0] == 'delete')
        if arr[2] in locationMap
            del locationMap[arr2]
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
