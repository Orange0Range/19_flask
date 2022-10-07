from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hey!'

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def welcomeHome():
    return 'welcome home'

@app.route('/welcome/back')
def welcomeBack():
    return 'welcome back'