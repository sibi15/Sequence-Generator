# main program:

# OLD VERSION: without pyttsx3 (AS IT IS FROM WINDOWS, MAC UPDATES ON THE with pyttsx3 main.py)

# As in MAC, directories to notepad files and sub-programs are to be changed




# Right now, sequence info transcipt sending, is via MULTI-LINE STRING
# and shell transcript is via TEXT FILE



# CSV  ===> NOTEPAD
# TEXT ===> NOTEPAD


# Slowly, add voice recognition at the input parts (if wrong, cancel and type too) and reach 10 sequences.


import mysql.connector
from time import perf_counter, sleep
import time
import pyttsx3
engine=pyttsx3.init()

start=time.perf_counter()                            # for time complexity of the program

import sys
import ssl
import smtplib

# CONNECTION AND CURSOR OBJECT INSTANTIATION:

con=mysql.connector.connect(host='localhost', user='root', password='kobe_24@lakers_8_2_messi_10', database='test')
# if con.is_connected():
#     print('Connection successful')

cur=con.cursor()   #cursor object:

#____________________________________________________________________________________________________________________________________________________


# ask_choice2           ---> Going back to seqeunce info or main choice
# ask_choice3           ---> Going back to sequence generation or main choice
# suggestion            ---> To add suggestion of a sequence to MySQL

# SHELL:
    # send_windowtranscript     ---> Probably will remove, doesn't work
    # send_text                 ---> sending the window transcript by writing onto a CSV file
    # send_text_multilinestring ---> send the multi-line string directly

# INFO:
    # send_infotranscript   ---> Line-by-line info send
    # send_direct           ---> send direct file
    # send_multilinestring  ---> send via multilinestring

#____________________________________________________________________________________________________________________________________________________

                                                                    # CHOICES:
  

def ask_choice2():                                             # function defined here rather than importing ask_choice2 because of variable problem (while return value is assigned to some variable y, here.)
    print('\nOptions:')
    time.sleep(1)                                              # this function is a choice for going back to main choice or for going back to sequence information choice. 
    print('1. Go back to main choice: ')
    print('2. Go back to sequence information choices: ')
    print('3. EXIT: ')
    #print('4. Suggestion for adding sequences: ')
    
    time.sleep(2)
    k=0
    try:
        #global ch3
        ch3=int(input('Please enter a choice (1-3): '))
        time.sleep(2)
        for i in range(0,5):
            if ch3<1:
                time.sleep(1)
                print('Your choice is less than 1.')
                time.sleep(1)
                ch3=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch3>3:     
                time.sleep(1)
                print('Your choice is greater than 3.')
                time.sleep(1)
                ch3=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch3==1:
                pass
            elif ch3==2:
                pass
            elif ch3==3:    # add that suggestion here
                time.sleep(1)
                suggestion()                                                                # SUGGESTION usage before defined, might give error
                time.sleep(2)

##                send_windowtranscript()
##                time.sleep(2)
                send_text()
                time.sleep(2)
##                send_text_multilinestring()
##                time.sleep(2)

##                send_infotranscript()
##                time.sleep(2)
##                send_direct()
##                time.sleep(2)
                send_multiilinestring()
                time.sleep(2)
                end=time.perf_counter()
                time1=end-start
                print('\nThank you for visiting!                                                                        > Time elapsed:',time1,'seconds')
                time.sleep(1)
                sys.exit()
            if k==4:
                time.sleep(1)
                end=time.perf_counter()
                time1=end-start
                print('Maximum no. of attempts crossed, program exiting.                                              > Time elapsed:',time1,'seconds')
                time.sleep(1)
                sys.exit()
    except ValueError:
        time.sleep(1)
        end=time.perf_counter()
        time1=end-start
        print('Wrong input, program exiting.                                                                > Time elapsed:', time1,'seconds')
        time.sleep(1)
        sys.exit()
        #print('\n')
    return ch3                                                # return value stored in some variable for easier access
                

