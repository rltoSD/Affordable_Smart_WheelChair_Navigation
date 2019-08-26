#include <ros/ros.h>
#include <geometry_msgs/PoseArray.h>
#include <std_msgs/String.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <gmapping_navigation/mark_location.h>

//this code is to create a Subscriber/ServiceServer to pair the user input name and current pose to save into a txt file

geometry_msgs::Pose current; 

//the subscriber callback function, to get the current pose from pose array
void getLocation(const geometry_msgs::PoseArray msg)
{
	float position_x = 0.0, position_y = 0.0, position_z = 0.0, orientation_x = 0.0, orientation_y = 0.0, orientation_z = 0.0, orientation_w = 0.0;
	
	//get the current pose by calculating the average value of pose array
	for(int i = 0; i < msg.poses.size(); i++)
	{
		position_x += msg.poses[i].position.x;
		position_y += msg.poses[i].position.y;
		position_z += msg.poses[i].position.z;
		orientation_x += msg.poses[i].orientation.x;
		orientation_y += msg.poses[i].orientation.y;
		orientation_z += msg.poses[i].orientation.z;
		orientation_w += msg.poses[i].orientation.w;
	}
	
	current.position.x = position_x / msg.poses.size();
	current.position.y = position_y / msg.poses.size();
	current.position.z = position_z / msg.poses.size();
	current.orientation.x = orientation_x / msg.poses.size();
	current.orientation.y = orientation_y / msg.poses.size();
	current.orientation.z = orientation_z / msg.poses.size();
	current.orientation.w = orientation_w / msg.poses.size();

	
}

//save the pose to txt file
bool save(gmapping_navigation::mark_location::Request &req,
	  gmapping_navigation::mark_location::Response &res)
{
	std::ofstream myfile;
	std::string location = req.location;
	myfile.open("location.txt", std::ios::app);
	
	myfile << location << " " << std::setprecision(6) << current.position.x << " " << current.position.y << " " << current.position.z << " " << current.orientation.x << " " << current.orientation.y << " " << current.orientation.z << " " << current.orientation.w << std::endl;
	myfile.close();
	res.success = true;
	return true;
}

int main(int argc, char** argv){
	//initialize a node 
	ros::init(argc, argv, "map_location");
	ros::NodeHandle n;
	//create subscriber
	ros::Subscriber sub = n.subscribe("particlecloud", 1000, getLocation);
	//create service server 
	ros::ServiceServer service = n.advertiseService("/save_location", save);
	ros::spin();

	return 0;
}



