
import code
from email import message
from flask import Blueprint, redirect,render_template,flash,request, session, url_for
from werkzeug.utils import secure_filename
import os

from zmq import ROUTER
from database_operations import dbOperation
import datetime;

users = Blueprint('users', __name__)


@users.route('/landing', methods=['GET','POST'])
def landing():
    project_added=''
    try:
        
        
        target = os.path.join("data_upload_folder")
        if not os.path.isdir(target):
            os.makedirs(target)
        if request.method == "POST":

            # from_dashboard = request.args['message']
            if(session['from_dashboard']):
                print("oh yesss from dashboard")
                return render_template("landing.html", username = session['username'])
            else:
                ct = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                if 'file' not in request.files:
                    print('file not selected')
                file = request.files['file']
                filename = file.filename
                if filename == '':
                    print('filenmae is empty')
                
                
                
                
                file.save(os.path.join("data_upload_folder", filename))
                session['filename'] = os.path.join("data_upload_folder", filename)
                print(session['filename'])

                # DB project details insertion part
                
                
                
                user_first_name = session['username'].split(',')[0]
                user_last_name = session['username'].split(',')[1]
                user_email  = session['email']
                print(user_email)
                user_project_name = request.form.get("inputprojectName")
                print(user_project_name)
                user_project_created_on = ct
                user_project_last_updated_on = ct
                user_project_status='ACTIVE'
                
                db_operation = dbOperation()

                # get_project_details = db_operation.getProjectDetails(user_first_name,user_last_name,user_project_name)



                save_project_details = db_operation.initialProjectCheckpoint(user_first_name,user_last_name,user_email, user_project_name, user_project_created_on, user_project_last_updated_on, user_project_status)
            
                print(save_project_details)
                if (save_project_details):
                    get_project_details=db_operation.getProjectDetails(user_first_name,user_last_name,user_email)
                    # ,user_project_name)
                    print(get_project_details)
                    for rows in get_project_details:
                        print(rows)
                    flash('Project details save successfully')
                    print('data inserted')
                    return render_template("landing.html", username = session['username'])
                    
                else :
                    flash('Project details cant be saved')
                    return render_template('homepage.html')
            
        else:
            
            return render_template("landing.html", username = session['username'])
           
    except Exception as e:
        print(e)

# @users.route('/uploadtest', methods=['POST','GET'])
# def upload():
    
#     target = os.path.join("data_upload_folder")
#     if not os.path.isdir(target):
#         os.makedirs(target)
#     if request.method == 'POST':
#         # print(request.form)
#         # print(request.files['profile'].filename)
        
#         if 'file' not in request.files:
#             print('file not selected')
#         file = request.files['file']
#         filename = file.filename
#         if filename == '':
#             print('filenmae is empty')

#         file.save(os.path.join("data_upload_folder", filename))


#     return render_template("file_upload.html")
# @users.route('/landing', methods=['POST','GET'])
# def landing():
#     return render_template("landing.html")

@users.route('/new-project', methods= ['POST','GET'])
def new_project():

    return render_template("newproject.html")


@users.route('/dashboard', methods= ['POST','GET'])
def dashboard():

    get_project_details=()
    project_added=''
    try:
        
    
        # if request.method == 'POST':
           
           
            user_email = session['email']
            # user_password = request.form.get('pass')
            user_login_check = dbOperation()
            # user_validation = user_login_check.validateUser(user_email,user_password)
            # getUsername = user_login_check.getUserName(user_email,user_password)
            # print(getUsername)
            
            if user_email:
                # return redirect(url_for('main.check'))


                
                
                

                get_project_details=user_login_check.getProjectDetails(session['username'].split(',')[0],session['username'].split(',')[1], user_email)
                print(get_project_details)
                for rows in get_project_details:
                    print(rows)
                return render_template('dashboard.html', username = session['username'], rows=get_project_details)
            else:
                print(session['username'])
                flash('Login failed')
                return redirect(url_for("main.login"))
                #return render_template('login.html')
           
        # else:
        #     project_added = request.form.get('todo')
        #     print(project_added)
        #     if(project_added == 'project_added'):
        #         print('hello')
        #         return render_template("homepage.html",username=session['username'], rows=get_project_details)
        #     return render_template("newproject.html",username=session['username'], rows=get_project_details)
        #     return 'this is bullshit'
        # return render_template('homepage.html', username = getUsername)
    except Exception as e:
        print(e)
        return e


@users.route('/landings', methods=['POST','GET'])
def from_dashboard():
    # return render_template("landing.html")
    session['from_dashboard'] = True
    return redirect(url_for("users.landing"), code=307)
    