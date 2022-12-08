import sys
import time


# first ask choice for entering:

ch1=0
def ask_choice1():                                                                         # function for asking FIRST choice
    print('Operations: ')
    time.sleep(2)

    print('1. Display Information of Sequences: ')
    print('2. Choose sequence to work with (generation): ')
    print('3. EXIT:', '\n')
    time.sleep(4)
    
    j=0
    try:
        global ch
        ch=int(input('Please enter a choice (1-3): '))                     # Choosing of operation to perform:
        time.sleep(2)
        for i in range(0,5):                                                                # Gives user 5 attempts to enter a number in the range (1-3):
            time.sleep(1)
            if ch<1:                                                            
                print('Your choice is less than 1.')
                time.sleep(1)
                ch=int(input('Please enter a numerical choice in the range (1-3): '))
                j+=1
            elif ch1>3:
                print('Your choice is greater than 3.')
                time.sleep(1)
                ch=int(input('Please enter a numerical choice in the range (1-3): '))
                j+=1
            elif ch==1:
                break
            elif ch==2:
                break
            elif ch==3:
                break
            if j==4:
                print('Wrong inputs, program exiting')                                       # If data type other than an integer is inputed: (exits program)
                time.sleep(1)                                                               # no chances
                sys.exit()
    

    except ValueError:                                                                     
        print('Wrong input, program exiting')
        time.sleep(1)
        sys.exit()

    if ch1==1:
        print('\nYour choice is (1. Display Information of Sequences: )\n')
    elif ch1==2:
        print('\nYour choice is (2. Choose sequence to work with (generation): )\n')
    elif ch1==3:
        print('\nYour choice is (3. EXIT: )\n')
    time.sleep(3)
    return ch1

#ask_choice1()
#print(ch1)

