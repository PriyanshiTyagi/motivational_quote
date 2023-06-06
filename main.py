import datetime as dt
import os
import random
import smtplib

import dotenv

dotenv.load_dotenv()

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as file:
    data = file.readlines()
message = random.choice(data)

my_email = os.getenv("GMAIL")
password = os.getenv("GMAIL_PASS")

print(day_of_week)

if day_of_week==2:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="lavendar.lavy@yahoo.com",
            msg=f"Subject:Today's Motivation\n\n {message}"

        )
