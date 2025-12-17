import smtplib
import datetime as dt
import random

# --- CONFIG: fill these with your own details when you run locally ---
MY_EMAIL = "your_email@example.com"          # e.g. your Gmail address
MY_APP_PASSWORD = "your_app_password_here"   # app password, not real login
TO_EMAIL = "recipient@example.com"           # where the quote will be sent
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
# ---------------------------------------------------------------------

now = dt.datetime.now()
day = now.weekday()  # 0 = Monday, ..., 6 = Sunday

if day == 0:  # send on Monday
    with open("quotes.txt") as motivation_text:
        all_quotes = motivation_text.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )
