# collatz sequence function:
import time

time.sleep(2)

print('----- This is a Collatz sequence -----')

def collatz(n):
    time.sleep(0.05)
    print(n)
    while n!=1:
        if n%2==0:
            n=n//2
            time.sleep(0.05)
            print(n)
            continue
        elif n%2!=0:
            n=(3*n)+1
            time.sleep(0.05)
            print(n)
            continue
        else:
            pass

time.sleep(2)
N=int(input('Enter no. of times to input any number and check the result: '))            
time.sleep(2)
#for i in range(1,N+1):
i=1
while i<N+1:
    time.sleep(1)
    n=int(input('Enter any number to start the sequence with: '))
    time.sleep(2)
    if (n<=0):
        print('Collatz sequence is defined for natural numbers only, please try again.')
        time.sleep(1)
        i-=1                # to show that counter is kept unchanged if negative number or 0 is inputed.
        i+=1
        continue
    time.sleep(2)
    collatz(n)
    i+=1
if N>1:
    time.sleep(1)
    print('- As you can see, no matter what number you start with, you will always get the result as 1, when the number is used to begin the Collatz sequence.')
    time.sleep(5)
    print('- Such an unexplainable phenomenon is called a conjecture in mathematics.')
    time.sleep(4)
else:
    pass



