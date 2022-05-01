from asyncio.log import logger
from cmath import log
from gettext import find
from json.tool import main
import logging
from tabnanny import process_tokens
from unicodedata import name
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from flask import flash, session 
from application_logging.logger import App_Logger
from DB_connect.db_connect import connect_to_DB
from cassandra.query import tuple_factory

# logging.basicConfig(filename="newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')

# logger = logging.getLogger(__name__)

# logger.setLevel(logging.INFO)





class  dbOperation:
    """
        This will be used for all the DB related operations

        Written By: Sunny Tamang
        Version: 1.0
        Revisions: None

    """

    def __init__(self):
        self.logger = App_Logger()
        self.connect_to_database = connect_to_DB()




    def dataBaseConnection(self):
        """
            Method Name: dataBaseConnection
            Description: This method creates the connection with the database
            Output: Connection to the DB
            On Failure: Raise ConnectionError

            Written By: Sunny Tamang
            Version: 1.0
            Revisions: None            
        """
        try:
            cloud_config= {
                'secure_connect_bundle': 'secure-connect-onlineeda.zip'
            }
            auth_provider = PlainTextAuthProvider('JpuZaXAKUbcvezUPigAofrwp', 'iU50rwbZ+fJQqFRjB9H.8wXFl3X54o0C1A.1kEEofB1PXvISBZ15Z8Q43Q3ASWcC7I.9SETYr,b,7CQiwKn7zdzWdiq6ZmfiQpCO+ikf.WbyZ2wS135joqFA_r14uPQN')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            # logger.info("Database connected")
            row = session.execute("select release_version from system.local;").one()
            if row:
                print(row)
                file = open("Logs/DatabaseConnectionLog.txt",'a+')
                self.logger.log(file,"DB connection established successfully")
                file.close()
            
        except ConnectionError:
            file = open("Logs/DatabaseConnectionLog.txt",'a+')
            self.logger.log(file,"Error while connecting to the database")
            file.close()
        # return row



    def registerUser(self, email, first_name, last_name, password):
        """
            Method Name: registerUser
            Description: This method register the user and save it in DB
            Output: Data insertion
            On Failure: Raise DB errors

            Written By: Sunny Tamang
            Version: 1.0
            Revisions: None   
        
        """
        # cloud_config= {
        #         'secure_connect_bundle': 'secure-connect-onlineeda.zip'
        #     }
        # auth_provider = PlainTextAuthProvider('JpuZaXAKUbcvezUPigAofrwp', 'iU50rwbZ+fJQqFRjB9H.8wXFl3X54o0C1A.1kEEofB1PXvISBZ15Z8Q43Q3ASWcC7I.9SETYr,b,7CQiwKn7zdzWdiq6ZmfiQpCO+ikf.WbyZ2wS135joqFA_r14uPQN')
        # cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        # session = cluster.connect()

        session = self.connect_to_database.db_connection()
        self.email = email
        self.first_name = first_name
        self.last_name  = last_name
        self.password = password
        
        try:
            CQLString = f"INSERT INTO users.t_sec_user_mst (id, email, firstname, lastname, password) VALUES (uuid(),'{self.email}', '{self.first_name}', '{self.last_name}', '{self.password}');"
            
            session.execute(CQLString)
            file = open("Logs/ApplicationLog.txt",'a+')
            self.logger.log(file,"User registration successfull")
            file.close()
            # if (data_inserted != null):
            #     flash('You were successfully logged in')
                 
        except Exception as e:
            file = open("Logs/ApplicationLog.txt",'a+')
            self.logger.log(file,e)
            file.close()
            return False
        finally:
            return True


    def validateUser(self, email, password):
        """
        It takes in email and password as parameters and checks if the user exists in the database. If
        the user exists, it returns True else it returns False
        
        :param email: The email address of the user
        :param password: The password for the user
        :return: A tuple of tuples.
        """
        

        # cloud_config= {
        #         'secure_connect_bundle': 'secure-connect-onlineeda.zip'
        #     }
        # auth_provider = PlainTextAuthProvider('JpuZaXAKUbcvezUPigAofrwp', 'iU50rwbZ+fJQqFRjB9H.8wXFl3X54o0C1A.1kEEofB1PXvISBZ15Z8Q43Q3ASWcC7I.9SETYr,b,7CQiwKn7zdzWdiq6ZmfiQpCO+ikf.WbyZ2wS135joqFA_r14uPQN')
        # cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        # session = cluster.connect()

        session = self.connect_to_database.db_connection()
        self.email = email
        self.password = password
        try:
            CQLString = f"SELECT EMAIL, PASSWORD from users.t_sec_user_mst where email = '{self.email}' and password = '{self.password}' allow filtering;"


            
            
            session.row_factory = tuple_factory
            rows = session.execute(CQLString).one()
            if rows:
                file = open("Logs/ApplicationLog.txt",'a+')
                self.logger.log(file,"User Found. Login Successful")
                file.close()
                return True
            else:
                file = open("Logs/ApplicationLog.txt",'a+')
                self.logger.log(file,"User not found. Login Failed")
                file.close()
                return False
            
        except Exception as e:
            file = open("Logs/ApplicationLog.txt",'a+')
            self.logger.log(file,e)
            file.close()
            return False


    def getUserName(self, email, password):
        """
        It takes an email and password as input and returns the firstname and lastname of the user
        
        :param email: user@gmail.com
        :param password: 'b.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ.ZQ
        :return: The name of the user.
        """
        session = self.connect_to_database.db_connection()
        self.email = email
        self.password = password
        name = ''
        try:
            CQLString = f"SELECT firstname, lastname from users.t_sec_user_mst where email = '{self.email}' and password = '{self.password}' allow filtering;"


            
            
            session.row_factory = tuple_factory
            rows = session.execute(CQLString).one()
            name = rows[0].capitalize() +","+ rows[1].capitalize()
                
            if rows:
                file = open("Logs/ApplicationLog.txt",'a+')
                self.logger.log(file,"User Found.")
                file.close()
                return name
            else:
                file = open("Logs/ApplicationLog.txt",'a+')
                self.logger.log(file,"User not found.")
                file.close()
                return ""
            
        except Exception as e:
            file = open("Logs/ApplicationLog.txt",'a+')
            self.logger.log(file,e)
            file.close()
            return name
            
        
    def initialProjectCheckpoint(self, first_name, last_name, user_email, project_name, created_on, last_updated_on, project_status):
        """
        It inserts a row into a table
        
        :param first_name: String
        :param last_name: "Doe"
        :param user_email: user@gmail.com
        :param project_name: "Test Project"
        :param created_on: 2020-02-20
        :param last_updated_on: 2020-02-20
        :param project_status: This is a string that can be either "active" or "inactive"
        :return: The return value is a boolean value.
        """
        session = self.connect_to_database.db_connection()
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.project_name = project_name
        # self.project_id = project_id
        self.created_on =  created_on
        self.last_updated_on = last_updated_on
        self.project_status = project_status
        
        try:
            CQLString = f"INSERT INTO users.user_project_names (first_name, last_name, user_email, project_name, proj_id, created_on, last_updated_on, project_status) VALUES ('{self.first_name}', '{self.last_name}', '{self.user_email}', '{self.project_name}', uuid(), '{self.created_on}', '{self.last_updated_on}', '{self.project_status}');"
            print(CQLString)
            session.execute(CQLString)
            file = open("Logs/ApplicationLog.txt",'a+')
            self.logger.log(file,"Project details added")
            file.close()
            return True

        except Exception as e:
            file = open("Logs/ApplicationLog.txt",'a+')
            self.logger.log(file,e)
            file.close()
            return False



    def getProjectDetails(self, first_name, last_name, user_email):
        """
        It takes in a first name, last name, and email address and returns a list of project names that
        the user has access to.
        
        :param first_name: "John"
        :param last_name: 'Smith'
        :param user_email: 'test@test.com'
        :return: A list of tuples.
        """
        session = self.connect_to_database.db_connection()
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        # self.project_name = project_name
        try:
            project_names=[]
            CQLString = f"SELECT project_name from users.user_project_names where first_name = '{self.first_name}' and last_name = '{self.last_name}' and user_email = '{self.user_email}' allow filtering;"


            
            print(CQLString)
            session.row_factory = tuple_factory
            rows = session.execute(CQLString)
            for row in rows:
                project_names.append(row[0])
            print(rows)
            if rows:
                file = open("Logs/ApplicationLog.txt",'a+')
                self.logger.log(file,"Project Found: " +len(rows))
                file.close()
                return tuple(rows)
            else:
                file = open("Logs/ApplicationLog.txt",'a+')
                self.logger.log(file,"No project found")
                file.close()
                return project_names
            
        except Exception as e:
            file = open("Logs/ApplicationLog.txt",'a+')
            self.logger.log(file,e)
            file.close()
            return False        
        # finally:
        #     return True


    def add_csv_data_to_DB():
        """
        This function adds data from a csv file to a database.
        """
        pass


# if __name__ == '__main__':
#     logging.info('Database connected')
