
from turtle import shape
import pandas as pd
from flask import Blueprint, redirect,render_template,flash,request, session, url_for
from werkzeug.utils import secure_filename
from application_operations.application_operations import application_operations
import os

import datetime;

application = Blueprint('application', __name__)


@application.route("/overview", methods=['GET','POST'])
def overview():
    application_process = application_operations()
    application_process.import_csv(session['filename'])
    shape = application_process.shape()
    dataset_stats = application_process.dataset_statistics()
    variable_type_and_count =application_process.variable_types()
    print(session['filename'])
    return render_template("overview.html", shape=shape, data_stats=dataset_stats, variable_type_and_count=variable_type_and_count, zip=zip)