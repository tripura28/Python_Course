#Email Automation

import random
import math
import smtplib #simple mail transfer protocol library
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+" is your otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("sundaritripura44@gmail.com","izar sdrv uchr sneo")
user="sundaritripura44@gmail.com"
email=input("enter the mail which you want to send your otp")
s.sendmail(user,email,msg)

while True:
    a=input("enter the otp")
    if a==OTP:
        print("OTP is correct")
    else:
        print("wrong OTP")
