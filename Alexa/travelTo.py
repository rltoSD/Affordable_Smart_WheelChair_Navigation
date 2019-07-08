import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.mgs import Point, Twist
from math import atan2

x = 0.0 
y = 0.0
theta = 0.0 

#set the goal you want to reach
#will add subscriber to take this from user input
goal = Point()
goal.x = 0.0 
goal.y = 0.0

def newOdom(msg):
    global x
    global y
    global theta

    #set x and y valued to those we get from odometry
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    #get orientation values
    rot_q = msg.pose.pose.orientation
    (roll,pitch,theta) = euler_from_quaternion ([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

def setGoal(msg)
    #i dont know if i did this part correctly since its a point
    global goal
    goal.x = msg.x
    goal.y = msg.y

rospy.init_node("speed_controller")

#sub to Odometry info
sub = rospy.Subscriber("/odom", Odometry, newOdom)
#publish movement to be made
pub = rospy.Publisher("/cmd_vel", Twist,queue_size = 1)

#subto desired position
move = rospy.Subscriber("MoveTopic", move_msg, setGoal)

#controls speed
speed = Twist()

r = rospy.Rate(4)

abool = True

while abool:
    #to calculate angle
    inc_x = goal.x - x
    inc_y = goal.y - y
    
    #Stop condition for when you have reached goal
    if inc_x == 0 and inc_y == 0:
        abool = False
        continue    

    #calculate angle to turn in order to     
    angle_to_goal = atan2(inc_y, inc_x)

    #should point the chair in the right direction
    if abs(angle_to_goal - theta) > 0.1:
        speed.linear.x = 0.0
        speed.angular.z = 0.3
    #once its there it should go forward
    else:
        speed.linear.x = 0.5
        speed.angular.z = 0.0
    

    pub.publish(speed)
    r.sleep()


