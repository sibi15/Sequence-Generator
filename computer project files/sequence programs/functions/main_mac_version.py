# main program:

# Sequence info transcipt is via MULTI-LINE STRING
# Shell transcript is via TEXT FILE

# LESS SECURE APPS link:
#https://myaccount.google.com/u/2/lesssecureapps?pli=1&rapt=AEjHL4Pt00WJObL2Gz1gyIyS-pjTd7FOgqspqLjlPWRZTqL6BI4zGG_6i-N0gjT-O4D00GWwMIKBLkYaMBfrzQ0IitJglwKyvw

import mysql.connector
from time import perf_counter, sleep
import time
import pyttsx3
start=time.perf_counter()                      # time complexity of program

import sys
import ssl
import smtplib
import csv

# CONNECTION AND CURSOR OBJECT INSTANTIATION:
con=mysql.connector.connect(host='localhost', user='root', password='', database='test')
cur=con.cursor()

#                                              Description of user-defined functions used in project:
#____________________________________________________________________________________________________________________________________________________

# ask_choice2           ---> Going back to seqeunce info or main choice
# ask_choice3           ---> Going back to sequence generation or main choice
# ask_speak             ---> Asking the user for a speaker for the sequence information
# suggestion            ---> To add suggestion of a sequence to MySQL
# suggestion_csv        ---> To add suggestion of a sequence to a CSV file
# improvement_review    ---> To give suggestions of improvement or reviews (CSV File)

# SHELL 
    # send_windowtranscript     ---> 
    # (*) send_text             ---> sending the window transcript by writing onto a TEXT file
    # send_text_multilinestring ---> send the multi-line string directly

# INFO:
    # send_infotranscript       ---> Line-by-line info send
    # send_direct               ---> send direct file
    # (*) send_multilinestring  ---> send via multilinestring

#____________________________________________________________________________________________________________________________________________________

                                                                    # CHOICES:


def ask_choice2():                                             
    print('\nOptions:')                                              
    print('1. Go back to main choice: ')
    print('2. Go back to sequence information choices: ')
    print('3. EXIT: ')
    time.sleep(1)
    k=0
    try:
        ch3=int(input('Please enter a choice (1-3): '))
        for i in range(0,5):
            if ch3<1:
                time.sleep(1)
                print('Your choice is less than 1.')
                ch3=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch3>3:
                time.sleep(1)
                print('Your choice is greater than 3.')
                ch3=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch3==1:
                pass
            elif ch3==2:
                pass
            elif ch3==3:
                suggestion()
                #suggestion.csv()
                #improvement_review()
                #send_windowtranscript()
                send_text()
                #send_text_multilinestring()
                #send_infotranscript()
                #send_direct()
                send_multilinestring()
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
                sys.exit()
    except ValueError:
        end=time.perf_counter()
        time1=end-start
        print('Wrong input, program exiting.                                                                > Time elapsed:', time1,'seconds')
        time.sleep(1)
        sys.exit()
    return ch3

def ask_choice3():                                            
    print('\nOptions:')
    print('1. Go back to main choice: ')
    print('2. Go back to sequence generation choices: ')
    print('3. EXIT: ')
    time.sleep(1)
    k=0
    try:
        ch5=int(input('Please enter a choice in the range (1-3): '))
        for i in range(0,5):
            if ch5<1:
                time.sleep(1)
                print('Your choice is less than 1. ')
                ch5=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch5>3:
                time.sleep(1)
                print('Your choice is greater than 3. ')
                ch5=int(input('Please enter a numerical choice in the range (1-3): '))
                k+=1
            elif ch5==1:
                pass
            elif ch5==2:
                pass
            elif ch5==3:
                suggestion()
                #suggestion.csv()
                #improvement_review()
                #send_windowtranscript()
                send_text()
                #send_text_multilinestring()
                #send_infotranscript()
                #send_direct()
                send_multilinestring()
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
                sys.exit()
    except ValueError:
        end=time.perf_counter()
        time1=end-start
        print('Wrong input, program exiting.                                                                > Time elapsed:', time1,'seconds')
        time.sleep(1)
        sys.exit()
    return ch5

def ask_speak():
    speaker=input('\nSPEAKER: Would you like a speaker for the sequence information? (y/n): ')
    if speaker=='n':
        pass
    elif speaker=='y':
        pass
    else:
        print('Please enter a valid choice:')
        ask_speak()
    return speaker

#____________________________________________________________________________________________________________________________________________________

                                                                # SUGGESTION:

                                                      
