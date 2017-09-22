import MySQLdb

MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"
MYSQL_DB = "mysql"

mysqlConnection = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT,
    user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB)
dbhandler = mysqlConnection.cursor()