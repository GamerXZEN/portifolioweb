import streamlit as sl
from send_email import send_email as se

sl.header("Contact Me")

with sl.form(key="email_form", clear_on_submit=True):
	email = sl.text_input("Your email address", placeholder="Enter email address. Ex: youwho@gnpmail.com")
	feedback = sl.text_area("Your message", placeholder="Enter your feedback")
	feedback = f"""\
Subject: New email from Portfolio Website
{feedback}
From {email}"""
	button = sl.form_submit_button("Submit")
	if button:
		sl.info("Success: email sent")
		se(message=feedback)
