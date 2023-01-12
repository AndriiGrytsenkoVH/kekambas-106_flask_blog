from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user

@app.route('/')
def index():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'mango', 'blueberry']
    return render_template('index.html', name='Brian', fruits=fruits)

@app.route('/posts')
def posts():
    return 'These are the posts!'

@app.route('/signup', methods=["GET", "POST"])
def signup():
    # Create an instance of the SignUpForm
    form = SignUpForm()
    # Check if a POST request AND data is valid
    if form.validate_on_submit():
        print('Form Submitted and Validated!')
        # Get data from the form
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        # Query our user table to see if there are any users with either username or email from form
        check_user = User.query.filter( (User.username == username) | (User.email == email) ).first()
        # If the query comes back with any results
        if check_user:
            # Flash message saying that a user with email/username already exists
            flash('A user with that email and/or username already exists.', 'danger')
            return redirect(url_for('signup'))
        # If check_user is empty, create a new record in the user table
        new_user = User(email=email, username=username, password=password)
        # Flash a success message
        flash(f'Thank you {new_user.username} for signing up!', 'success')
        # Redirect back to Home
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    # Check if a POST request AND data is valid
    if form.validate_on_submit():
        print('Form Validated!')
        # Get data from the form
        username = form.username.data
        password = form.password.data
        print(username, password)

        
        user = User.query.filter_by(username=username).first()
        # If the query comes back with any results
        if user is not None and user.check_password(password):
            login_user(user)
            flash(f'{user.username} is now logged in', 'warning')
            return redirect(url_for('index'))
        else:
            flash(f"Incorrect username or password","warning")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route("/logout")
# @login_required
def logout():
    logout_user()
    flash("You have been logged out","warning")
    return redirect(url_for('index'))
