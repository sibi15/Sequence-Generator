# parameterized queries: input from users:
# used for runtime input from users

# (i) OLD style:
# SYNTAX: f%v
# f - template string 
# v - values to be formatted using templates (should be a tuple)

# eg: 'select * from student where marks > %s'%(70,)
#f-'select * from student where marks>%s'
#v-(70,)

# s - value like %(70,) [replaced at runtime]
# single element tuple (70,)

# (ii) NEW style:
# string template with % formatting

# eg: str="select * from student where marks>{} and section='{}'".format(70,'B')
# format replaces blanks inside {} by 70 and 'B' during runtime



import mysql.connector
con=mysql.connector.connect(host='localhost', user='root', password='kobe_24@lakers_8_2_messi_10', database='test')

#if con.is_connected():
#    print('Connection Successful')

cur=con.cursor()



query1=('select * from sequences')
cur.execute(query1)
data1=cur.fetchall()
for i in data1:
    print(i)
print('No. of records retrieved =', cur.rowcount,'\n')

# to display the details of those sequences discovered after the year 1500:
query2=('select * from sequences where Year_of_Discovery>1500')
cur.execute(query2)
data2=cur.fetchall()
for i in data2:
    print(i)
print('No. of records retrieved =', cur.rowcount,'\n')




# (i) OLD METHOD:

# PARAMETERIZED INPUT:

# user input for Year_of_Discovery during runtime:
y=int(input('Enter Year_of_Discovery for query: '))
query3=('select * from sequences where Year_of_Discovery>%s'%(y,))
cur.execute(query3)
data3=cur.fetchall()
for i in data3:
        print(i)
print('No. of records retrieved =', cur.rowcount,'\n')



# MULTIPARAMETERIZED INPUTS:

# user input for Year_of_Discovery and sequence_name during runtime:
y=int(input('Enter min year of discovery after which all records to be displayed for query: '))
s=input('Enter sequence name for query: ')
query4=("select * from sequences where Year_of_Discovery>%s and sequence_name='%s'"%(y,s))
cur.execute(query4)
data4=cur.fetchall()
for i in data4:
    print(i)
print('No. of records retrieved =', cur.rowcount, '\n')



# (ii) NEW METHOD:

# PARAMETERIZED INPUTS:

# user input for Year_of_Discovery during runtime:
y=int(input('Enter min year of discovery after which all records to be displayed for query: '))
query5=("select * from sequences where Year_of_Discovery>{}".format(y))
cur.execute(query5)
data5=cur.fetchall()
for i in data5:
    print(i)
print('No. of records retrieved is =', cur.rowcount, '\n')


# MUTLIPARAMETERIZED INPUT:

# user input for Year_of_Discovery and sequence_name during runtime:
y=int(input('Enter min year of discovery after which all records to be displayed for query: '))
s=input('Enter sequence name for query: ')
query6=("select * from sequences where Year_of_Discovery>{} and sequence_name='{}'".format(y,s))
cur.execute(query6)
data6=cur.fetchall()
for i in data6:
    print(i)
print('No. of records retrieved =', cur.rowcount, '\n')
        
















        












