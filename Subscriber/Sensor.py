#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
#callback to grab topic data
def callback(data):
        #grabs and stores sensor data from the Float64MultiArray Topic
        sensor_one=data.data[0]
        sensor_two=data.data[1]
        sensor_three=data.data[2]
        sensor_four=data.data[3]
        sensor_five=data.data[4]
        sensor_six=data.data[5]
        sensor_seven=data.data[6]
        sensor_eight=data.data[7]
        sensor_nine=data.data[8]
        sensor_ten=data.data[9]
        sensor_eleven=data.data[10]
        sensor_twelve=data.data[11]
        #prints data to terminal
        rospy.loginfo('sensor_1: {}'.format(sensor_one))
        rospy.loginfo('sensor_2: {}'.format(sensor_two))
        rospy.loginfo('sensor_3: {}'.format(sensor_three))
        rospy.loginfo('sensor_4: {}'.format(sensor_four)
        rospy.loginfo('sensor_5: {}'.format(sensor_five))
        rospy.loginfo('sensor_6: {}'.format(sensor_six))
        rospy.loginfo('sensor_7: {}'.format(sensor_seven))
        rospy.loginfo('sensor_8: {}'.format(sensor_eight))
        rospy.loginfo('sensor_9: {}'.format(sensor_nine))
        rospy.loginfo('sensor_10: {}'.format(sensor_ten))
        rospy.loginfo('sensor_11: {}'.format(sensor_eleven))
        rospy.loginfo('sensor_12: {}'.format(sensor_twelve))
def main():
        #new node
        rospy.init_node('TFS_Information')
        #subscribes to "tof_sensor" topic
        rospy.subscriber("/tof_sensor", Float64MultiArray, callback)
        rospy.spin()
if __name__== '__main__':
        main()
