import ssl
import smtplib

def send_mail():    
    port=465 # SSL
    smtp_server="smtp.gmail.com"
    sender_email="sibikarthik1@gmail.com"
    receiver_email="rajanviji1994@gmail.com"
    password="sibi1234"
    message=""

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print("Sending mail")
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

send_mail()
print('Mail sent')
