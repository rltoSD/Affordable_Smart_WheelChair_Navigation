from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask (__name__)
ask = Ask(app, "/navigate_input_voice")
input = 0.0

@app.route('/')
def homepage():
	return "hello"
@ask.launch
def welcome():
	welcome_msg = render_template('Where do you want to go?')
	return question(welcome_msg)

@ask.intent("Input", convert={'first': int})
def movement(first):
	global input
	input = first
	text = "The location is {}".format(input) 			
	return statement(text)
if __name__ == '__main__':
    app.run(debug=True)	
