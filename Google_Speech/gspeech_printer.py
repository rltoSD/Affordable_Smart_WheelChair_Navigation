#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
        #grabs the transcript and confidence and stores them for later use
        transcript=data.data
        #prints out the information for user to see
        rospy.loginfo('transcript: {}'.format(transcript)
def main():
        #create a new node
        rospy.init_node('GSPEECH_INPUT_INFORMATION')
        #grabs the information for transcript and confidence
        rospy.Subscriber("chatter", String, callback)
        rospy.spin()
if __name__=='__main__':
        main()
