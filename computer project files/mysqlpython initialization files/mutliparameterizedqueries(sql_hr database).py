# multi parameterized queries:
import mysql.connector
con2=mysql.connector.connect(host='localhost', user='root', password='kobe_24@lakers_8_2_messi_10', database='sql_hr')

#if con2.is_connected():
#   print('Connection 2 successful')

# basic select all:

cur1=con2.cursor()

query1=('select * from offices')
cur1.execute(query1)
data1=cur1.fetchall()
for i in data1:
    print(i)
print('No. of records retrieved =', cur1.rowcount, '\n')

#(i) OLD STYLE:
# user input for office_id and state during runtime:

o=int(input('Enter min office_id for query: '))
s=input('Enter state for query: ')
query2=("select * from offices where office_id>%s and state='%s'"%(o,s))
cur1.execute(query2)
data2=cur1.fetchall()
for i in data2:
    print(i)
print('No. of records retrieved =', cur1.rowcount, '\n')

#(ii) NEW STYLE:

o=int(input('Enter min office_id for query: '))
s=input('Enter state for query: ')
query3=("select * from offices where office_id>{} and state='{}'".format(o,s))
cur1.execute(query3)
data3=cur1.fetchall()
for i in data3:
    print(i)
print('No. of records retrieved =', cur1.rowcount, '\n')




