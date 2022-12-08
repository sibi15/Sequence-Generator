# csv part for sequence generator

import csv

def suggestion_csv():
      #with open('suggestions.csv', mode='a') as test:
      #      test.close()

      with open('suggestions.csv', mode='r') as f:
            r=csv.reader(f, delimiter=',')
            count=0
            for row in r:
                if len(row)!=0:
                      #print(row)
                      count+=1
                else:
                      pass

      with open('suggestion.csv', mode='a') as f:
            w=csv.writer(f,delimiter=',')
            n=int(input('Please input no. of suggestions you wish to provide: '))
            for i in range(1,n+1):
                  serial_num=str(count+i)+'.'
                  suggestion=input('Enter sequence name: ')
                  w.writerow([serial_num,suggestion])
            print('Suggestions received. Thank you!')

      



suggestion_csv()
                  
            
            
            
