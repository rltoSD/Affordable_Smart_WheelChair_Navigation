#!/bin/bash
#install mapping program
git clone https://github.com/appliedAI-Initiative/orb_slam_2_ros.git
catkin_make
#launch mapping program
roslaunch openni_launch openni.launch
roslaunch orb_slam2_ros orb_slam2_r200_rgbd.launch
rosrun rviz rviz -d rospack find ~/Desktop/ROS/mapping_settings_rviz/mapping_settings.rviz
#begin recording mapping program
rosbag record /orb_slam2_rgbd/map_points