def ask_choice3():                                            # this function is a choice for going back to main choice or for going back to sequence generation choice.
    print('\nOptions:')
    time.sleep(1)
    print('1. Go back to main choice: ')
    print('2. Go back to sequence generation choices: ')
    print('3. EXIT: ')

    time.sleep(2)
    k=0
    try:
        ch5=int(input('Please enter a choice in the range (1-3): '))
        time.sleep(2)
        for i in range(0,5):
            if ch5<1:
                time.sleep(1)
                print('Your choice is less than 1. ')
                time.sleep(1)
                ch5=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch5>3:
                time.sleep(1)
                print('Your choice is greater than 3. ')
                time.sleep(1)
                ch5=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch5==1:
                pass
            elif ch5==2:
                pass
            elif ch5==3:
                time.sleep(1)
                suggestion()
                time.sleep(2)

##                send_windowtranscript()
##                time.sleep(2)
                send_text()
                time.sleep(2)
##                send_text_multilinestring()
##                time.sleep(2)

##                send_infotranscript()
##                time.sleep(2)
##                send_direct()
##                time.sleep(2)
                send_multiilinestring()
                time.sleep(2)
                end=time.perf_counter()
                time1=end-start
                print('\nThank you for visiting!                                                                        > Time elapsed:',time1,'seconds')
                time.sleep(1)
                sys.exit()
            if k==4:
                time.sleep(1)
                end=time.perf_counter()
                time1=end-start
                print('Maximum no. of attempts crossed, program exiting.                                              > Time elapsed:',time1,'seconds')
                time.sleep(1)
                sys.exit()
    except ValueError:
        time.sleep(1)
        end=time.perf_counter()
        time1=end-start
        print('Wrong input, program exiting.                                                                > Time elapsed:', time1,'seconds')
        time.sleep(1)
        sys.exit()
        #print('\n')
    return ch5




#____________________________________________________________________________________________________________________________________________________

                                                                # SUGGESTION:

                                                        
# SUGGESTION MODULE (Cursor object needed, hence defined here after the cursor object is instantiated):

def suggestion():           # call this function at every exit point except for the input error exits:
    time.sleep(1)
    sug=input('\nSUGGESTION: Would you like to provide a suggestion for a sequence to add? (y/n): ')
    time.sleep(2)

    if sug=='y':
        n=int(input('Please enter the no. of suggestions you want to provide: '))
        time.sleep(1)
        for i in range(1,n+1):
            name=input('Enter sequence name suggestion: ')
            query1=("insert into suggestions values('{}')".format(name))
            cur.execute(query1)
            con.commit()
            time.sleep(1)
            print('Suggestion accepted successfully.\n')
    elif sug=='n':
        pass
    else:
        print('Wrong input, try again. \n')
        time.sleep(1)
        suggestion()        # Recurssion
        


#____________________________________________________________________________________________________________________________________________________

                                                            # TRANSCRIPT 1: SHELL WINDOW:


def send_windowtranscript():     # only variable is the mail id:
    time.sleep(2)
    tr1=input('\nTRANSCRIPT 1: Would you like to receive a mail regarding the transcript of the shell window? (y/n): ')
    time.sleep(2)
    if tr1=='n':
        pass
    elif tr1=='y':
        n=int(input('Enter no. of mails to be sent to the same, or different addresses: '))              # n and message are fixed
        time.sleep(2)
        message=input('Please copy the text in the shell window above, paste it here and enter: ')       
        time.sleep(2)

        port=465
        smtp_server="smtp.gmail.com"
        sender_email="04250@asianintlschool.com"
        password="sibikarthik260104"
#       context=ssl.create_default_context()
        for i in range(1,n+1):
            context=ssl.create_default_context()
            receiver_email=input('Please enter email address to send the shell window transcript to: ')
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print('Sending mail',i)
                #try:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
                #except SMTPAuthenticationError:
                print('Mail sent.\n')
                server.quit()
        print('Mail to the addresses sent.\n') 
    else:
        print('Wrong input, try again. \n')
        time.sleep(1)
        send_windowtranscript()


# TWO DIFFERENT FUNCTIONS for sending the shell window transcript (CSV FILE and MULTI-LINE STRING):

# (i) CSV FILE:

