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

time.sleep(2)
receiver_email=input('Please enter email address to send the transcript to: ')
time.sleep(1)
message=input('Please copy the text in the shell window above, paste it here and enter: ')
time.sleep(2)
send_filetranscript(receiver_email, message)
print('Mail sent')
server.quit()

##file1=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fibonaccinumbers.txt','r')   # TEST for the notepad readlines mail
##r1=file1.readlines()
##for i in r1:
##    #print(i.strip())                       # or rstrip()
##    #message=input('Please copy the text in the shell window above, paste it here and enter: ')
##    message=i.strip()
##    time.sleep(2)
##    send_filetranscript(receiver_email, message)
##    print('Mail sent')
##    server.quit()


# TEST PROGRAM TRY FILE.WRITELINE and GET TRANSCRIPT FROM THERE (reading line by line)




# problem with python shell.
# probably because of the 310 limit
# but sends mails for integers but not for words.
# so try like reading lines from notepad files
# and send that.


    
