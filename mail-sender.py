
import smtplib
sender_mail=(input('enter the recitent mail address: '))
msg=
sever = smtplib.SMTP('smtp.gmail.com',587)
sever.starttls()
sever.login('sabari8788@gmail.com','5262@sabari')
sever.sendmail('sabari8788@gmail.com ',sender_mail, msg)