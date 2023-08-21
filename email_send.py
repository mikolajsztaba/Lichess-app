import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "lichessapp123@gmail.com"
receiver_email = os.environ.get("RECEIVER_EMAIL")
print(receiver_email)
print(os.environ.get("LICHESS_PASSWORD"))
subject = "Subject of your email"
message = "Body of your email."

# Create a MIME object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to Gmail's SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Use 465 for SSL or 587 for TLS

# Establish a secure session with the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Encrypt the connection
    server.login(sender_email, os.environ.get("LICHESS_PASSWORD"))  # Replace with your Gmail password

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email sent successfully.")