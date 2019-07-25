#Instructions to get the ydlidar working
First, we need to source the setup.bash.
-source catkin_ws/devel/setup.bash
Afterwards, we can run the ydlidar to map
the room.
-roslaunch ydlidar all_nodes.launch
the reason why we use roslaunch instead
of rosrun is because of the fact that
roslaunch allows us to run the master node

#Instructions to get the kobuki working
roslaunch kobuki_node minimal.launch --screen                                                   
roslaunch kobuki_keyop safe_keyop.launch --screen                                                                                         
