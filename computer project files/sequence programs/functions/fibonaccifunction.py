# fibonacci numbers sequence(original):
import time

time.sleep(2)

print('----- This program prints the sequence of Fibonacci Numbers -----')

time.sleep(1.5)
def fibonacci_n(n):
    a=0
    b=1
    c=0
    time.sleep(0.05)
    print(a)
    time.sleep(0.05)
    print(b)
    for i in range (n-2):
        c=a+b
        time.sleep(0.05)
        print(c)
        a=b
        b=c

time.sleep(1)
n=int(input('Enter no. of terms in the sequence required to be displayed: '))
fibonacci_n(n)
time.sleep(1)
# print("The original Fibonacci Series with the starting numbers 0 and 1 is unique due to its application in the real world.")
        
