import pymysql.cursors
import pymysql

#connect to database
cnx = pymysql.connect(host='localhost', user= 'root', password= 'organization@16',db='sodiq',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
mycursor= cnx.cursor()
mycursor.execute("show tables")
for x in mycursor:
    print(x)
mycursor.execute("select * from achievers")
for x in mycursor:
    print(x)