def send_text():
    time.sleep(2)
    tr1=input('\nTRANSCRIPT 1: Would you like to receive a mail regarding the transcript of the shell window? (y/n): ')
    time.sleep(2)
    if tr1=='n':
        pass
    elif tr1=='y':
        n=int(input('Enter the no. of mails to be sent to the same, or different addresses: '))
        time.sleep(2)
        print('Please follow the following instructions: ')
        time.sleep(1)
        print('\nPlease copy the text in the shell window above, paste it after this line when prompted and ENTER. Then when the cursor is at the starting of the next line, please press CTRL+D: ')
        time.sleep(6)
        text=sys.stdin.read()
        shell_w=open('C:/Users/sibik/OneDrive/Desktop/computer project files/shellwindow.txt','w')
        shell_w.write(text)
        shell_w.close()
        shell_r=open('C:/Users/sibik/OneDrive/Desktop/computer project files/shellwindow.txt','r')
        time.sleep(1)
        shell_r=shell_r.read()
        #shell.close()
        time.sleep(2)

        port=465
        smtp_server="smtp.gmail.com"
        sender_email="04250@asianintlschool.com"
        password="sibikarthik260104"
        for i in range(1,n+1):
            context=ssl.create_default_context()
            receiver_email=input('\nPlease enter email address to send the shell window transcript to: ')
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print('Sending mail to mail address', i)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, shell_r)
                print('Mail sent.\n')
                server.quit()
        print('Mail to the address sent.\n')
    else:
        print('Wrong input, try again. \n')
        time.sleep(1)
        send_text()


# (ii) DIRECT MULTI-LINE string send after reading from NOTEPAD File:

def send_text_multilinestring():
    time.sleep(2)
    tr2=input('\nTRANSCRIPT 1: Would you like to receive a mail regarding the transcript of the shell window? (y/n): ')
    time.sleep(2)
    if tr2=='n':
        pass
    elif tr2=='y':
        n=int(input('Enter the no. of mails to be sent to the same, or different addresses: '))
        time.sleep(2)
        print('Please follow the following instructions: ')
        time.sleep(1)
        print('\nPlease copy the text in the shell window above, paste it after this line when prompted and ENTER. Then when the cursor is at the starting of the next line, please press CTRL+D: ')
        time.sleep(6)
        text=sys.stdin.read()
        shell_w=open('C:/Users/sibik/OneDrive/Desktop/computer project files/shellwindow.txt','w')
        shell_w.write(text)
        shell_w.close()
        text=''''''
        shell_r=open('C:/Users/sibik/OneDrive/Desktop/computer project files/shellwindow.txt','r')
        time.sleep(1)
        shell_r=shell_r.read()
        text=text+shell_r
        #shell.close()
        time.sleep(2)

        port=465
        smtp_server="smtp.gmail.com"
        sender_email="04250@asianintlschool.com"
        password="sibikarthik260104"
        for i in range(1,n+1):
            context=ssl.create_default_context()
            receiver_email=input('\nPlease enter email address to send the shell window transcript to: ')
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print('Sending mail to mail address', i)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
                print('Mail sent.\n')
                server.quit()
        print('Mail to the address sent.\n')
    else:
        print('Wrong input, try again. \n')
        time.sleep(1)
        send_text_multilinestring()
        


#____________________________________________________________________________________________________________________________________________________

                                                            # TRANSCRIPT 2: SEQUENCE INFO FILES:


