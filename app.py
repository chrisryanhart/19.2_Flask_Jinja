from flask import Flask, request, render_template
from stories import *

app = Flask(__name__)
# app.config['SECRET_KEY'] = "oh-so-secret"

@app.route('/')
def story_type():
    stories = story.get_words()

    return render_template("form.html", my_Story=stories)



@app.route('/madlib')
def madlib():
    story_dict = {}

    for word in story.get_words():
        story_dict[word] = request.args[word]
    print(story_dict)

    madlib = story.generate(story_dict)

    return render_template('madlib.html', my_madlib=madlib)


