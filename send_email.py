from email.mime.text import MIMEText
import smtplib

from_email = "yardenkrok@gmail.com"
from_password = "Test12312#"
port = 587
host_address = "smtp.gmail.com"

def send_email(email, height, avg, count):
	subject = "Height Data"
	message = "Hey there, your height is <strong>{}</strong>. The average height of <strong>{}</strong> people is <strong>{}</strong> ".format(height, count, avg)

	msg = MIMEText(message, 'html')
	msg['Subject'] = subject
	msg['To'] = email
	msg['From'] = from_email

	smtp_email = smtplib.SMTP(host_address, port)
	# smtp_email.set_debuglevel(1)
	smtp_email.ehlo()
	smtp_email.starttls()
	# smtp_email.ehlo()
	smtp_email.login(from_email, from_password)
	smtp_email.send_message(msg)