import pandas as pd
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
EMAIL = "handikasyam.dev@gmail.com"
PASSWORD = ""
data = pd.read_csv("./birthdays.csv")
date_now = dt.datetime()
today = date_now.day
month = date_now.month
today_birthdays = data[(data["day"] == today) & (data["month"] == month)]

if not today_birthdays.empty:
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter:
        letter_content = letter.read()

    for i in today_birthdays.index:
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=today_birthdays.at[i, "email"],
                msg=f"Subject:Happy Birthday {today_birthdays.at[i, 'name']}\n\n{letter_content.replace(PLACEHOLDER, today_birthdays.at[i, 'name'])}",
            )
