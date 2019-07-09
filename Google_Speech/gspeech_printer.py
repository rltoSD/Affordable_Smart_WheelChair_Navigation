#!/usr/bin/env python

import rospy
from gspeech_input_msg import input
from google.cloud import speech
from std_msgs.msg import String, Header

def callback(data):
        transcript=input.transcript
        confidence=input.confidence
        rospy.loginfo('transcript: {}, confidence{}'.format(transcript,confidence)
def main():
        rospy.init_node('GSPEECH_INPUT_INFORMATION')
        rospy.Subscriber("/input", input, callback)
        rospy.spin()
if __name__=='__main__':
        main()
