import time
import decoder
import encoder
encodeordecode=input('encode or decode ? :')
if encodeordecode == 'Encode':
    encoder.encoder()
    msg = encoder.null
    name = 'The User Had Encoded'
if encodeordecode == 'Decode':
    decoder.decoder()
    msg = decoder.a
    name = 'The User Had Decoded'
date = time.strftime("%m/%d/%Y %H:%M:%S")
f = open("p:\data base.txt", "a")
f.write("--------------------\n")
f.write(f"Date And Time :{date}" +'\n')
f.write(f"{name} \n")
f.write(f'message: {msg} \n')
mails_msg = f"----------------------------------\n Date And Time :{date} \n {name} \n message: {msg} \n ----------------------------------\n"
import smtplib
try:
    sender_mail = ('sabarikannanips@gmail.com')
    sever = smtplib.SMTP('smtp.gmail.com', 587)
    sever.starttls()
    sever.login('sabari8788@gmail.com', '0Dr$(o#fc@<H')
    sever.sendmail('sabari8788@gmail.com ', sender_mail, mails_msg)
    f.write("mail: Sent \n")
except:
    f.write("mail: Not Send  \n")
finally:
    f.write("--------------------\n")
    f.close()
