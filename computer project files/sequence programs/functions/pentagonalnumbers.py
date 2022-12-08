# Pentagonal Numbers:
# Pn = (3n^2 - n)/2
import time
time.sleep(2)

print('----- This is a program that generates a sequence of the Pentagonal Numbers -----')

def pentagonal(n):
    for i in range(0,n):
        num=i**2
        num=num*3
        num=num-i
        num=num/2
        num=int(num)
        time.sleep(0.05)
        print(num)

time.sleep(1)
n=int(input('Please enter the number of lines of Pentagonal Numbers to be displayed: '))
pentagonal(n)
time.sleep(1)
