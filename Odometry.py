#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def callback(data):
        #subscribes and grabs x,y,z position for Odometry
        x=data.pose.pose.position.x
        y=data.pose.pose.position.y
        z=data.pose.pose.position.z
        #subscribes and gets orientation z,x,y,w data for Odometry
        orientation_x=data.pose.pose.orientation.x
        orientation_y=data.pose.pose.orientation.y
        orientation_w=data.pose.pose.orientation.w
        orientation_z=data.pose.pose.orientation.z
        #subscribes and gets linear data        
        linear_x=data.twist.twist.linear.x
        linear_y=data.twist.twist.linear.y
        linear_z=data.twist.twist.linear.z
        #subscribes and gets angular data
        angular_x=data.twist.twist.angular.x
        angular_y=data.twist.twist.angular.y
        angular_z=data.twist.twist.angular.z
        #prints it to terminal
        rospy.loginfo('x: {}, y: {}, z {}'.format(x,y,z))
        rospy.loginfo('orientation_x: {}, orientation_y: {}, orientation_w {}, orientation_z {}'.format(orientation_x,orientation_y,orientation_w,orientation_z))
        rospy.loginfo('linear_x: {}, linear_y: {}, linear_z {}'.format(linear_x,linear_y,linear_z))
        rospy.loginfo('angular_x: {}, angular_y: {}, angular_z {}'.format(angular_x,angular_y,angular_z))
def main():
        #create a new node
        rospy.init_node('Odometry_Node_Information')
        #subscribe to topic
        rospy.Subscriber("/odom", Odometry, callback)
        rospy.spin()
if __name__== '__main__':
        main() 