def suggestion():
    sug=input('\nSUGGESTION: Would you like to provide a suggestion for a sequence to add? (y/n): ')
    if sug=='y':
        n=int(input('Please enter the no. of suggestions you want to provide: '))
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
        suggestion()

def suggestion_csv():
      sug=input('\nSUGGESTION: Would you like to provide a suggestion for a sequence to add? (y/n): ')
      if sug=='y':
          with open('suggestions.csv', mode='r') as f:
                r=csv.reader(f, delimiter=',')
                count=0
                for row in r:
                    if len(row)!=0:
                        count+=1
                    else:
                        pass
          with open('suggestion.csv', mode='a') as f:
                w=csv.writer(f,delimiter=',')
                n=int(input('Please input no. of suggestions you wish to provide: '))
                for i in range(1,n+1):
                      serial_num=str(count+i)+'.'
                      suggestion=input('Enter sequence name: ')
                      w.writerow([serial_num,suggestion])
                print('Suggestions received. Thank you!')
      elif sug=='n':
          pass
      else:
          print('Wrong input, try again. \n')
          suggestion_csv()

#____________________________________________________________________________________________________________________________________________________

                                                # IMPROVEMENTS or REVIEWS (Suggestions on project) (CSV):

def improvement_review():
    imp=input('\nIMPROVEMENTS / REVIEWS: Would you like to give a review or provide a suggestion of improvement? (y/n): ')
    if imp=='y':
        with open('improvements_reviews.csv', mode='r') as f:
            r=csv.reader(f, delimiter=',')
            count=0
            for row in r:
                if len(row)!=0:
                    count+=1
                else:
                    pass
        with open('improvements_reviews.csv', mode='w') as f:
            w=csv.writter(f, delimiter=',')
            serial_num=str(count+1)+'.'
            name=input('Enter your name (OPTIONAL): ')
            imp_review=input('Type in your improvement suggestions or reviews: ')
            w.write_row([serial_num,name,imp_review])
            print('Reviews received. Thank you!')      
    elif imp=='n':
        pass
    else:
        print('Wrong input, try again. \n')
        improvement_review()

#____________________________________________________________________________________________________________________________________________________

                                                            # TRANSCRIPT 1: SHELL WINDOW:

def send_windowtranscript():
    tr1=input('\nTRANSCRIPT 1: Would you like to receive a mail regarding the transcript of the shell window? (y/n): ')
    if tr1=='n':
        pass
    elif tr1=='y':
        # OLD Mailing Method:
        #port=465
        #smtp_server="smtp.gmail.com"
        #sender_email=""
        #password="" # "upge gpcx oqxe vvpm"
        #context=ssl.create_default_context()
        #for i in range(1,n+1):
        #    context=ssl.create_default_context()
        #    receiver_email=input('Please enter email address to send the shell window transcript to: ')
        #    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #       print('Sending mail',i)
        #       #try:
        #       server.login(sender_email, password)
        #        server.sendmail(sender_email, receiver_email, message)
        #        #except SMTPAuthenticationError:
        #        print('Mail sent.\n')
        #        server.quit()
        #print('Mail to the addresses sent.\n') """
        
        sender_id=''
        passwd=''
        n=int(input('Enter no. of mails to be sent to the same, or different addresses: '))
        message=input('Please copy the text in the shell window above, paste it here and enter: ')
        subject='Shell Window Transcript'
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender_id,passwd)
        for i in range(1,n+1):
            receiver_id=input('\nPlease enter email address to send the shell window transcript to: ')
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % subject,
                    '', message])
            server.sendmail(sender_id, [receiver_id], body)
            print('Mail sent.\n')
        server.quit()
        print('Mail to the address sent.\n')
    else:
        print('Wrong input, try again. \n')
        send_windowtranscript()

# TWO DIFFERENT FUNCTIONS for sending the shell window transcript (CSV FILE and MULTI-LINE STRING):

# (i) TEXT FILE:

