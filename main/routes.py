

# from crypt import methods

from urllib.request import Request
from flask import Blueprint, render_template, request, flash
from connect_database import dbOperation

main = Blueprint('main', __name__)


@main.route('/', methods=['POST','GET'])
def login():
    
    return render_template('login.html')

@main.route('/user-registration', methods=['POST', 'GET'])
def user_registration():
    try:
        
        if request.method == 'POST':
           
            user_email = request.form.get('reg_email')
            user_first_name = request.form.get('reg_firstname')
            user_last_name = request.form.get('reg_lastname')
            user_password = request.form.get('reg_pass')
            user_register = dbOperation()
            user_registered = user_register.registerUser(user_email,user_first_name,user_last_name,user_password)

            if (user_registered):
                flash('User registeration successful. Please click here to login')
                return render_template('signup.html')
                
            else :
                flash('Registration failed')
                return render_template('signup.html')
        else:
            return 'this is bullshit'
    except Exception as e:
        print(e)
        return e

@main.route('/sign-up', methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@main.route('/check', methods=['POST','GET'])
def check():
    # form = login(request.form)
    try:
        if request.method == 'POST':
           
            user_email = request.form.get('login_email')
            user_password = request.form.get('pass')
            
            
            
        else:
            return 'this is bullshit'
    except Exception as e:
        print(e)
        return e


@main.route('/check1', methods=['POST','GET'])
def check1():
    # form = login(request.form)
    try:
        if request.method == 'POST':
           
            print(request.form['reg_email'])
           
            # return request.form['reg_email']
            
            
        else:
            return 'this is bullshit'
    except Exception as e:
        print(e)
        return e