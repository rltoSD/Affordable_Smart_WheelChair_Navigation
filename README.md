# SmartWheelChairROS

Instructions to get the Subscriber node scripts to work with embedded

sudo chmod 777 /opt/ros/kinetic/share/rosserial_python/

sudo apt update && sudo apt install ros-kinetic-rosserial-server

source <ws>/install/setup.bash

osrun rosserial_python serial_node.py /dev/ttyACM0

sudo chmod 666 /dev/ttyACM0 

rostopic echo odom

rosrun rosserial_python insert_script_name_here.py

do rostopic list to find the desired topic node 
