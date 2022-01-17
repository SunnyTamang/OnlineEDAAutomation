

from crypt import methods
from urllib.request import Request
from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)


@main.route('/', methods=['POST','GET'])
def login():
    return render_template('login.html')

@main.route('/sign-up', methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@main.route('/check', methods=['POST','GET'])
def check():
    # form = login(request.form)
    try:
        if request.method == 'POST':
           
            print(request.form['login_email'])
           
            
            
            
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