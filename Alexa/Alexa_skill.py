from flask import Flask
from flask_ask import Ask, statement, question, session
from std_msgs.msg import int64
import json
import requests
import time
import unidecode
import rospy

app = Flask (__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
input = 0.0
@ask.launch
def welcome():
	welcome_msg = render_template('Where do you want to go?')
	return question(welcome_msg)

@ask.intent("AnswerIntent", convert={'first': int})
def movement(first):
	global input
	input = first
	text = "The location is {}".format(input) 			
	return statement(text)
def talker()
	rospy.Publisher('chatter', int64, queue_size=1)
	rospy.init_node('input', anonymous=True)
	while not rospy.is_shutdown():
		rospy.loginfo(input)
		pub.publish(input)
		rate.sleep()
if __name__ == '__main__':
    app.run(debug=True)
    talker()
