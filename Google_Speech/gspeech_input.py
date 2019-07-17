#!/usr/bin/env python
import speech_recognition as sr
from std_msgs.msg import String
import rospy
text = ""
mic_name = ""
#Sample rate is how often values are recorded
#Initialize the recognizer
r = sr.Recognizer()
#generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()
#the following loop aims to set the device ID of the mic that
#we specifically want to use to avoid ambiguity.
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i 
print mic_list
#use the microphone as source for input. Here, we also specify
#which device ID to specifically look for incase the microphone
#is not working, an error will pop up saying "device_id undefined"
with sr.Microphone(device_index = device_id, sample_rate = 48000, chunk_size=1024 )as source:
    #wait for a second to let the recognizer adjust the
    #energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
    print "Where do you want to go?"
    #listens for the user's input
    audio = r.listen(source)

    try:
        global text
        text = r.recognize_google(audio)
        print text
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        rospy.loginfo(text)
        pub.publish(text)
        rate.sleep()
    #error occurs when google could not understand what was said

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("There is no internet connection; {0}".format(e))
