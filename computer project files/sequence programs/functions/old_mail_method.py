n=int(input('Enter no. of mails to be sent to the same, or different addresses: '))
        message=input('Please copy the text in the shell window above, paste it here and enter: ')
        port=465
        smtp_server="smtp.gmail.com"
        sender_email=""
        password="" # "upge gpcx oqxe vvpm"
        #context=ssl.create_default_context()
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
