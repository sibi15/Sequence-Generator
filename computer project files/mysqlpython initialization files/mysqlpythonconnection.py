import mysql.connector
con=mysql.connector.connect(host="localhost", user="root", password="kobe_24@lakers_8_2_messi_10")
if con.is_connected():
    print("Connection Successful")
#con is the connection object
cur=con.cursor()                    #CursorObject=ConnectionObject.cursor()
cur.execute("create database tests") #CursorObject.execute(<SQL Query string>)
print("Query executed successfully")
