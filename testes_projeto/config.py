from flask_mysqldb import MySQL

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'M5fBd5UCXT&vfDX!'
    MYSQL_DB = 'bossow'

config = {
    'development': DevelopmentConfig
}