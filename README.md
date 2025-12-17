# Monday Motivation Email

Small Python script that sends a random motivational quote by email on Mondays.

## Main features

- Checks the current weekday with `datetime` and only sends on Monday.
- Reads a list of motivational quotes from `quotes.txt`.
- Chooses one quote at random using `random.choice`.
- Uses `smtplib` to send the quote via SMTP.
- Email address, app password, recipient and SMTP server are easy to change at the top of `main.py`.

## What I learned

- Sending emails with Python’s built-in `smtplib`.
- Working with dates and times using `datetime`.
- Reading and processing text files.
- Using randomness to pick an item from a list.
- Keeping configuration values separate from the main logic so the script can be reused or scheduled.

## How to run

1. Make sure you have Python 3 installed.
2. Open `motivation-python/main.py` and replace the email settings with your own.
3. From the project folder, run `python motivation-python/main.py`.
4. If today is Monday, the script will send one random quote from `quotes.txt` to the target email; on other days it will exit without sending.
