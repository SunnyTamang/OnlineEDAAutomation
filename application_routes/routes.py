
from dataclasses import dataclass
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
    print(session['filename'])
    return render_template("overview.html", shape=shape, data_stats=dataset_stats, variable_type_and_count=variable_type_and_count, zip=zip)

@application.route("/column-wise-details")
def column_wise_details():

    application_process= application_operations()
    application_process.import_csv(session['filename'])
    count_check = application_process.get_column_wise_counts()
    desc_columns, describe = application_process.get_basic_descriptive_analysis()
    return render_template("column_wise_details.html",zip=zip, count_check=count_check,  desc_columns=desc_columns,  describe=describe)

@application.route("/correlations")
def correlation():
    
    return render_template("correlation.html" )

# @application.route("/visualise")
# def plot_png():
      
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = np.random.rand(100)
#     ys = np.random.rand(100)
#     axis.plot(xs, ys)
#     output = io.BytesIO()
#     fig.savefig(output)
#     output.seek(0)
#     FigureCanvas(fig).print_png(output)
#     return send_file(output, mimetype='image/png')


@application.route('/pearson')
def plot_pearson_heatmap():
   
    # application_process=application_operations()
    # dataset = application_process.return_dataframe(session['filename'])
    # fig = plt.figure(figsize=(8,8))
    # plt.title("Heatmap of Pearson's Correlation", fontsize = 20) # title with fontsize 20
    # plt.xlabel('Years', fontsize = 5) # x-axis label with fontsize 15
    # plt.ylabel('Monthes', fontsize = 5) # y-axis label with fontsize 15
    # print(session['filename'])
    # sns.heatmap(dataset.corr('pearson'), cmap="Blues", annot=True)
    # canvas = FigureCanvas(fig)
    # img= io.BytesIO()
    # fig.savefig(img)
    # img.seek(0)
    # return send_file(img, mimetype='image/png')

    application_process = application_operations()
    application_process.import_csv(session['filename'])
    return application_process.pearson_correlation()

@application.route('/spearman')
def plot_spearman_heatmap():
    application_process = application_operations()
    application_process.import_csv(session['filename'])
    return application_process.spearman_correlation()

# @application.route('/kendall')
# def plot_kendall_heatmap():
#     application_process = application_operations()
#     application_process.import_csv(session['filename'])
#     return application_process.kendall_correlation()


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
    