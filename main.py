"""Simple Email message sender made with python"""
import smtplib
from email.message import EmailMessage

emailUser = input('Enter your email\n')

""" If you are using Google mail service you will need 2 step factor authethication 
And you need to generate an app password""" 

emailPassword = input("Enter your Password\n")
rec =[]
reciever = input('Email list of email without comma\n').split()
reciever.append

emailPassword = "User Password"
"""Enter reciever Email"""
reciever =[]

msg = EmailMessage()
msg.set_content('Enter body of Your message')

msg["Subject"] ="Subject of your mail"
msg['From'] = emailUser
msg['To'] = reciever


try:
    # send message via our own smtp server
  
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login(emailUser, emailPassword)
  server.send_message(msg)
  server.quit()
  print('Mail sent')
except:
    print('something went wrong')

if__name__ ='__main__'