import serial
import rospy
from std_msgs.msg import Float32

class StartState:
    def __init__(self):
        self.name = "start"
        self.ser = serial
        self.odometryExist = false
        self.scanExist = false
        self.serialExist = false

    def run(self):
        """
        Code to be executed when in start state
        """
        try:
                self.ser = serial.Serial('tty.usbmodem14101', 14101, timeout=1)
                if (ser.read()):
                        print 'serial open and Arduino connected'
                        self.serialExist = true
                else:
                        print 'serial closed and Arduino not connected'
                        ser.close()
        except serial.serialutil.SerialException:
                print 'exception'

        published_topics = rospy.get_published_topics()
        for (i, j) in published_topics:
                if i == "Odometry":
                        self.odometryExist = true
                if i == "scan":
                        self.scanExist = true

        if (self.serialExist and self.odometryExist and self.scanExist):
                pub = rospy.Publisher("start_mapping", Float32, queue_size=1)
                rate = rospy.Rate(10)
                pub.publish(1.0)
                rate.sleep()

        print("start_state::body")

    def next_state(self, data):
        # decompose the data tuple
        (start_mapping,
        start_logging,
        map_built,
        goal_received,goal_reached) = data

        if start_logging:
            return "logging"
        elif start_mapping:
            return "mapping"
        else:
            return self.name
