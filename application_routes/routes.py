

from dataclasses import dataclass
from itertools import count
from pydoc import describe
from tkinter import Canvas
from turtle import shape
from graphviz import render
import pandas as pd
from flask import Blueprint, redirect,render_template,flash,request, send_file, session, url_for, Response
from werkzeug.utils import secure_filename
from application_operations.application_operations import application_operations
import os
import datetime;
from application_logging.logger import App_Logger
import matplotlib
matplotlib.use('Agg')
from collections import OrderedDict
# import matplotlib
# matplotlib.use('Agg')
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import io
# import seaborn as sns
# import matplotlib.pyplot as plt 
# import numpy as np
# import pandas as pd



application = Blueprint('application', __name__)



@application.route("/overview", methods=['GET','POST'])
def overview():
    application_process = application_operations()
    application_process.import_csv(session['filename'])
    shape = application_process.shape()
    dataset_stats = application_process.dataset_statistics()
    variable_type_and_count =application_process.variable_types()
    isRowDuplicate, duplicate_row_count = application_process.duplicate_row_check()
    isColDuplicate_byname= application_process.duplicate_column_check_byname()
    isColDuplicate_byvalue = application_process.duplicate_column_check_byvalue()
    column_data_types = application_process.column_data_types()
    
    if request.method=='POST':
        if request.form['customize'] == 'true':
            session['customConfig'] = request.form
        
            session['isCustom'] = 'true'
           
        else:
            # session['customConfig'] = request.form
        
            session['isCustom'] = 'false'
            

    session['customConfig'] = dict(reversed(list(session['customConfig'].items())))
    print(session['customConfig'])
    
    return render_template("overview.html", reversed=reversed,dict=dict, list=list, shape=shape, data_stats=dataset_stats, len=len, variable_type_and_count=variable_type_and_count, zip=zip,isCustom=session['isCustom'],isRowDuplicate=isRowDuplicate, duplicate_row_count=len(duplicate_row_count),isColDuplicate_byname=isColDuplicate_byname,isColDuplicate_byvalue=isColDuplicate_byvalue,column_data_types=column_data_types,customConfig=session['customConfig'] )

@application.route("/column-wise-details", methods=['POST','GET'])
def column_wise_details():

    application_process= application_operations()
    application_process.import_csv(session['filename'])
    count_check = application_process.get_column_wise_counts()
    desc_columns, describe = application_process.get_basic_descriptive_analysis()
    
    if request.method=='POST':
        if request.form['customize'] == 'true':
            session['customConfig'] = request.form
        
            session['isCustom'] = request.form['customize']

            print('when true: ',request.form)
        else:
            # session['customConfig'] = request.form
        
            session['isCustom'] = 'false'
            print('when false: ',request.form)
    
    session['customConfig'] = dict(reversed(list(session['customConfig'].items())))
     

    return render_template("column_wise_details.html",zip=zip, count_check=count_check,  desc_columns=desc_columns,  describe=describe, isCustom=session['isCustom'],customConfig=session['customConfig'])

@application.route("/correlations")
def correlation():  
    return render_template("correlation.html")


@application.route('/pearson')
def plot_pearson_heatmap():
   
   
    application_process = application_operations()
    application_process.import_csv(session['filename'])
    return application_process.pearson_correlation()

@application.route('/spearman')
def plot_spearman_heatmap():
    application_process = application_operations()
    application_process.import_csv(session['filename'])
    spear=application_process.spearman_correlation()
    if spear:
        print('this is done')
        spear_conf=True
    else:
        print('this is not done')
    return application_process.spearman_correlation()

@application.route('/kendall')
def plot_kendall_heatmap():
    application_process = application_operations()
    application_process.import_csv(session['filename'])
    return application_process.kendall_correlation()

@application.route('/mising-values')
def missing_values():
    application_process = application_operations()
    return render_template('missing_values.html')
    # return render_template('reports.html')

@application.route('/nullity-matrix')
def nullity_matrix():
    application_process = application_operations()
    application_process.import_csv(session['filename'])
    return application_process.nullity_matrix()


@application.route('/sample-dataset')
def dataset():
    application_process = application_operations()
    application_process.import_csv(session['filename'])
    column_names, head,tail = application_process.dataset_check()
    return render_template('dataset.html', column_names=column_names, head=head, tail=tail, zip=zip)
    

@application.route('/about', methods=['GET','POST'])
def about_us():
    return render_template('aboutus.html')


@application.route('/overview-post-customization', methods=['POST','GET'])
def overview_post_customization():
    if request.method =='POST':
        # clicked = request.values('data')
        # clicked = request.form['data']
        print(request.form)
        # application_process = application_operations()
        # application_process.import_csv(session['filename'])
        # shape = application_process.shape()
        # dataset_stats = application_process.dataset_statistics()
        # variable_type_and_count =application_process.variable_types()
    return render_template('/custom/overview_custom.html')