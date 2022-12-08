# insert, update and delete (DML) operations:

import mysql.connector
con=mysql.connector.connect(host='localhost', user='root', password='kobe_24@lakers_8_2_messi_10', database='test')

if con.is_connected():
    print('Connection Successful')
cur=con.cursor()

# paste it here


#(i) INSERT OPERATION (use parameterized inputs from user):
s=int(input('Enter serial no. for query (start from 7): '))
n=input('Enter sequence name for query: ')
y=int(input('Enter year of discovery of the sequence for the query: '))
query1=("insert into sequences values({}, '{}', {})".format(s,n,y))
cur.execute(query1)
con.commit()                              # change in database reflects in mysql, but at that moment in python, it shows the insertion but in sql it doesn't and after that insertion finishes, it will not be reflected in both sql and python.
print('Row inserted successfully')

# test insertion:
query=('select * from sequences')
cur.execute(query)
data1=cur.fetchall()
for i in data1:
      print(i)
# for pre-insertion test, copy the above code and paste before the insertion query.



#(ii) UPDATE OPERATION: (can also be done without parameterized input):
# eg: (NON parameterized input):
# query='update mytable set marks=50 where RollNo=9" 

s=int(input('Enter serial no. for the record(row) to be updated: '))
n=input('Enter new (if to be changed, else enter same) sequence name for query: ')
y=int(input('Enter new year of discovery (if to be changed, else enter same) of the sequence for the query: '))
# here, one column to be the updating variable as updation is done by choosing that particular variable.
# therefore, the updating variable can be changed as per requirement.
# here it is s(serial number).
query2=("update sequences set sequence_name='{}', Year_of_Discovery={} where S_no={}".format(n,y,s))
cur.execute(query2)
con.commit()
print('Row updated successfully')

# test updation:
query=('select * from sequences')
cur.execute(query)
data1=cur.fetchall()
for i in data1:
      print(i)



#(iii) DELETE OPERATION: (can also be done without parameterized input):
# eg: (NON parameterized input):
# query='delete from sequences where S_no=7'
# here primary key can be used as deleting variable if one row to be deleted, else if for another column name details to be deleted, use another deleting variable (that colomn name).

s=int(input('Enter serial no. for the record(row) to be deleted: '))
# here in deletion, only the primary key is enough to delete the whole row as it is always unique.
query3=("delete from sequences where S_no={}".format(s))
cur.execute(query3)
con.commit()
print('Row deleted successfully')

# test deletion:
query=('select * from sequences')
cur.execute(query)
data1=cur.fetchall()
for i in data1:
      print(i)



