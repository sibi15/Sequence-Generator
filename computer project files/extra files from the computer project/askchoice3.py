# askchoice3
# this choice is for going back from the sequence GENERATION part

import sys
import time

def ask_choice3():
    time.sleep(1)
    print('\n1. Go back to main choice: ')
    print('2. Go back to sequence generation choices: ')
    print('3. EXIT: ')

    time.sleep(1)
    k=0
    try:
        ch5=int(input('Please enter a choice in the range (1-3): '))
        time.sleep(2)
        for i in range(0,5):
            if ch5<1:
                print('Your choice is less than 1. ')
                time.sleep(1)
                ch5=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch5>3:
                print('Your choice is greater than 3: ')
                time.sleep(1)
                ch5=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch5==1:
                pass
            elif ch5==2:
                pass
            elif ch5==3:
                sys.exit()
            if k==4:
                print('Wrong input, program exiting')
                time.sleep(1)
                sys.exit()
    except ValueError:
        print('Wrong input, program exiting')
        time.sleep(1)
        sys.exit()
    return (ch5,10)
y=ask_choice3()[0]
print(y)      
        
    
