import smtplib as smt
import ssl
import os


def send_email(message):
	host = "smtp.gmail.com"
	port = 465

	username = "codspecialops@gmail.com"
	password = os.getenv("PASSWORD")

	receiver = "codspecialops@gmail.com"

	context = ssl.create_default_context()

	with smt.SMTP_SSL(host, port, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, message)
