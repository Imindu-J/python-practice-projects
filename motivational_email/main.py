# uijalt02@gmail.com: pass=Bla**swor****n*2, app pass=obhs uove cfyp wdbs
# uijalt@yahoo.com: pass=Bla**swor****n*2, app pass=

import smtplib
import datetime as dt
import random

my_email = 'uijalt02@gmail.com'
password = 'obhs uove cfyp wdbs'

now = dt.datetime.now()
day = now.weekday()
if day == 6:
    with open('quotes.txt', 'r') as text:
        q_list = text.readlines()
        quote = random.choice(q_list)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='uijalt@yahoo.com',
            msg=f'Subject:Git up btch\n\n{quote}'
        )