def send_infotranscript():
    time.sleep(2)
    tr3=input('\nTRANSCRIPT 2: Would you like a mail regarding the transcript of the sequence information? (y/n): ')
    time.sleep(2)
    if tr3=='n':
        pass
    elif tr3=='y':
        n=int(input('Enter no. of mails to be sent to the same, or different addresses: '))
        time.sleep(2)
        print('\nNOTE: You will be getting a no. of mails for each of the sequences and maybe also the same sequence as parts because of the word limit constraint while sending\n')
        time.sleep(8)
        port=465
        smtp_server="smtp.gmail.com"
        sender_email="04250@asianintlschool.com"
        password="sibikarthik260104"
        file1=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fibonaccinumbers.txt','r')
        r1=file1.readlines()
        file2=open('C:/Users/sibik/OneDrive/Desktop/computer project files/prime numbers.txt','r')
        r2=file2.readlines()
        file3=open('C:/Users/sibik/OneDrive/Desktop/computer project files/collatz sequence.txt','r')
        r3=file3.readlines()
        file4=open('C:/Users/sibik/OneDrive/Desktop/computer project files/pascal triangle numbers.txt','r')     
        r4=file4.readlines()
        file5=open('C:/Users/sibik/OneDrive/Desktop/computer project files/pentagonal numbers.txt','r')           
        r5=file5.readlines()
        file6=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fermat numbers.txt','r')               
        r6=file6.readlines()
        
        for i in range (1,n+1):
            context=ssl.create_default_context()
            receiver_email=input('Please enter email address to send the shell window transcript to: ')
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print('Sending mail to address',i)
                server.login(sender_email, password)
                for j in r1:
                    message=j.strip()
                    time.sleep(1)
                    server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 1 sent.')
                file1.close()
                for j in r2:
                    message=j.strip()
                    time.sleep(1)
                    server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 2 sent.')
                file2.close()
                for j in r3:
                    message=j.strip()
                    time.sleep(1)
                    server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 3 sent.')
                file3.close()
                for j in r4:
                    message=j.strip()
                    time.sleep(1)
                    server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 4 sent.')
                file4.close()
                for j in r5:
                    message=j.strip()
                    time.sleep(1)
                    server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 5 sent.')
                file5.close()
                for j in r6:
                    message=j.strip()
                    time.sleep(1)
                    server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 6 sent.\n')
                file6.close()
                server.quit()
        print('> Mail to the inputed', n, 'addresses sent.\n')
    else:
        print('Wrong input, try again. \n')
        time.sleep(1)
        send_infotranscript()


# TWO DIFFERENT FUNCTIONS for Notepad file sending (DIRECT and MULTI-LINE STRING):

# (i) DIRECT:

def send_direct():
    time.sleep(2)
    tr4=input('\nTRANSCRIPT 2: Would you like a mail regarding the transcript of the sequence information? (y/n): ')
    time.sleep(2)
    if tr4=='n':
        pass
    elif tr4=='y':
        n=int(input('Enter no. of mails to be sent to the same, or different addresses: '))
        time.sleep(2)
        port=465
        smtp_server="smtp.gmail.com"
        sender_email="04250@asianintlschool.com"
        password="sibikarthik260104"
        
        for i in range(1,n+1):
            context=ssl.create_default_context()
            receiver_email=input('Please enter email address to send the shell window transcript to: ')
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print('Sending files to address', i)
                server.login(sender_email, password)
                time.sleep(2)

                message1=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fibonaccinumbers.txt','r')
                message1=message1.read()
                server.sendmail(sender_email, receiver_email, message1)
                print('SEQUENCE 1 sent.')
                time.sleep(2)

                message2=open('C:/Users/sibik/OneDrive/Desktop/computer project files/prime numbers.txt','r')
                message2=message2.read()
                server.sendmail(sender_email, receiver_email, message2)
                print('SEQUENCE 2 sent.')
                time.sleep(2)

                message3=file3=open('C:/Users/sibik/OneDrive/Desktop/computer project files/collatz sequence.txt','r')
                message3=message3.read()
                server.sendmail(sender_email, receiver_email, message3)
                print('SEQUENCE 3 sent.')
                time.sleep(2)
                
                message4=open('C:/Users/sibik/OneDrive/Desktop/computer project files/pascal triangle numbers.txt','r')     
                message4=message4.read()
                server.sendmail(sender_email, receiver_email, message4)
                print('SEQUENCE 4 sent.')
                time.sleep(2)
                
                message5=open('C:/Users/sibik/OneDrive/Desktop/computer project files/pentagonal numbers.txt','r')           
                message5=message5.read()
                server.sendmail(sender_email, receiver_email, message5)
                print('SEQUENCE 5 sent.')
                time.sleep(2)
                      
                message6=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fermat numbers.txt','r')               
                message6=message6.read()
                server.sendmail(sender_email, receiver_email, message6)
                print('SEQUENCE 6 sent.\n')
                time.sleep(2)

                print('Mails sent for address', i)
                server.quit()
        print('\nAll mails sent.')
    else:
        print('Wrong input, try again. \n')
        time.sleep(1)
        send_direct()


