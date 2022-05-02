# It creates a class called application_operations.
from multiprocessing.reduction import duplicate
from flask import Blueprint, redirect,render_template,flash,request, session, url_for
import pandas  as pd
from pyparsing import col
from application_logging.logger import App_Logger

class application_operations:

   # dataset=''

   def __init__(self):
      self.logger = App_Logger()
      
        

   def import_csv(self,filename):
      self.filename=filename
      self.dataset = pd.read_csv(filename)

   def shape(self):
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