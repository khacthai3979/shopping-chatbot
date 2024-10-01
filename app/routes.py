
from flask import render_template, redirect, url_for, flash
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Journal, TestResults
from flask_login import login_user, logout_user
from app.models import User
from app import login_manager
from flask import request, jsonify
from app import app
from app.chatbot import get_bot_response 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Get the JSON data sent by fetch
    user_message = data.get('message')  # Extract the user's message
    bot_response = get_bot_response(user_message)  # Get the bot's response

    # Return the bot's response as JSON
    return jsonify({'reply': bot_response})

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/chat', endpoint='chat_route_1')
def chat():
    return render_template('chat.html')

@app.route('/chat2', endpoint='chat_route_2')
def chat():
    return render_template('chat.html')


@app.route('/sos')
def sos():
    return render_template('sos.html')
