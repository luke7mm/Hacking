#Simple python smtp server from https://realpython.com/python-send-email/

import smtplib, ssl

port = 1025
password = input("Enter password: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
  server.login("myself@gmail.com", password)

server.sendmail(sender_email, reciever_email, message)

sender_email = "myself@gmail.com"
reciever_email = "yourself@gmail.com"
message = """\
Subject: Hello sir

We come from outer space."""