def send_text():
    time.sleep(1)
    tr1=input('\nTRANSCRIPT 1: Would you like to receive a mail regarding the transcript of the shell window? (y/n): ')
    if tr1=='n':
        pass
    elif tr1=='y':
        n=int(input('Enter the no. of mails to be sent to the same, or different addresses: '))
        print('Please follow the following instructions: ')
        print('\nCopy the text in the shell window above, paste it after this line when prompted and ENTER. Then when the cursor is at the starting of the next line, please press CTRL+D: ')
        time.sleep(1)
        text=sys.stdin.read()
        shell_w=open('/Users/sibikarthik/Desktop/python projects/computer project files/shellwindow.txt','w')
        shell_w.write(text)
        shell_w.close()
        shell_r=open('/Users/sibikarthik/Desktop/python projects/computer project files/shellwindow.txt','r')
        time.sleep(1)
        shell_r=shell_r.read()

        # OLD Mailing Method:
        #port=465
        #smtp_server="smtp.gmail.com"
        #sender_email=""
        #password="" # "upge gpcx oqxe vvpm"
        #for i in range(1,n+1):
        #    context=ssl.create_default_context()
        #    receiver_email=input('\nPlease enter email address to send the shell window transcript to: ')
        #    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #        print('Sending mail to mail address', i)
        #        server.login(sender_email, password)
        #        server.sendmail(sender_email, receiver_email, shell_r)
        #        print('Mail sent.\n')
        #        server.quit()
        #print('Mail to the address sent.\n')

        # MAC METHOD:
        sender_id=''
        passwd=''
        subject='Shell Window Transcript'
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender_id,passwd)
        for i in range(1,n+1):
            receiver_id=input('\nPlease enter email address to send the shell window transcript to: ')
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % subject,
                    '', shell_r])
            server.sendmail(sender_id, [receiver_id], body)
            print('Mail sent.\n')
        server.quit()
        print('Mail to the address sent.\n')

    else:
        print('Wrong input, try again. \n')
        send_text()

# (ii) DIRECT MULTI-LINE string send after reading from NOTEPAD File:

def send_text_multilinestring():
    tr2=input('\nTRANSCRIPT 1: Would you like to receive a mail regarding the transcript of the shell window? (y/n): ')
    if tr2=='n':
        pass
    elif tr2=='y':
        n=int(input('Enter the no. of mails to be sent to the same, or different addresses: '))
        print('Please follow the following instructions: ')
        print('\nPlease copy the text in the shell window above, paste it after this line when prompted and ENTER. Then when the cursor is at the starting of the next line, please press CTRL+D: ')
        time.sleep(1)
        text=sys.stdin.read()
        shell_w=open('/Users/sibikarthik/Desktop/python projects/computer project files/shellwindow.txt','w')
        shell_w.write(text)
        shell_w.close()
        text=''''''
        shell_r=open('/Users/sibikarthik/Desktop/python projects/computer project files/shellwindow.txt','r')
        ime.sleep(1)
        shell_r=shell_r.read()
        text=text+shell_r

        # OLD Mailing Method:
        #port=465
        #smtp_server="smtp.gmail.com"
        #sender_email=""
        #password=""
        #for i in range(1,n+1):
        #    context=ssl.create_default_context()
        #    receiver_email=input('\nPlease enter email address to send the shell window transcript to: ')
        #    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #        print('Sending mail to mail address', i)
        #        server.login(sender_email, password)
        #        server.sendmail(sender_email, receiver_email, text)
        #        print('Mail sent.\n')
        #        server.quit()
        #print('Mail to the address sent.\n')
        
        # MAC METHOD:
        sender_id=''
        passwd=''
        subject='Shell Window Transcript'
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender_id,passwd)
        for i in range(1,n+1):
            receiver_id=input('\nPlease enter email address to send the shell window transcript to: ')
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % subject,
                    '', text])
            server.sendmail(sender_id, [receiver_id], body)
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
    tr3=input('\nTRANSCRIPT 2: Would you like a mail regarding the transcript of the sequence information? (y/n): ')
    if tr3=='n':
        pass
    elif tr3=='y':
        n=int(input('Enter no. of mails to be sent to the same, or different addresses: '))
        print('\nNOTE: You will be getting a no. of mails for each of the sequences and maybe also the same sequence as parts because of the word limit constraint while sending\n')
        
        #port=465
        #smtp_server="smtp.gmail.com"
        #sender_email=""
        #password=""
        #file1=open('/Users/sibikarthik/Desktop/python projects/computer project files/fibonaccinumbers.txt','r')
        #r1=file1.readlines()
        #file2=open('/Users/sibikarthik/Desktop/python projects/computer project files/prime numbers.txt','r')
        #r2=file2.readlines()
        #file3=open('/Users/sibikarthik/Desktop/python projects/computer project files/collatz sequence.txt','r')
        #r3=file3.readlines()
        #file4=open('/Users/sibikarthik/Desktop/python projects/computer project files/pascal triangle numbers.txt','r')     
        #r4=file4.readlines()
        #file5=open('/Users/sibikarthik/Desktop/python projects/computer project files/pentagonal numbers.txt','r')           
        #r5=file5.readlines()
        #file6=open('/Users/sibikarthik/Desktop/python projects/computer project files/fermat numbers.txt','r')               
        #r6=file6.readlines()
        
        #for i in range (1,n+1):
        #    context=ssl.create_default_context()
        #    receiver_email=input('Please enter email address to send the shell window transcript to: ')
        #    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #        print('Sending mail to address',i)
        #        server.login(sender_email, password)
        #        for j in r1:
        #            message=j.strip()
        #            server.sendmail(sender_email, receiver_email, message)
        #        print('Mail for sequence 1 sent.')
        #        file1.close()
        #        for j in r2:
        #            message=j.strip()
        #            server.sendmail(sender_email, receiver_email, message)
        #        print('Mail for sequence 2 sent.')
        #        file2.close()
        #        for j in r3:
        #            message=j.strip()
        #            server.sendmail(sender_email, receiver_email, message)
        #        print('Mail for sequence 3 sent.')
        #        file3.close()
        #        for j in r4:
        #            message=j.strip()
        #            server.sendmail(sender_email, receiver_email, message)
        #        print('Mail for sequence 4 sent.')
        #        file4.close()
        #        for j in r5:
        #            message=j.strip()
        #            server.sendmail(sender_email, receiver_email, message)
        #        print('Mail for sequence 5 sent.')
        #        file5.close()
        #        for j in r6:
        #            message=j.strip()
        #            server.sendmail(sender_email, receiver_email, message)
        #        print('Mail for sequence 6 sent.\n')
        #        file6.close()
        #        server.quit()
        #print('> Mail to the inputed', n, 'addresses sent.\n')
        
        
    else:
        print('Wrong input, try again. \n')
        send_infotranscript()