# (ii) MULTI-LINE string:

def send_multilinestring():
    time.sleep(2)
    tr5=input('\nTRANSCRIPT 2: Would you like a mail regarding the transcript of the sequence information? (y/n): ')
    time.sleep(2)
    if tr5=='n':
        pass
    elif tr5=='y':
        n=int(input('Enter no. of mails to be sent to the same, or different addresses: '))
        time.sleep(2)
        port=465
        smtp_server="smtp.gmail.com"
        sender_email="04250@asianintlschool.com"
        password="sibikarthik260104"
        
        for i in range(1,n+1):
            context=ssl.create_default_context()
            receiver_email=input('Please enter email address to send the shell window transcript to: ')
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print('Sending files to address', i)
                server.login(sender_email, password)
                time.sleep(2)

                m1=''''''
                message1=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fibonaccinumbers.txt','r')
                message1=message1.read()
                m1=m1+message1
                server.sendmail(sender_email, receiver_email, m1)
                print('SEQUENCE 1 sent.')
                time.sleep(2)

                m2=''''''
                message2=open('C:/Users/sibik/OneDrive/Desktop/computer project files/prime numbers.txt','r')
                message2=message2.read()
                m2=m2+message2
                server.sendmail(sender_email, receiver_email, m2)
                print('SEQUENCE 2 sent.')
                time.sleep(2)

                m3=''''''
                message3=open('C:/Users/sibik/OneDrive/Desktop/computer project files/collatz sequence.txt','r')
                message3=message3.read()
                m3=m3+message3
                server.sendmail(sender_email, receiver_email, m3)
                print('SEQUENCE 3 sent.')
                time.sleep(2)

                m4=''''''
                message4=open('C:/Users/sibik/OneDrive/Desktop/computer project files/pascal triangle numbers.txt','r')     
                message4=message4.read()
                m4=m4+message4
                server.sendmail(sender_email, receiver_email, m4)
                print('SEQUENCE 4 sent.')
                time.sleep(2)

                m5=''''''
                message5=open('C:/Users/sibik/OneDrive/Desktop/computer project files/pentagonal numbers.txt','r')           
                message5=message5.read()
                m5=m5+message5
                server.sendmail(sender_email, receiver_email, m5)
                print('SEQUENCE 5 sent.')
                time.sleep(2)

                m6=''''''
                message6=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fermat numbers.txt','r')               
                message6=message6.read()
                m6=m6+message6
                server.sendmail(sender_email, receiver_email, m6)
                print('SEQUENCE 6 sent.\n')
                time.sleep(2)

                print('Mails sent for address', i)
                server.quit()
        print('\nAll mails sent.')
    else:
        print('Wrong input, try again. \n')
        time.sleep(1)
        send_multilinestring()

        

                
#____________________________________________________________________________________________________________________________________________________
        
    
                                                                    #INTRODUCTION:

                                                                    

time.sleep(2)
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
time.sleep(2)
print('                                                            ----- SEQUENCE GENERATOR -----\n')
time.sleep(2)
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
time.sleep(2)
print('----------------------------------------------------------------------------------------------------')
time.sleep(2)
print('| * NOTE:                                                                                          |')
time.sleep(2)
print('| - When the program asks for your input, please type the input and press the ENTER key.           |')
time.sleep(2)
print("| - If you want to exit the program immediately at any point, please use the command 'CTRL+C'.     |")
time.sleep(2)
print('----------------------------------------------------------------------------------------------------\n')
time.sleep(6)

