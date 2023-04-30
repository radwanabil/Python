import mysql.connector
from mysql.connector import Error
from getpass import getpass

class database:
    def __init__(self, config):
        self.config = config

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            print(err)
        else:
            return self

    def insert(self, query, data):
        self.query(query, data)

    def remove(self, query, data):
        self.query(query, data)

    def update(self, query, data):
        self.query(query, data)

    def query(self, query, data=None):
        try:
            self.cursor.execute(query, data)
            self.cnx.commit()
        except mysql.connector.Error as err:
                print(err)

    def get_all_records(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as err:
                print(err)
        else:
            return self.cursor.fetchall()