# TWO DIFFERENT FUNCTIONS for Notepad file sending (DIRECT and MULTI-LINE STRING):

# (i) DIRECT:

def send_direct():
    tr4=input('\nTRANSCRIPT 2: Would you like a mail regarding the transcript of the sequence information? (y/n): ')
    if tr4=='n':
        pass
    elif tr4=='y':
        n=int(input('Enter no. of mails to be sent to the same, or different addresses: '))
        
        # OLD Mailing method:
        #port=465
        #smtp_server="smtp.gmail.com"
        #sender_email=""
        #password=""
        
        #for i in range(1,n+1):
        #    context=ssl.create_default_context()
        #    receiver_email=input('Please enter email address to send the shell window transcript to: ')
        #    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #        print('Sending files to address', i)
        #        server.login(sender_email, password)

        #        message1=open('/Users/sibikarthik/Desktop/python projects/computer project files/fibonaccinumbers.txt','r')
        #        message1=message1.read()
        #        server.sendmail(sender_email, receiver_email, message1)
        #        print('SEQUENCE 1 sent.')

        #        message2=open('/Users/sibikarthik/Desktop/python projects/computer project files/prime numbers.txt','r')
        #        message2=message2.read()
        #        server.sendmail(sender_email, receiver_email, message2)
        #        print('SEQUENCE 2 sent.')

        #        message3=file3=open('/Users/sibikarthik/Desktop/python projects/computer project files/collatz sequence.txt','r')
        #        message3=message3.read()
        #        server.sendmail(sender_email, receiver_email, message3)
        #        print('SEQUENCE 3 sent.')
                
        #        message4=open('/Users/sibikarthik/Desktop/python projects/computer project files/pascal triangle numbers.txt','r')     
        #        message4=message4.read()
        #        server.sendmail(sender_email, receiver_email, message4)
        #        print('SEQUENCE 4 sent.')
                
        #        message5=open('/Users/sibikarthik/Desktop/python projects/computer project files/pentagonal numbers.txt','r')           
        #        message5=message5.read()
        #        server.sendmail(sender_email, receiver_email, message5)
        #        print('SEQUENCE 5 sent.')
                      
        #        message6=open('/Users/sibikarthik/Desktop/python projects/computer project files/fermat numbers.txt','r')               
        #        message6=message6.read()
        #        server.sendmail(sender_email, receiver_email, message6)
        #        print('SEQUENCE 6 sent.\n')

        #        print('Mails sent for address', i)
        #        server.quit()
        #print('\nAll mails sent.')
        
        # MAC METHOD:
        sender_id=''
        passwd=''
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender_id,passwd)
        for i in range(1,n+1):
            receiver_id=input('\nPlease enter email address to send the shell window transcript to: ')
            print('Sending files to address', i)
            
            message1=open('/Users/sibikarthik/Desktop/python projects/computer project files/fibonaccinumbers.txt','r')
            message1=message1.read()
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 1',
                    '', message1])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 1 sent.')

            message2=open('/Users/sibikarthik/Desktop/python projects/computer project files/prime numbers.txt','r')
            message2=message2.read()
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 2',
                    '', message2])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 2 sent.')

            message3=open('/Users/sibikarthik/Desktop/python projects/computer project files/collatz sequence.txt','r')
            message3=message3.read()
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 3',
                    '', message3])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 3 sent.')

            message4=open('/Users/sibikarthik/Desktop/python projects/computer project files/pascal triangle numbers.txt','r')
            message4=message4.read()
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 4',
                    '', message4])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 4 sent.')

            message5=open('/Users/sibikarthik/Desktop/python projects/computer project files/pentagonal numbers.txt','r')
            message5=message5.read()
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 5',
                    '', message5])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 5 sent.')

            message6=open('/Users/sibikarthik/Desktop/python projects/computer project files/fermat numbers.txt','r')
            message6=message6.read()
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 6',
                    '', message6])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 6 sent.')

            print('Mails sent for address', i)
        server.quit()
        print('\nAll mails sent.')
        
    else:
        print('Wrong input, try again. \n')
        send_direct()


