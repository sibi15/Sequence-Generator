import ssl
import smtplib
import time
s=''''''

def send_filetranscript(receiver_email, message):
      port=465
      smtp_server="smtp.gmail.com"
      sender_email="04250@asianintlschool.com"
      password="sibikarthik260104"

      context=ssl.create_default_context()
      with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            print('Sending mail')
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

receiver_email=input("Enter receiver mail.")
message=open('C:/Users/sibik/OneDrive/Desktop/computer project files/fibonaccinumbers.txt','r')
message=message.read()
s=s+message
send_filetranscript(receiver_email, s)

