from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from application_logging.logger import App_Logger

class connect_to_DB:
    def __init__(self):
        pass

    def db_connection(self):
        try:
            cloud_config= {
                'secure_connect_bundle': 'secure-connect-onlineeda.zip'
            }
            auth_provider = PlainTextAuthProvider('JpuZaXAKUbcvezUPigAofrwp', 'iU50rwbZ+fJQqFRjB9H.8wXFl3X54o0C1A.1kEEofB1PXvISBZ15Z8Q43Q3ASWcC7I.9SETYr,b,7CQiwKn7zdzWdiq6ZmfiQpCO+ikf.WbyZ2wS135joqFA_r14uPQN')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            return session
        except ConnectionError:
            file = open("Logs/DatabaseConnectionLog.txt",'a+')
            self.logger.log(file,"Error while connecting to the database")
            file.close()