# (ii) MULTI-LINE string:

def send_multilinestring():
    tr5=input('\nTRANSCRIPT 2: Would you like a mail regarding the transcript of the sequence information? (y/n): ')
    if tr5=='n':
        pass
    elif tr5=='y':
        n=int(input('Enter no. of mails to be sent to the same, or different addresses: '))

        #port=465
        #smtp_server="smtp.gmail.com"
        #sender_email="04250@asianintlschool.com"
        #password="sibikarthik260104"
        
        #for i in range(1,n+1):
            #context=ssl.create_default_context()
            #receiver_email=input('Please enter email address to send the shell window transcript to: ')
            #with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                #print('Sending files to address', i)
                #server.login(sender_email, password)

                #m1=''''''
                #message1=open('/Users/sibikarthik/Desktop/python projects/computer project files/fibonaccinumbers.txt','r')
                #message1=message1.read()
                #m1=m1+message1
                #server.sendmail(sender_email, receiver_email, m1)
                #print('SEQUENCE 1 sent.')

                #m2=''''''
                #message2=open('/Users/sibikarthik/Desktop/python projects/computer project files/prime numbers.txt','r')
                #message2=message2.read()
                #m2=m2+message2
                #server.sendmail(sender_email, receiver_email, m2)
                #print('SEQUENCE 2 sent.')

                #m3=''''''
                #message3=open('/Users/sibikarthik/Desktop/python projects/computer project files/collatz sequence.txt','r')
                #message3=message3.read()
                #m3=m3+message3
                #server.sendmail(sender_email, receiver_email, m3)
                #print('SEQUENCE 3 sent.')

                #m4=''''''
                #message4=open('/Users/sibikarthik/Desktop/python projects/computer project files/pascal triangle numbers.txt','r')     
                #message4=message4.read()
                #m4=m4+message4
                #server.sendmail(sender_email, receiver_email, m4)
                #print('SEQUENCE 4 sent.')

                #m5=''''''
                #message5=open('/Users/sibikarthik/Desktop/python projects/computer project files/pentagonal numbers.txt','r')           
                #message5=message5.read()
                #m5=m5+message5
                #server.sendmail(sender_email, receiver_email, m5)
                #print('SEQUENCE 5 sent.')

                #m6=''''''
                #message6=open('/Users/sibikarthik/Desktop/python projects/computer project files/fermat numbers.txt','r')               
                #message6=message6.read()
                #m6=m6+message6
                #server.sendmail(sender_email, receiver_email, m6)
                #print('SEQUENCE 6 sent.\n')

        # MAC METHOD:
        sender_id=''
        passwd=''
        
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender_id,passwd)
        
        for i in range(1,n+1):
            receiver_id=input('\nPlease enter email address to send the shell window transcript to: ')
            print('Sending files to address', i)

            m1=''''''
            message1=open('/Users/sibikarthik/Desktop/python projects/computer project files/fibonaccinumbers.txt','r')
            message1=message1.read()
            m1=m1+message1
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 1',
                    '', m1])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 1 sent.')

            m2=''''''
            message2=open('/Users/sibikarthik/Desktop/python projects/computer project files/prime numbers.txt','r')
            message2=message2.read()
            m2=m2+message2
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 2',
                    '', m2])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 2 sent.')

            m3=''''''
            message3=open('/Users/sibikarthik/Desktop/python projects/computer project files/collatz sequence.txt','r')
            message3=message3.read()
            m3=m3+message3
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 3',
                    '', m3])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 3 sent.')

            m4=''''''
            message4=open('/Users/sibikarthik/Desktop/python projects/computer project files/pascal triangle numbers.txt','r')
            message4=message4.read()
            m4=m4+message4
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 4',
                    '', m4])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 4 sent.')

            m5=''''''
            message5=open('/Users/sibikarthik/Desktop/python projects/computer project files/pentagonal numbers.txt','r')
            message5=message5.read()
            m5=m5+message5
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 5',
                    '', m5])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 5 sent.')

            m6=''''''
            message6=open('/Users/sibikarthik/Desktop/python projects/computer project files/fermat numbers.txt','r')
            message6=message6.read()
            m6=m6+message6
            body='\r\n'.join(['To: %s' % receiver_id,
                    'From: %s' % sender_id,
                    'Subject: %s' % 'SEQUENCE 6',
                    '', m6])
            server.sendmail(sender_id, [receiver_id], body)
            print('SEQUENCE 6 sent.')

            print('Mails sent for address', i)
        server.quit()
        print('\nAll mails sent.')
    else:
        print('Wrong input, try again. \n')
        send_multilinestring()
        

