from flask_mysqldb import MySQL
import os

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = ''
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'bossow'

config = {
    'development': DevelopmentConfig
}