

# from crypt import methods

import re
from urllib.request import Request
from flask import Blueprint, redirect, render_template, request, flash, session, url_for
from database_operations import dbOperation

main = Blueprint('main', __name__)


@main.route('/', methods=['POST','GET'])
def login():
    session['from_dashboard'] = ""
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

@main.route('/home', methods=['POST','GET'])
def home():
    # form = login(request.form)
    # getUsername=''
    if session['from_dashboard'] == True:
        session['from_dashboard'] = False
    get_project_details=()
    project_added=''
   
    try:
        
    
        if request.method == 'POST':
           
           
            user_email = request.form.get('login_email')
            user_password = request.form.get('pass')
            user_login_check = dbOperation()
            user_validation = user_login_check.validateUser(user_email,user_password)
            # getUsername = user_login_check.getUserName(user_email,user_password)
            # print(getUsername)
            
            if user_validation:
                # return redirect(url_for('main.check'))


                
                
                getUsername = user_login_check.getUserName(user_email,user_password)
                session['username'] =  getUsername
                session['email'] = user_email

                get_project_details=user_login_check.getProjectDetails(session['username'].split(',')[0],session['username'].split(',')[1], user_email)
                print(get_project_details)
                for rows in get_project_details:
                    print(rows)
                return render_template('newproject.html', username = session['username'], rows=get_project_details)
            else:
                flash('Login failed')
                return redirect(url_for("main.login"))
                #return render_template('login.html')
           
        else:
            project_added = request.form.get('todo')
            print(project_added)
            if(project_added == 'project_added'):
                print('hello')
                return render_template("homepage.html",username=session['username'], rows=get_project_details)
            return render_template("newproject.html",username=session['username'], rows=get_project_details)
        #     return 'this is bullshit'
        # return render_template('homepage.html', username = getUsername)
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
