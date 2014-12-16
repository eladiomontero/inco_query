import csv, mysql.connector, glob
from mysql.connector import errorcode

class DataDownloader():
    def __init__(self):
        self.config = {
          'user': 'admin',
          'password': 'grupoinco',
          'host': 'grupoinco.c1h9rscqpaqw.us-west-2.rds.amazonaws.com',
          'database': 'datasur',
          'port': 3306
        }
        self.cnx = ""
        self.cursor = ""

    def connect(self):
        try:
          self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exists")
          else:
            print(err)
        else:
          self.cursor = self.cnx.cursor()

    def execute_query(self, query):
        try:
            result = self.cursor.execute(query)
        except Exception as e:
            print e.message
