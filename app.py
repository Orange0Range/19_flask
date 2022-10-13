from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello-hi'
debug = DebugToolbarExtension(app)

@app.route('/')
def home():

    words = story.prompts
    return render_template('home.html', story = story.prompts)

@app.route('/story')
def storyPage():
    response = {}
    for prompt in story.prompts:
        response[prompt] = request.args[prompt]
    
    print(story.generate(response))
    return render_template('story.html',yourStory = story.generate(response))
