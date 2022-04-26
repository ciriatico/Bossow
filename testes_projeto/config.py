from flask_mysqldb import MySQL
import os

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')

config = {
    'development': DevelopmentConfig
}

