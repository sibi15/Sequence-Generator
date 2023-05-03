# TRANSCRIPT 1: Shell Window:
# 1. send_windowscript()
port=465
smtp_server="smtp.gmail.com"
sender_email=""
password=""
context=ssl.create_default_context()
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

# 2. send_text()
port=465
smtp_server="smtp.gmail.com"
sender_email=""
password=""
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
        
# 3. send_text_multilinestring()
port=465
smtp_server="smtp.gmail.com"
sender_email=""
password=""
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


# TRANSCRIPT 2: Sequence Info Files:
# 1. send_infotranscript()
port=465
smtp_server="smtp.gmail.com"
sender_email=""
password=""
file1=open('/Users/sibikarthik/Desktop/python projects/computer project files/fibonaccinumbers.txt','r')
r1=file1.readlines()
file2=open('/Users/sibikarthik/Desktop/python projects/computer project files/prime numbers.txt','r')
r2=file2.readlines()
file3=open('/Users/sibikarthik/Desktop/python projects/computer project files/collatz sequence.txt','r')
r3=file3.readlines()
file4=open('/Users/sibikarthik/Desktop/python projects/computer project files/pascal triangle numbers.txt','r')     
r4=file4.readlines()
file5=open('/Users/sibikarthik/Desktop/python projects/computer project files/pentagonal numbers.txt','r')           
r5=file5.readlines()
file6=open('/Users/sibikarthik/Desktop/python projects/computer project files/fermat numbers.txt','r')               
r6=file6.readlines()

for i in range (1,n+1):
        context=ssl.create_default_context()
        receiver_email=input('Please enter email address to send the shell window transcript to: ')
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print('Sending mail to address',i)
                server.login(sender_email, password)
                for j in r1:
                    message=j.strip()
                    server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 1 sent.')
                file1.close()
                for j in r2:
                    message=j.strip()
                    server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 2 sent.')
                file2.close()
                for j in r3:
                        message=j.strip()
                        server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 3 sent.')
                file3.close()
                for j in r4:
                        message=j.strip()
                        server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 4 sent.')
                file4.close()
                for j in r5:
                        message=j.strip()
                        server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 5 sent.')
                file5.close()
                for j in r6:
                        message=j.strip()
                        server.sendmail(sender_email, receiver_email, message)
                print('Mail for sequence 6 sent.\n')
                file6.close()
                server.quit()
print('> Mail to the inputed', n, 'addresses sent.\n')

# 2. send_direct()
port=465
smtp_server="smtp.gmail.com"
sender_email=""
password=""

for i in range(1,n+1):
        context=ssl.create_default_context()
        receiver_email=input('Please enter email address to send the shell window transcript to: ')
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print('Sending files to address', i)
                server.login(sender_email, password)

                message1=open('/Users/sibikarthik/Desktop/python projects/computer project files/fibonaccinumbers.txt','r')
                message1=message1.read()
                server.sendmail(sender_email, receiver_email, message1)
                print('SEQUENCE 1 sent.')

                message2=open('/Users/sibikarthik/Desktop/python projects/computer project files/prime numbers.txt','r')
                message2=message2.read()
                server.sendmail(sender_email, receiver_email, message2)
                print('SEQUENCE 2 sent.')

                message3==open('/Users/sibikarthik/Desktop/python projects/computer project files/collatz sequence.txt','r')
                message3=message3.read()
                server.sendmail(sender_email, receiver_email, message3)
                print('SEQUENCE 3 sent.')

                message4=open('/Users/sibikarthik/Desktop/python projects/computer project files/pascal triangle numbers.txt','r')     
                message4=message4.read()
                server.sendmail(sender_email, receiver_email, message4)
                print('SEQUENCE 4 sent.')

                message5=open('/Users/sibikarthik/Desktop/python projects/computer project files/pentagonal numbers.txt','r')           
                message5=message5.read()
                server.sendmail(sender_email, receiver_email, message5)
                print('SEQUENCE 5 sent.')

                message6=open('/Users/sibikarthik/Desktop/python projects/computer project files/fermat numbers.txt','r')               
                message6=message6.read()
                server.sendmail(sender_email, receiver_email, message6)
                print('SEQUENCE 6 sent.\n')
                print('Mails sent for address', i)
                server.quit()
print('\nAll mails sent.')

# 3. send_multilinestring()
port=465
smtp_server="smtp.gmail.com"
sender_email=""
password=""

for i in range(1,n+1):
        context=ssl.create_default_context()
        receiver_email=input('Please enter email address to send the shell window transcript to: ')
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print('Sending files to address', i)
                server.login(sender_email, password)

                m1=''''''
                message1=open('/Users/sibikarthik/Desktop/python projects/computer project files/fibonaccinumbers.txt','r')
                message1=message1.read()
                m1=m1+message1
                server.sendmail(sender_email, receiver_email, m1)
                print('SEQUENCE 1 sent.')

                m2=''''''
                message2=open('/Users/sibikarthik/Desktop/python projects/computer project files/prime numbers.txt','r')
                message2=message2.read()
                m2=m2+message2
                server.sendmail(sender_email, receiver_email, m2)
                print('SEQUENCE 2 sent.')

                m3=''''''
                message3=open('/Users/sibikarthik/Desktop/python projects/computer project files/collatz sequence.txt','r')
                message3=message3.read()
                m3=m3+message3
                server.sendmail(sender_email, receiver_email, m3)
                print('SEQUENCE 3 sent.')

                m4=''''''
                message4=open('/Users/sibikarthik/Desktop/python projects/computer project files/pascal triangle numbers.txt','r')     
                message4=message4.read()
                m4=m4+message4
                server.sendmail(sender_email, receiver_email, m4)
                print('SEQUENCE 4 sent.')

                m5=''''''
                message5=open('/Users/sibikarthik/Desktop/python projects/computer project files/pentagonal numbers.txt','r')           
                message5=message5.read()
                m5=m5+message5
                server.sendmail(sender_email, receiver_email, m5)
                print('SEQUENCE 5 sent.')

                m6=''''''
                message6=open('/Users/sibikarthik/Desktop/python projects/computer project files/fermat numbers.txt','r')               
                message6=message6.read()
                m6=m6+message6
                server.sendmail(sender_email, receiver_email, m6)
                print('SEQUENCE 6 sent.\n')
                print('Mails sent for address', i)
                server.quit()
print('\nAll mails sent.')
