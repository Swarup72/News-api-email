import smtplib
import os
import ssl
from email.message import EmailMessage
import certifi

PASSWORD = os.getenv("EMAIL_NEWS_PASSWORD")
SENDER = "swarup111505@gmail.com"
RECEIVER = "swarup111505@gmail.com"

# def send_email(message):
#     email_message = EmailMessage()
#     email_message["Subject"] = "Today's Headlines.."
#     email_message["From"] = SENDER
#     email_message["To"] = RECEIVER
#     email_message.set_content(message)
#
#     # Choose either 587 or 465
#     USE_PORT_587 = False
#
#     if USE_PORT_587:
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.ehlo()
#             server.starttls()
#             server.login(SENDER, PASSWORD)
#             server.sendmail(SENDER, RECEIVER, email_message.as_string())
#     else:
#         context = ssl.create_default_context(cafile=certifi.where())
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#             server.login(SENDER, PASSWORD)
#             server.sendmail(SENDER, RECEIVER, email_message.as_string())
def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    email_message = EmailMessage()
    email_message["Subject"] = "Today's Headlines.."
    email_message["From"] = SENDER
    email_message["To"] = RECEIVER
    email_message.set_content(message)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(SENDER, PASSWORD)
        server.send_message(email_message)