# Pascal Triangle Numbers:
# If we only add the middle numbers other than the 1s, we see that it is a geometric progression
# 0,1,2,6(3+3),14(4+6+4),30(5+10+10+5),...

import time

print('----- This is a program that generates a sequence of the Pascal Triangle Numbers ----- ')

def trianglenum(n):
        L1=[['\n1'],[1,2,1]]
        for i in range(0,n-2):
                L2=[1]+[(L1[-1][i] + L1[-1][i+1]) for i in range(0,len(L1[-1])-1)]+[1]
                L1.append(L2)

        ctr=0
        for i in L1:
              if ctr>0:
                    print('\n')
              for j in i:
                    print(j, end=' ')
                    time.sleep(0.01)
                    ctr+=1
        
time.sleep(2)
n=int(input('Enter number of lines to be generated: '))
trianglenum(n)

##num=0
##	for i in range(0,n):
##             num=(2*num)+2
##             #time.sleep(0.05)
##     	     print(num)
    
    
