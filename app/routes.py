from flask import render_template, redirect, url_for, flash, request, jsonify
from app import app, db, bcrypt, login_manager
from app.forms import RegistrationForm, LoginForm
from app.models import User, Journal, TestResults
from flask_login import login_user, logout_user, login_required, current_user


from app.chatbot import get_bot_response


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:  
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:  
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out!', 'info')
    return redirect(url_for('home'))


@app.route('/chat', methods=['GET', 'POST'])
@login_required  
def chat():
    if request.method == 'POST':
        user_message = request.json.get('message') 
        if not user_message:
            return jsonify(error='No message provided'), 400 

        bot_response = get_bot_response(user_message) 
        return jsonify(reply=bot_response)  
    return render_template('chat.html')


@app.route('/sos')
@login_required  
def sos():
    return render_template('sos.html')
