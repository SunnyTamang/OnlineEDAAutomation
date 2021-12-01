
from flask import Blueprint,render_template,flash,request

users = Blueprint('users', __name__)

@users.route('/login/', methods=['GET','POST'])
def login():
    return render_template("login.html")
    return '<p>Login</p>'