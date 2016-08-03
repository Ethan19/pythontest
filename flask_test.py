import mysql.connector

cnx = mysql.connector.connect(user='root',password='ethan2',host='localhost',database='pythontest')

cur = cnx.cursor()

cur.execute('select * from user')

print(cur.fetchall)

cnx.close()