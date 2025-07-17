# import smtplib

# email = "handikasyam.dev@gmail.com"
# password = ""

# with smtplib.SMTP(host="smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs="handika00026@gmail.com",
#         msg="Subject:Hello from Python\n\nPesan ini untuk Handika yaitu diri saya sendiri hehe, saya harap kamu tidak menyerah dan terus semangat mengejar cita-cita dan membahagiakan kedua orang tua dan kakak saya.",
#     )

#######
# connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=2004, month=9, day=26, hour=7)

# print(date_of_birth)

import random
import datetime as dt
import smtplib

weekday = dt.datetime.now().weekday()
EMAIL = "handikasyam.dev@gmail.com"
PASSWORD = ""

if weekday == 0:
    with open("./quotes.txt") as file:
        quote = random.choice(file.readlines())

    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="handika00026@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}",
        )