#____________________________________________________________________________________________________________________________________________________
        
    
                                                                    #INTRODUCTION:

                                                                    

time.sleep(0.5)
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
time.sleep(0.5)
print('                                                            ----- SEQUENCE GENERATOR -----\n')
time.sleep(0.5)
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
time.sleep(0.5)
print('----------------------------------------------------------------------------------------------------')
time.sleep(0.5)
print('| * NOTE:                                                                                          |')
time.sleep(0.5)
print('| - When the program asks for your input, please type the input and press the ENTER key.           |')
time.sleep(0.5)
print("| - If you want to exit the program immediately at any point, use the command 'CTRL+C'.     |")
time.sleep(0.5)
print('----------------------------------------------------------------------------------------------------\n')
time.sleep(0.5)

print('Options:')
time.sleep(0.5)
print('      |')
print('      |')
time.sleep(0.5)
print('      |---> 1. SEQUENCE INFORMATION')
time.sleep(0.5)
print('      |')
print('      |')
time.sleep(0.5)
print('      |---> 2. SEQUENCE GENERATION')
time.sleep(0.5)
print('      |')
print('      |')
time.sleep(0.5)
print('      |---> 3. EXIT')
time.sleep(0.5)
print('                  |')
print('                  |')
time.sleep(0.5)
print('                  |---> SUGGESTION TO ADD SEQUENCES')
time.sleep(0.5)
#print('                  |---> REVIEWS / SUGGESTIONS')
#time.sleep(0.5)
print('                  |---> FILE TRANSCRIPT')
time.sleep(0.5)
print('                                      |')
print('                                      |')
time.sleep(0.5)
print('                                      |---> Shell Window (copy and paste)')
time.sleep(0.5)
print('                                                       |')
print('                                                       |')
time.sleep(0.2)
print('                                                       |---> Direct TEXT file sending')
print('                                                       |---> Multi-line string from TEXT file\n')
time.sleep(1)
print('                                      |---> Briefs of sequences')
time.sleep(0.5)
print('                                                       |')
print('                                                       |')
time.sleep(0.2)
print('                                                       |---> Line-by-line sending')
print('                                                       |---> Direct TEXT file sending')
print('                                                       |---> Multi-line string\n')
time.sleep(2)

time.sleep(1)
print('- The following is the table of sequences within which you may ask the given operations to be performed: ', '\n')
time.sleep(0.5)
print('(S_no:', ' Sequence Name:', ' Year of Discovery:)', sep=' ', end='\n')
time.sleep(0.5)

query=('select * from sequences')              
cur.execute(query)
data1=cur.fetchall()
#print('\n')
for i in data1:
    time.sleep(1)
    print(i,'\n')
time.sleep(1)
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')



# USER INPUT:

