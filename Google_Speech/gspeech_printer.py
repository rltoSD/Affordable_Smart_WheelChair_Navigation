#!/usr/bin/env python

import rospy
from gspeech_input_msg import input
from google.cloud import speech
from std_msgs.msg import String, Header

def callback(data):
        #grabs the transcript and confidence and stores them for later use
        transcript=input.transcript
        confidence=input.confidence
        #prints out the information for user to see
        rospy.loginfo('transcript: {}, confidence{}'.format(transcript,confidence)
def main():
        #create a new node
        rospy.init_node('GSPEECH_INPUT_INFORMATION')
        #grabs the information for transcript and confidence
        rospy.Subscriber("/input", input, callback)
        rospy.spin()
if __name__=='__main__':
        main()
