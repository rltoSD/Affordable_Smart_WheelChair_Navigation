#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from alexa_msgs.msgs import move_msg

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
           
            array = locationMap[arr[2]]
            #stores information into that message
            msg.x= array[0]
            msg.y= array[1]
            msg.z= array[2]
            msg.ax= array[3]
            msg.ax= array[4]
            msg.ax= array[5]

            #publishes to the topic
            pub1.publish(msg)
            r.sleep()
        else:
            rospy.loginfo("Location not found : %s",arr[2])

    #if command wants to set new location
    else if arr[0] == 'mark':
        #check that its not already marked
        if arr[4] in locationMap:
            rospy.loginfo("Location %s already marked",arr[4])
        else:
            arrOdometry = [data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.position.z
                          data.twist.twist.angular.x, data.twist.twist.angular.y, data.twist.twist.angular.z]
            locationMap[arr[4]] = arrOdometry
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
