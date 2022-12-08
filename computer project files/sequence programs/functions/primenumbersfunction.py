# prime numbers function:
import time

time.sleep(2)
print('----- This is a program that generates a sequence of prime numbers within an interval -----')

def prime(l,u):
    c=0
    if l<2 or l==2:
        print('2')
    for n in range(l,u):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
                else:
                    c+=1
                    if c==(n-2):
                        time.sleep(0.05)
                        print(n)
                        c=0

time.sleep(1)
l=int(input('Please enter the lower limit of the range within which prime numbers are to be displayed: '))
time.sleep(1)
u=int(input('Please enter the upper limit of the range within which prime numbers are to be displayed: '))
time.sleep(1)

prime(l,u)
time.sleep(1)
                        
                
                    

