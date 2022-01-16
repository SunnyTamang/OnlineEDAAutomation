from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'secure-connect-onlineeda.zip'
}
auth_provider = PlainTextAuthProvider('JpuZaXAKUbcvezUPigAofrwp', 'iU50rwbZ+fJQqFRjB9H.8wXFl3X54o0C1A.1kEEofB1PXvISBZ15Z8Q43Q3ASWcC7I.9SETYr,b,7CQiwKn7zdzWdiq6ZmfiQpCO+ikf.WbyZ2wS135joqFA_r14uPQN')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

class conn:
    def conn_test():


        row = session.execute("select release_version from system.local;").one()
        if row:
            print(row[0])
        else:
            print("An error occurred.")