print('Options:')
time.sleep(2)
print('      |')
print('      |')
time.sleep(2)
print('      |---> 1. SEQUENCE INFORMATION')
time.sleep(2)
print('      |')
print('      |')
time.sleep(2)
print('      |---> 2. SEQUENCE GENERATION')
time.sleep(2)
print('      |')
print('      |')
time.sleep(2)
print('      |---> 3. EXIT')
time.sleep(2)
print('                  |')
print('                  |')
time.sleep(2)
print('                  |---> SUGGESTION TO ADD SEQUENCES')
time.sleep(2)
print('                  |---> FILE TRANSCRIPT')
time.sleep(2)
print('                                      |')
print('                                      |')
time.sleep(2)
print('                                      |---> Shell Window (copy and paste)')
time.sleep(2)
print('                                                       |')
print('                                                       |')
time.sleep(1)
print('                                                       |---> Direct TEXT file sending')
print('                                                       |---> Multi-line string from TEXT file\n')
time.sleep(3)
print('                                      |---> Briefs of sequences')
time.sleep(2)
print('                                                       |')
print('                                                       |')
time.sleep(1)
print('                                                       |---> Line-by-line sending')
print('                                                       |---> Direct TEXT file sending')
print('                                                       |---> Multi-line string\n')
time.sleep(3)

time.sleep(5)
print('- The following is the table of sequences within which you may ask the given operations to be performed: ', '\n')
time.sleep(4)
print('(S_no:', ' Sequence Name:', ' Year of Discovery:)', sep=' ', end='\n')
time.sleep(3)

query=('select * from sequences')               # prints table 
cur.execute(query)
data1=cur.fetchall()
#print('\n')
for i in data1:
    time.sleep(1)
    print(i,'\n')
time.sleep(2)
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
time.sleep(2)






# USER INPUT:

while True:                                                                                 # This is for the choice twice back or once back (corresponds to the breaks)

    print('\nOperations: ')
    time.sleep(2)

    print('1. Display Information of Sequences: ')
    print('2. Choose sequence to work with (generation): ')
    print('3. EXIT:', '\n')
    time.sleep(4)
    print('Attempts = 5\n')
    time.sleep(2)
    

    j=0
    try:
        ch1=int(input('Please enter a choice (1-3): '))                                     # Choosing of operation to perform:
        time.sleep(2)
        for i in range(0,5):                                                                # Gives user 5 attempts to enter a number in the range (1-3):
            if ch1<1:
                time.sleep(1)
                print('Your choice is less than 1.')
                time.sleep(1)
                ch1=int(input('Please enter a numerical choice in the range (1-3): '))
                j+=1
            elif ch1>3:
                time.sleep(1)
                print('Your choice is greater than 3.')
                time.sleep(1)
                ch1=int(input('Please enter a numerical choice in the range (1-3): '))
                j+=1
            elif ch1==1:
                break
            elif ch1==2:
                break
            elif ch1==3:
                #print('Thank you for visiting! ')
                #sys.exit()
                #break
                pass
            if j==4:
                time.sleep(1)
                end=time.perf_counter()
                time1=end-start
                print('Maximum no. of attempts crossed, program exiting.                                              > Time elapsed:',time1,'seconds')
                time.sleep(1)
                sys.exit()
    except ValueError:                                                                        # If data type other than an integer is inputed: (exits program)
        time.sleep(1)
        end=time.perf_counter()
        time1=end-start
        print('Wrong input, program exiting.                                                                > Time elapsed:', time1,'seconds')
        time.sleep(1)
        sys.exit()

    if ch1==1:                                                                                # may have to remove this part for neatness
        print('\n--> Your choice is (1. Display Information of Sequences: )\n')
    elif ch1==2:
        print('\n--> Your choice is (2. Choose sequence to work with (generation): )\n')
    elif ch1==3:
        print('\n--> Your choice is (3. EXIT: )\n')
    time.sleep(3)







# WHAT TO DO DEPENDING ON THE INPUTS:

# (i) choice 1 for INFO DISPLAY:
   
    #from askchoice2 import ask_choice2                                                       # main choice
    #from askchoice1 import ask_choice1                                                       # sub choice (may not be required)
    

