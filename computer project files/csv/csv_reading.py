# to read from a csv file:

import csv

def read_csv():
      with open('s.csv', mode='r') as f:
            read=csv.reader(f, delimiter=',')
            for row in read:
                  print(row)
      f.close()

read_csv()
