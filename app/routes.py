from app import app
from flask import render_template

@app.route('/')
def index():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'mango', 'blueberry']
    return render_template('index.html', name='Brian', fruits=fruits)

@app.route('/posts')
def posts():
    return 'These are the posts!'

@app.route('/signup')
def signup():
    return render_template('signup.html')