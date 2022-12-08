# this choice function is for choice to go back or exit;
# now, this is to only give back the right choices (1,2,3) and handle the wrong inputs from user

import sys
import time
from askchoice1 import ask_choice1
#ch3=0
#class ask:
def ask_choice2():
    time.sleep(1)
    print('\n1. Go back to main choice: ')
    print('2. Go back to sequence information choices: ')
    print('3. EXIT: ')
    
    time.sleep(1)
    k=0
    try:
        #global ch3
        ch3=int(input('Please enter a choice (1-3): '))
        time.sleep(2)
        for i in range(0,5):
            if ch3<1:
                print('Your choice is less than 1.')
                time.sleep(1)
                ch3=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch3>3:     
                print('Your choice is greater than 3.')
                time.sleep(1)
                ch3=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch3==1:
                pass
            elif ch3==2:
                #ask_choice1()
                pass
            elif ch3==3:
                sys.exit()
            if k==4:
                print('Wrong inputs, program exiting')
                time.sleep(1)
                sys.exit()
    except ValueError:
        print('Wrong input, program exiting')
        sys.exit()
    return (ch3,10)     # return a tuple value to access from outside
##y=ask_choice2()
##print(y)
#print(ask_choice2()[0])
#ask1=ask()
#ask1.ask_choice2()
#print(ask1.ch3)
#global ch3
#ask_choice2()
#print(ask_choice2()[0])
#print(ch3)
#print(ch1)
