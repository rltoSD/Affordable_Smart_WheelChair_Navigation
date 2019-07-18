#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import String
from nav_msgs.msg import Odometry

#global variables for storage
x = 0.0 
y = 0.0 
z = 0.0 
#publisher to publish Odometry information to Odometry topic
pub = rospy.Publisher('/newOdom', Odometry, queue_size = 1)

#method to initialize global variables
def callbackOdom(data):
        global x
        global y
        global z
        #accesses embedded's odometry topic to get x,y,z
        x = data.pose.pose.position.x
        y = data.pose.pose.position.y   
        z = data.pose.pose.position.z   

#method to make use of the string
def callbackString(data):
        #loads the dictionary for stored locations or locations to be stored
        location = np.load("Dictionary.npy").item()
        text = ""
        textArr = []
        #grabs the text from the ros chatter topic and lowercases it
        text = data.data
        text = text.lower()
        #initialize to an array for easy access of each word
        textArr = text.split(" ")
        
        #if uttterance is longer than 3 words
        if len(textArr) > 3:
                i=3
                #loops through the array and combines everything after index 3
                while i < len(textArr):
                        textArr[2] = textArr[2] + textArr[i]
                        i += 1
        
        #edge case for sentences longer than 3 words
        if len(textArr) < 3:
                print 'Length of command not 3'
        #detects if the command is go
        elif textArr[0] == 'go':
                #checks if the location is in the dictionary
                if textArr[2] in location:
                        print "going to location " + textArr[2]
                        #sets the array stored in location to array
                        array = location[textArr[2]]
                        #grabs location data x,y,z to publish to newOdom topic
                        newOdom.pose.pose.position.x = array[0]
                        newOdom.pose.pose.position.y = array[1]
                        newOdom.pose.pose.position.z = array[2]
                        pub.publish(newOdom)
                else:
                        print "Location not in Dictionary"
        #handles marking locations
        elif textArr[0] == 'mark':
                if textArr[2] in location:
                        print "Location already marked"
                else:
                        print "marking location " + textArr[2]
                        #stores current location to arrOdom
                        arrOdom = [x,y,z]
                        #stores it in location
                        location[arr[2]] = arrOdom
                        #saves location to numpy for future use
                        np.save("Dictionary.npy", location)
        #handles removing a location
        elif textArr[0] == 'remove':
                #checks if location is in the dictionary
                if textArr[2] in location:
                        #removes it
                        location.pop(textArr[2])
                        #saves again
                        np.save("Dictionary.npy", locationMap)
                else:
                        print "Location not found"

def listener():
        #creates a new listener node
        rospy.init_node('handler', anonymous=True)
        #subscribes to topic
        rospy.Subscriber("/odom", Odometry, callbackOdom)
        rospy.Subscriber("chatter", String, callbackString)
        rospy.spin()

if __name__ == '__main__':
        listener()
