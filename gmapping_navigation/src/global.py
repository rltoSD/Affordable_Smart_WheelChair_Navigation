#! /usr/bin/env python

# the code is to call the "global_localization" service to initialize particleclouds in map
 
import rospy
from std_srvs.srv import Empty, EmptyRequest
import sys 

#initialize a service client node 
rospy.init_node('service_client')  

#wait untial the service server is up and running
rospy.wait_for_service('/global_localization') 

#call a service proxy
particleclouds_service = rospy.ServiceProxy('/global_localization', Empty)

msg = EmptyRequest()

result = particleclouds_service(msg)

print result
