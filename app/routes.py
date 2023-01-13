from app import app
from flask import render_template, redirect, url_for, flash, request
from app.forms import SignUpForm, LoginForm, PostForm
from app.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

# @app.route('/posts')
# def posts():
#     return 'These are the posts!'

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

@app.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        print(title, body, current_user)
        new_post = Post(title=title, body=body, user_id=current_user.id)
        flash(f"{new_post.title} has been created", 'success')
        return redirect(url_for('index'))
    return render_template('create-post.html', form = form)

@app.route('/posts/<int:post_id>')
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    if not post:
        flash('No such post', "waning")
    return render_template('post.html', post=post)

@app.route('/posts/<post_id>/edit', methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if not post:
        flash('No such post', "waning")
        return redirect(url_for('index'))
    if post.author != current_user:
        flash("cant edit posts you don't own", 'warning')
        return redirect(url_for('index'))
    form = PostForm()
    if request.method == 'GET':
        form.title.data = post.title
        form.body.data = post.body
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        print(title, body)
        # post.update_post()
        # return redirect(url_for)
    return render_template('edit_post.html', post=post, form=form)