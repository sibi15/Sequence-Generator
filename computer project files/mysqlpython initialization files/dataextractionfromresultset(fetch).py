# extraction of data from resultset:
# during select query:

# all tuples are stored in lists: [(row1),(row2),(row3),...,(row n)]
# row=record

# data=cursor.fetchall() - return records (rows) retrieved as per query in a tuple
# data=cursor.fetchone() - one retrieval of record as a tuple from resultset at a time
# data=cursor.fetchmany(n) - fetches n records as a tuple
# variable=cursor.rowcount - returns no. of rows retrieved [PROPERTY]

# if no record is retrieved, default value returned is None

# cursor above refers to the cursor object

# mysql - LIBRARY
# connector - PACKAGE
import mysql.connector
con=mysql.connector.connect(host="localhost", user="root", password="kobe_24@lakers_8_2_messi_10", database='test', buffered=True)

# if con.is_connected():
#     print("Connection Successful")



#FETCHALL()

#1:
cur1=con.cursor()
cur1.execute('select * from sequences')

# now use fetch to display the result of the SQL Query here:

data1=cur1.fetchall()
for i in data1:
    print(i)
print('\nTotal no. of rows retrieved =', cur1.rowcount,'\n')

#2:
cur2=con.cursor()
query1='select * from sequences where Year_of_Discovery>1500'
cur2.execute(query1)

data2=cur2.fetchall()
for i in data2:
    print(i)
print('\nTotal no. of rows retrieved =', cur2.rowcount,'\n')


#FETCHONE()
cur3=con.cursor()
cur3.execute('select * from sequences')


data3=cur3.fetchone()
print(data3)
print('\nTotal no. of rows retrieved =', cur3.rowcount,'\n')

data3=cur3.fetchone()                   #FETCHONE() retrieves one record at a time
print(data3)                            #here cursor object jumps from record 1 to record 2
print('\nTotal no. of rows retrieved =', cur3.rowcount,'\n')


# but does not show rowcount as 1, because same cursor's rowcount gets added, rows retrieved at point of time, so shows 2



#FETCHMANY(N):
cur4=con.cursor(buffered=True)
cur4.execute('select * from sequences')

data4=cur4.fetchmany(2)
#c=0                                    # use c if buffered is true, internal
for i in data4:
    #c+=1
    print(i)
#print(data4)
print('\nTotal no. of rows retrieved =', cur4.rowcount,'\n')

data4=cur4.fetchmany(3)               # same again, basically fetchone() one at a time, and cursor continues, WHEREAS here, cursor continues after wherever the n ends (eg: 4+4+)
#c=0
for i in data4:
    #c+=1
    print(i)
#print(data4)
print('\nTotal no. of rows retrieved =', cur4.rowcount,'\n')

data5=cur4.fetchone()
print(data5)





























    






    
