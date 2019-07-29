#!/bin/bash
#installation of ydlidar
cd 
mkdir catkin_ws
mkdir catkin_ws/src
cd catkin_ws/src
git clone https://github.com/EAIBOT/ydlidar
cd ..
catkin_make
roscd ydlidar/startup
sudo chmod 777./*
sudo sh initenv.sh
cd
source catkin_ws/devel/setup.bash
#installation of kobuki
cd
sudo apt-get install ros-kinetic-kobuki ros-kinetic-kobuki-core
sudo usermod -a -G dialout $USER
rosrun kobuki_ftdi create_udev_rules
