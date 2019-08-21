#!/usr/bin/env python
import speech_recognition as sr
import os
from gtts import gTTS
#import rospy
#the following name is only used as an example
text = ""
mic_name = "MacBook Pro Microphone"
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

#method that will do text to speech and ask the user
#where they want to go
#@param value
#@return none
def textToSpeech(value):
    tts = gTTS(text='Where to', lang='en')
    #saves to mp3 so it can be used for speech
    tts.save("input.mp3")
    os.system("mpg321 input.mp3")
    
#use the microphone as source for input. Here, we also specify
#which device ID to specifically look for incase the microphone
#is not working, an error will pop up saying "device_id undefined"
with sr.Microphone(device_index = device_id, sample_rate = 48000,
                        chunk_size = 1024) as source:
    #setup thread
    t = threading.Thread(target=textToSpeech, args=(1,))
    #start thread in background
    t.start()
    #case in which there is ambient noise
    r.adjust_for_ambient_noise(source, duration = 1.7)
    print ("Where do you want to go?")
    #listens for the user's input
    audio = r.listen(source)

    try:
        #grabs the text of the user's speech
        text = r.recognize_google(audio)
        print (text)
        #creates a publisher node of string type
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        #rate of broadcast
        rate = rospy.Rate(10) # 10hz
        #while there rospy is not off
        while not rospy.is_shutdown():
           #prints it 
           rospy.loginfo(text)
           #publish user's speech information to chatter topic 
           pub.publish(text)
           rate.sleep()

    #error occurs when google could not understand what was said
    except sr.UnknownValueError:
        #text that is to be said
        tts = gTTS(text='Google Speech Recognition could not understand audio', lang='en')
        #save to a mp3 file for voice output
        tts.save("input.mp3")
        os.system("mpg321 input.mp3")
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        #text that is to be said
        tts = gTTS(text='There is no internet connection', lang='en')
        #save to a mp3 file for voice output
        tts.save("input.mp3")
        os.system("mpg321 input.mp3")
        print("There is no internet connection; {0}".format(e))
