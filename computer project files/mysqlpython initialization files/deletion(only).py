import mysql.connector
con2=mysql.connector.connect(host='localhost', user='root', password='kobe_24@lakers_8_2_messi_10', database='test')

if con2.is_connected():
    print('Connection Successful')
cur=con2.cursor()

query=('select * from sequences')
cur.execute(query)
data1=cur.fetchall()
for i in data1:
      print(i)

query2=('delete from sequences where S_no>6')
cur.execute(query2)
con2.commit()
print('Successful Deletion')


query=('select * from sequences')
cur.execute(query)
data1=cur.fetchall()
for i in data1:
      print(i)







