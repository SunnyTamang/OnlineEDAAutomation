from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def login():
    return render_template('login.html')

@main.route('/sign-up')
def signup():
    return render_template('signup.html')