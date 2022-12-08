import ssl
import smtplib
import time

def send_filetranscript(receiver_email, message):
    port=465
    smtp_server="smtp.gmail.com"
    sender_email="04250@asianintlschool.com"
    #receiver_email=''
    password="sibikarthik260104"
    #message=''

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print('Sending mail')
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    

def send_infotranscript(receiver_email, message):
    port=465
    smtp_server="smtp.gmail.com"
    sender_email="04250@asianintlschool.com"
    #receiver_email=''
    password="sibikarthik260104"
    #message=''

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print('Sending mail')
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    


def transcript():
    time.sleep(1)   
    tr=input('Would you like to send a transcript of the code to your mail? (y/n) ')
    time.sleep(2)
    if tr==y:
        c=input('Would you like a transcript of the sequence informations, or the shell window: (i(for info)/s(for shell)) ')
        time.sleep(2)
        n=int(input('Please enter the no. of mails you want to send to the same mail ID or different mail IDs: ')
        time.sleep(1)
        if c==s: 
            for i in range(0,n+1):
                time.sleep(2)
                receiver_email=input('Please enter email address to send the transcript to: ')
                time.sleep(1)
                message=input('Please copy the text in the shell window above, paste it here and enter: ')
                time.sleep(2)
                send_filetranscript(receiver_email, message)
                print('Mail sent\n')
                #send_filetranscript()
                time.sleep(1)
                break
        elif c==i:
            file1=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fibonaccinumbers.txt','r')
            r1=file1.readlines()                                      # add the info transcript
            
        elif tr==n:
            pass
        else:
            print('Wrong input, try again.')
            time.sleep(1)
            transcript()








##time.sleep(2)
##    receiver_email=input('Please enter email address to send the transcript to: ')
##    time.sleep(1)
##    message=input('Please copy the text in the shell window above, paste it here and enter: ')
##    time.sleep(2)
##    send_filetranscript(receiver_email, message)
##    print('Mail sent\n')
##            
            
              
              
              
              
        
        



















# problem with python shell.
# probably because of the 310 limit
# but sends mails for integers but not for words.
# so try like reading lines from notepad files
# and send that.

    
    