# starts here

    if ch1==1:                                                                                # choice for DFH information display
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        print('(S_no:', ' Sequence Name:', ' Year of Discovery:)', sep=' ', end='\n')
        time.sleep(2)
        query=('select * from sequences')                                                     # prints table 
        cur.execute(query)
        data1=cur.fetchall()
        for i in data1:
            time.sleep(1)
            print(i,'\n')
        time.sleep(2)
        r=cur.rowcount                                                                        # counts no. of rows retrieved
        print("- Here, you'll get to know the information, history and why these sequences are important.(?) ")
        time.sleep(3)

        
        while True:                                                                             # while loop(secondary/sub) for program to ask for user input to perform operations until EXIT is pressed. 

            k=0
            print('\nEnter a choice when prompted corresponding to the serial number of each sequence ( 1 -', r,') :')                    # range as per no. of rows retrieved
            time.sleep(2.5)
            try:
                ch2=int(input('Please enter choice here: '))
                time.sleep(1)
                for i in range(0,5):                                                                # Gives user 5 attempts to enter a number in the range (1-3):
                    if ch2<1:
                        time.sleep(1)
                        print('Your choice is less than 1.')
                        time.sleep(1)
                        ch2=int(input('Please enter a numerical choice in the range (1-6): '))
                        k+=1
                    elif ch2>6:
                        time.sleep(1)
                        print('Your choice is greater than 3.')
                        time.sleep(1)
                        ch2=int(input('Please enter a numerical choice in the range (1-6): '))
                        k+=1
                    elif ch2==1:
                        pass
                    elif ch2==2:
                        pass
                    elif ch2==3:
                        pass
                    elif ch2==4:
                        pass
                    elif ch2==5:
                        pass
                    elif ch2==6:
                        pass
                    if j==4:
                        time.sleep(1)
                        end=time.perf_counter()
                        time1=end-start
                        print('Maximum no. of attempts crossed, program exiting.                                              > Time elapsed:',time1,'seconds')
                        time.sleep(1)
                        sys.exit()
##                      else:
##                          sys.exit()
            except ValueError:                                                                      # If data type other than an integer is inputed: (exits program)
                time.sleep(1)
                end=time.perf_counter()
                time1=end-start
                print('Wrong input, program exiting.                                                                > Time elapsed:', time1,'seconds')
                time.sleep(1)
                sys.exit()

            print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
            time.sleep(3)


            if ch2==1:                                                                                                   # FIRST SEQUENCE
                file1=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fibonaccinumbers.txt','r')
                r1=file1.readlines()
                for i in r1:
                    print(i.strip())                       # or rstrip()
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(12)
                y=ask_choice2()                            # ask_choice2()[0] (return value as tuple)    NVM
                if y==1:                                   # to get the first element in the tuple (ch3) of the return value for the function
                    break
                elif y==2:                                 # this elif statement is being executed when ch2 is not 1:, problem to check:
                    continue                               # this statement has to be made to go back to the starting of second while loop, check PROGRAMWIZ CONTINUE STATEMENT

           

            elif ch2==2:                                                                                                 # SECOND SEQUENCE
                file2=open('C:/Users/sibik/OneDrive/Desktop/computer project files/prime numbers.txt','r')
                r2=file2.readlines()
                for i in r2:
                    print(i.strip())
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(20)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue

                

            elif ch2==3:                                                                                                 # THIRD SEQUENCE
                file3=open('C:/Users/sibik/OneDrive/Desktop/computer project files/collatz sequence.txt','r')
                r3=file3.readlines()
                for i in r3:
                    print(i.strip())
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(20)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue

                

            elif ch2==4:                                                                                                # FOURTH SEQUENCE
                file4=open('C:/Users/sibik/OneDrive/Desktop/computer project files/pascal triangle numbers.txt','r')     
                r4=file4.readlines()
                for i in r4:
                    print(i.strip())
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(20)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue

                
  
            elif ch2==5:                                                                                                # FIFTH SEQUENCE
                file5=open('C:/Users/sibik/OneDrive/Desktop/computer project files/pentagonal numbers.txt','r')           
                r5=file5.readlines()
                for i in r5:
                    print(i.strip())
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(15)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue

                

            elif ch2==6:                                                                                                # SIXTH SEQUENCE
                file6=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fermat numbers.txt','r')               
                r6=file6.readlines()
                for i in r6:
                    print(i.strip())
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(20)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue



