from asyncio.log import logger
from cmath import log
from json.tool import main
import logging
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from application_logging.logger import App_Logger


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
                print(row[0])
                file = open("Logs/DatabaseConnectionLog.txt",'a+')
                self.logger.log(file,"DB connection established successfully")
                file.close()
            
        except ConnectionError:
            file = open("Logs/DatabaseConnectionLog.txt",'a+')
            self.logger.log(file,"Error while connecting to the database")
            file.close()
        return row


# if __name__ == '__main__':
#     logging.info('Database connected')