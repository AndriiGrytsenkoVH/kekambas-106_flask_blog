from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm

@app.route('/')
def index():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'mango', 'blueberry']
    return render_template('index.html', name='Brian', fruits=fruits)

@app.route('/posts')
def posts():
    return 'These are the posts!'

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUpForm()
    print(form.data)
    if form.validate_on_submit():
        print('From Submitter and Validated')
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        if username == 'bs':
            flash('The user already exists', 'danger')
            return render_template('signup.html', form=form)
        flash('Thank you for signing up!', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)