# just instantiate the ch3 value else only the file 1 will be printed and others will not due to the else statement for the continue as in line with "if ch3==1:"



# (ii) choice 2 for SEQUENCE GENERATION:    # need to do for trigonal sequence:

    # from fibonaccifunction import fibonacci_n
    # from fibonaccifunction(user) import fibonacci
    # from primenumbersfunction import prime
    # from collatzfunction import collatz
    # from fermatfunction import fermat
    # from fermatprimefunction import is_prime, collatz_prime


# starts here

    elif ch1==2:
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        time.sleep(1.5)
        print('Here, you can generate any of the given sequences. ')
        time.sleep(2)
        print('1. Fibonacci Numbers ')
        time.sleep(1)
        print('2. Prime Numbers ')
        time.sleep(1)
        print('3. Collatz Sequence ')
        time.sleep(1)
        print('4. Pascal Triangle Numbers ')
        time.sleep(1)
        print('5. Pentagonal Numbers ')
        time.sleep(1)
        print('6. Fermat Numbers ')
        time.sleep(1)

        while True:
            time.sleep(2)
            print('Please enter choice when prompted. ')
            time.sleep(2)
            m=0
            try:
                ch4=int(input('Please enter choice for the sequence you wish to generate: '))
                for i in range(0,5):
                    if ch4==1:
                        pass
                    elif ch4==2:
                        pass
                    elif ch4==3:
                        pass
                    elif ch4==4:
                        pass
                    elif ch4==5:
                        pass
                    elif ch4==6:
                        pass
                    elif ch4<1:
                        time.sleep(1)
                        print('Your choice is less than 1.')
                        time.sleep(1)
                        ch4=int(input('Please enter a numerical choice in the range (1-6): '))
                        m+=1
                    elif ch4>6:
                        time.sleep(1)
                        print('Your choice is more than 6.')
                        time.sleep(1)
                        ch4=int(input('Please enter a numerical choice in the range (1-6): '))
                        m+=1
                    if m==4:
                        time.sleep(1)
                        end=time.perf_counter()
                        time1=end-start
                        print('Maximum no. of attempts crossed, program exiting.                                              > Time elapsed:',time1,'seconds')
                        time.sleep(1)
                        sys.exit()
    ##                else:
    ##                    sys.exit()
            except ValueError:
                time.sleep(1)
                end=time.perf_counter()
                time1=end-start
                print('Wrong input, program exiting.                                                                > Time elapsed:', time1,'seconds')
                time.sleep(1)
                sys.exit()

            time.sleep(1)
            print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
            time.sleep(3)

            if ch4==1:                                              # Fibonacci Sequence
                from fibonaccifunction import fibonacci_n
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue

            elif ch4==2:                                            # Prime Numbers
                from primenumbersfunction import prime
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue

            elif ch4==3:                                            # Collatz Sequence
                from collatzfunction import collatz
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue

            elif ch4==4:                                            # Pascal triangle numbers (need to find logic print)
                print('Not updated.')
                time.sleep(2)
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue                                              

            elif ch4==5:
                from pentagonalnumbers import pentagonal
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue

            elif ch4==6:                                            # Fermat Numbers
                from fermatfunction import fermat
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue

            
                

# (iii) choice 3 for EXITING: (All exit points other than the input error ones have the suggestion and file transcript functions):           
                
            
    elif ch1==3:
        suggestion()                                                                # SUGGESTION usage before defined, might give error
        time.sleep(2)

##        send_windowtranscript()
##        time.sleep(2)
        send_text()
        time.sleep(2)
##        send_text_multilinestring()
##        time.sleep(2)

##        send_infotranscript()
##        time.sleep(2)
##        send_direct()
##        time.sleep(2)
        send_multilinestring()
        time.sleep(2)
        end=time.perf_counter()
        time1=end-start
        print('\nThank you for visiting!                                                                        > Time elapsed:',time1,'seconds')
        time.sleep(1)
        sys.exit()




#____________________________________________________________________________________________________________________________________________________
        
