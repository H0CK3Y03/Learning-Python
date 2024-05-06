import smtplib   # simple mail transfer protocol library

sender = "adamvesely2003@gmail.com"
receiver = "adamvesely67@gmail.com"
password = "mgeauuiqxxxmmvby"  # in security tab search app passwords and generate a new one, then place here, you need to have 2FA
subject = "Python email test"
body = "I wrote an email! :D"

# header
message = f"""From: Snoop Dogg{sender}
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)   # 587 -> Default mail submission port
server.starttls()     # start transport layer security

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,receiver,message)
    print("Email ha been sent")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")

















