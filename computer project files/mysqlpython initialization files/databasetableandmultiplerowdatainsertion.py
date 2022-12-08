# create databases and tables and multiple row parameterzied data inputs:

import mysql.connector
con=mysql.connector.connect(host='localhost', user='root', password='kobe_24@lakers_8_2_messi_10', database='con')
#connection object before database creation

if con.is_connected():
    print('Connection Successful')

cur=con.cursor()

# DATABASE CREATION commands:

##cur.execute('create database con')          
##print('Database created successfully')

# once database created, then add KEYWORD ARGUMENT database to the connection object creation line for creating table.
# so while doing the below query comment the database creation commands, as the database already exists.






# TABLE CREATION commands:

##query=('create table random(Number int, Name varchar(10), Price float)')
##cur.execute(query)
##print('Table created successfully')







# VALUE INSERTION into table: (use of PARAMETERIZED INPUTS):
# again, similar to the database one, create table commands are commented before executing this query.

# while loop for multiple row inputs:
while True:
    No=int(input('Enter number for insertion into table: '))
    Name=input('Enter name for insertion into table: ')
    Price=float(input('Enter price for insertion into table: '))
    query2=("insert into random values({},'{}',{})".format(No, Name, Price))
    cur.execute(query2)
    con.commit()                                            # for commands to reflect in mysql
    print('Values inserted into row successfully')
    ch=input('Do you want to enter more records (y/n): ')
    if ch=='n':
        break
    else:
        continue
