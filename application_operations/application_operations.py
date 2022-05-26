# It creates a class called application_operations.
from multiprocessing.reduction import duplicate
from turtle import width
from flask import Blueprint, redirect,render_template,flash,request, session, url_for, Response,send_file
from matplotlib import cm
import matplotlib
matplotlib.use('Agg')
import pandas  as pd
import numpy as np
from pyparsing import col
from application_logging.logger import App_Logger
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import matplotlib.pyplot as plt 
import seaborn as sns

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# fig,ax  = plt.subplots(figsize=(6,6))

class application_operations:

   # dataset=''

   def __init__(self):
      self.logger = App_Logger()
      
        

   def import_csv(self,filename):
      self.filename=filename
      self.dataset = pd.read_csv(filename)

   def return_dataframe(self,filename):
      self.filename=filename
      self.dataset = pd.read_csv(filename)
      return self.dataset

   def shape(self):
      print(self.dataset.shape, session['filename'])
      return self.dataset.shape

   
   def dataset_statistics(self):
      missing_count=0
      duplicate_count=0
      dataset_stats=[]
      num_of_var = len(self.dataset.dtypes)
      num_of_observation = len(self.dataset)
      for column in self.dataset.columns:
         if len(self.dataset[column].isnull().unique()) > 1:
            missing_count += 1
         if len(self.dataset[column].duplicated().unique()):
            duplicate_count += 1
      dataset_stats.append(num_of_var)
      dataset_stats.append(num_of_observation)
      dataset_stats.append(missing_count)
      dataset_stats.append(duplicate_count)
      return dataset_stats

   def variable_types(self):
      check=self.dataset.dtypes.value_counts()
      print(check)
      print(self.dataset.dtypes)
      print(check.keys())
      type_and_count = { k:v for (k,v) in zip(check.keys(), check.values) }
      print(type_and_count)
      return type_and_count


   def get_column_wise_counts(self):
      count_check={k:v for (k,v) in zip(self.dataset.count().keys(),self.dataset.count().values)}
      return count_check


   def get_basic_descriptive_analysis(self):
      
      describe_columns=self.dataset.describe().columns
      
      describe = self.dataset.describe()
     
      return  describe_columns, describe


   # def plot_png(self):
      
   #    fig = Figure()
   #    axis = fig.add_subplot(1, 1, 1)
   #    xs = np.random.rand(100)
   #    ys = np.random.rand(100)
   #    axis.plot(xs, ys)
   #    output = io.BytesIO()
   #    FigureCanvas(fig).print_png(output)
   #    return Response(output.getvalue(), mimetype='image/png')

   def pearson_correlation(self):
      try:
         data1 = self.dataset
         
         fig = plt.figure(figsize=(8,8))
         
         plt.title(f"Heatmap of Pearson's Correlation", fontsize = 20) # title with fontsize 20
         # plt.tight_layout()
         # plt.figure()
         sns.heatmap(data1.corr('pearson'), cmap="Blues", annot=True)
         canvas = FigureCanvas(fig)
         img1= io.BytesIO()
         fig.savefig(img1)
         # plt.cla()
         # plt.clf()
         # plt.close(fig)
         img1.seek(0)
         
         return send_file(img1, mimetype='image/png')
      except Exception as e:
         print(e)
      
   def spearman_correlation(self):
      try:
         data2 = self.dataset
         
         fig2 = plt.figure(figsize=(8,8))
         plt.title(f"Heatmap of Spearman's Correlation", fontsize = 20) # title with fontsize 20
         # plt.tight_layout()
         # plt.figure()
         sns.heatmap(data2.corr('spearman'), cmap="Blues", annot=True)
         canvas = FigureCanvas(fig2)
         img2= io.BytesIO()
         fig2.savefig(img2)
         # plt.cla()
         # plt.clf()
         # plt.close(fig2)
         img2.seek(0)
         return send_file(img2, mimetype='image/png')
      except Exception as e:
         print(e)
   
   def kendall_correlation(self):
      data3 = self.dataset
      
      fig3 = plt.figure(figsize=(8,8))
      plt.title(f"Heatmap of Kendall's Correlation", fontsize = 20) # title with fontsize 20
      # plt.tight_layout()
      # plt.figure()
      sns.heatmap(data3.corr('kendall'), cmap="Blues", annot=True)
      canvas = FigureCanvas(fig3)
      img3= io.BytesIO()
      fig3.savefig(img3)
      # plt.cla()
      # plt.clf()
      # plt.close(fig3)
      # plt.cla()
      img3.seek(0)
      return send_file(img3, mimetype='image/png')

   def nullity_matrix(self):
      data = self.dataset
      null_dict = {}
      for key, value in data.items():
         # if value.dtype == 'int64' or value.dtype =='float64':
         null_dict[key] = data[key].count()
      new_data=pd.Series(null_dict)
      fig=plt.figure(figsize=(15,8))
      plt.title(f"Nullity matrix", fontsize = 20)
      ax =sns.barplot(x=new_data.index, y=new_data.values, palette='summer')
   
   
      for i in ax.containers:
         ax.bar_label(i,)
      # plt.bar(range(len(new_data)), new_data.values, align='center')
      # plt.xticks(range(len(new_data)), new_data.index.values, size='small')
      canvas = FigureCanvas(fig)
      img= io.BytesIO()
      fig.savefig(img)
      # plt.cla()
      img.seek(0)
      return send_file(img, mimetype='image/png')


   def dataset_check(self):
      data = self.dataset
      column_names = [key for key in data.head(10).keys()]
      print(column_names)
      print(len(data.head(10).keys()))
      return data.head(10).keys(), data.head(10).values, data.tail(10).values