while True:                                                                 # This is for the choice twice back or once back (corresponds to the breaks)

    print('\nOperations: ')
    time.sleep(1)

    print('1. Display Information of Sequences: ')
    print('2. Choose sequence to work with (generation): ')
    print('3. EXIT:', '\n')
    time.sleep(0.5)
    print('Attempts = 5\n')
    time.sleep(1)
    
    j=0
    try:
        ch1=int(input('Please enter a choice (1-3): '))                     # Choosing of operation to perform:
        
        for i in range(0,5):                                                # Gives user 5 attempts to enter a number in the range (1-3):
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
    except ValueError:                                                              # If data type other than an integer is inputed: (exits program)
        time.sleep(1)
        end=time.perf_counter()
        time1=end-start
        print('Wrong input, program exiting.                                                                > Time elapsed:', time1,'seconds')
        time.sleep(1)
        sys.exit()

    #if ch1==1:                                                                                # may have to remove this part for neatness
    #    print('\n--> Your choice is (1. Display Information of Sequences: )\n')
    #elif ch1==2:
    #    print('\n--> Your choice is (2. Choose sequence to work with (generation): )\n')
    #elif ch1==3:
    #    print('\n--> Your choice is (3. EXIT: )\n')
    #time.sleep(1.5)




# WHAT TO DO DEPENDING ON THE INPUTS:

# (i) choice 1 for INFO DISPLAY:
   

# starts here

    if ch1==1:                                                                                # choice for DFH information display
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        print('(S_no:', ' Sequence Name:', ' Year of Discovery:)', sep=' ', end='\n')
        time.sleep(1)
        query=('select * from sequences')                                                     # prints table 
        cur.execute(query)
        data1=cur.fetchall()
        for i in data1:
            time.sleep(1)
            print(i,'\n')
        time.sleep(0.5)
        r=cur.rowcount                                                                        # counts no. of rows retrieved
        print("- Here, you'll get to know the information, history and why these sequences are important.(?) \n")
        time.sleep(1.5)


        speaker=ask_speak()
        #if speaker=='y':
        engine=pyttsx3.init()                                                                 # object instantiation of the init class

                
        while True:             # while loop(secondary/sub) for program to ask for user input to perform operations until EXIT is pressed. 

            k=0
            print('\nEnter a choice when prompted corresponding to the serial number of each sequence ( 1 -', r,') :')  # range as per no. of rows retrieved
            time.sleep(1)
            try:
                ch2=int(input('Please enter choice here: '))
                
                for i in range(0,5):                                # Gives user 5 attempts to enter a number in the range (1-3):
                    if ch2<1:
                        time.sleep(1)
                        print('Your choice is less than 1.')
                        time.sleep(1)
                        ch2=int(input('Please enter a numerical choice in the range (1-6): '))
                        k+=1
                    elif ch2>6:
                        time.sleep(1)
                        print('Your choice is greater than 6.')
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
            except ValueError:                  # If data type other than an integer is inputed: (exits program)
                time.sleep(1)
                end=time.perf_counter()
                time1=end-start
                print('Wrong input, program exiting.                                                                > Time elapsed:', time1,'seconds')
                time.sleep(1)
                sys.exit()


            
            voices=engine.getProperty('voices')         # to change male and female voices
            


            print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
            time.sleep(3)


            if ch2==1:                                                                                                   # FIRST SEQUENCE
                file1=open('/Users/sibikarthik/Desktop/python projects/computer project files/fibonaccinumbers.txt','r')
                r1=file1.readlines()
                for i in r1:
                    print(i.strip())                       
                    if speaker=='y':                # speaker variable from ask_speak() defined (user - me)   
                        #text1=file1.read()
                        engine.setProperty('voice', voices[0].id)
                        engine.say(i)
                        engine.runAndWait()
                #engine.stop()
                file1.close()
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                y=ask_choice2()                 # ask_choice2()[0] (return value as tuple)    NVM
                if y==1:                        # to get the first element in the tuple (ch3) of the return value for the function
                    break
                elif y==2:                      # (FIXED) this elif statement is being executed when ch2 is not 1:, problem to check:
                    continue                    # PROGRAMWIZ CONTINUE STATEMENT

           

            elif ch2==2:                                                                                                 # SECOND SEQUENCE
                file2=open('/Users/sibikarthik/Desktop/python projects/computer project files/prime numbers.txt','r')
                r2=file2.readlines()
                for i in r2:
                    print(i.strip())
                    if speaker=='y':  
                        #text2=file2.read()
                        engine.setProperty('voice', voices[1].id)
                        engine.say(i)
                        engine.runAndWait()
                #engine.stop()
                file2.close()
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue

                

            elif ch2==3:                                                                                                 # THIRD SEQUENCE
                file3=open('/Users/sibikarthik/Desktop/python projects/computer project files/collatz sequence.txt','r')
                r3=file3.readlines()
                for i in r3:
                    print(i.strip())
                    if speaker=='y':  
                        #text3=file3.read()
                        engine.setProperty('voice', voices[0].id)
                        engine.say(i)
                        engine.runAndWait()
                #engine.stop()
                file3.close()
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue

                

            elif ch2==4:                                                                                                 # FOURTH SEQUENCE
                file4=open('/Users/sibikarthik/Desktop/python projects/computer project files/pascal triangle numbers.txt','r')     
                r4=file4.readlines()
                for i in r4:
                    print(i.strip())
                    if speaker=='y':      
                        #text4=file4.read()
                        engine.setProperty('voice', voices[1].id)
                        engine.say(i)
                        engine.runAndWait()
                engine.stop()
                file4.close()
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue

                
  
            elif ch2==5:                                                                                                # FIFTH SEQUENCE
                file5=open('/Users/sibikarthik/Desktop/python projects/computer project files/pentagonal numbers.txt','r')           
                r5=file5.readlines()
                for i in r5:
                    print(i.strip())
                    if speaker=='y':  
                        #text5=file5.read()
                        engine.setProperty('voice', voices[0].id)
                        engine.say(i)
                        engine.runAndWait()
                #engine.stop()
                file5.close()
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue

                

            elif ch2==6:                                                                                                # SIXTH SEQUENCE
                file6=open('/Users/sibikarthik/Desktop/python projects/computer project files/fermat numbers.txt','r')               
                r6=file6.readlines()
                for i in r6:
                    print(i.strip())
                    if speaker=='y':  
                        #text6=file6.read()
                        engine.setProperty('voice', voices[1].id)
                        engine.say(i)
                        engine.runAndWait()
                #engine.stop()
                file6.close()
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                y=ask_choice2()
                if y==1:
                    break
                elif y==2:                                 
                    continue



