# fermat numbers function:
import time
time.sleep(2)
print('----- This is a Fermat Numbers sequence with terms not necessarily being prime -----')

def fermat(n):
    for i in range(1,n+1):
        f=(2**(2**i))+1
        time.sleep(0.05)
        print('-',f)
time.sleep(1)
n=int(input('Enter no. of terms of the sequence to be displayed: '))
fermat(n)
time.sleep(1)

