#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

//the code is to send the twist message from "cmd_vel", which is publised by navigation node, to "mobile_base/commands/velocity", which makes robot to move 
float linearX, angularZ;

//sent the twist message to global variables
void chatterCallback(const geometry_msgs::Twist& msg)
{
  linearX = msg.linear.x;
  angularZ = msg.angular.z;
}

int main(int argc, char **argv)
{
  //initialize a subscriber node 
  ros::init(argc, argv, "listener");

  ros::NodeHandle n;

  //create a subscriber
  ros::Subscriber sub = n.subscribe("/cmd_vel", 1000, chatterCallback);

  //create a publisher
  ros::Publisher pub = n.advertise<geometry_msgs::Twist>("mobile_base/commands/velocity", 1000);

  ros::Rate rate(2);

  //run the publisher
  while(ros::ok()){
     geometry_msgs::Twist msg;
     msg.linear.x = linearX;
     msg.linear.y = 0.0;
     msg.linear.z = 0.0;
     msg.angular.x = 0.0;
     msg.angular.y = 0.0;
     msg.angular.z = angularZ;
    
     pub.publish(msg);

     rate.sleep();

     ros::spinOnce();
   }

  return 0;
}