# just instantiate the ch3 value else only the file 1 will be printed and others will not due to the else statement for the continue as in line with "if ch3==1:"



# (ii) choice 2 for SEQUENCE GENERATION:

    # from fibonaccifunction import fibonacci_n
    # from fibonaccifunction(user) import fibonacci
    # from primenumbersfunction import prime
    # from collatzfunction import collatz
    # from fermatfunction import fermat
    # from fermatprimefunction import is_prime, collatz_prime


# starts here

    elif ch1==2:
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        time.sleep(1)
        print('Here, you can generate any of the given sequences. ')
        time.sleep(0.5)
        print('1. Fibonacci Numbers ')
        time.sleep(0.5)
        print('2. Prime Numbers ')
        time.sleep(0.5)
        print('3. Collatz Sequence ')
        time.sleep(0.5)
        print('4. Pascal Triangle Numbers ')
        time.sleep(0.5)
        print('5. Pentagonal Numbers ')
        time.sleep(0.5)
        print('6. Fermat Numbers ')
        time.sleep(0.5)

        while True:
            time.sleep(1)
            print('Please enter choice when prompted. ')
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
                        ch4=int(input('Please enter a numerical choice in the range (1-6): '))
                        m+=1
                    elif ch4>6:
                        time.sleep(1)
                        print('Your choice is more than 6.')
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
            time.sleep(1)

            if ch4==1:                                              # Fibonacci sequence
                from fibonaccifunction import fibonacci_n
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue

            elif ch4==2:                                            # Prime numbers
                from primenumbersfunction import prime
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue

            elif ch4==3:                                            # Collatz sequence
                from collatzfunction import collatz
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue

            elif ch4==4:                                            # Pascal triangle numbers
                  from pascaltriangle import trianglenum
                  print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                  time.sleep(2)
                  z=ask_choice3()
                  if z==1:
                      break
                  elif z==2:
                      continue
                  
            elif ch4==5:                                            # Pentagonal numbers
                from pentagonalnumbers import pentagonal
                print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------')
                time.sleep(2)
                z=ask_choice3()
                if z==1:
                    break
                elif z==2:
                    continue

            elif ch4==6:                                            # Fermat numbers
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
        suggestion()                                                                
        # suggestion.csv()
        time.sleep(1)
        #improvement_review()
        #time.sleep(2)

##        send_windowtranscript()
##        time.sleep(2)
        send_text()
        time.sleep(1)
##        send_text_multilinestring()
##        time.sleep(2)

##        send_infotranscript()
##        time.sleep(2)
##        send_direct()
##        time.sleep(2)
        send_multilinestring()
        time.sleep(1)
        end=time.perf_counter()
        time1=end-start
        print('\nThank you for visiting!                                                                        > Time elapsed:',time1,'seconds')
        time.sleep(1)
        sys.exit()


#____________________________________________________________________________________________________________________________________________________
