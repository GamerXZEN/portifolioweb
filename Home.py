import streamlit as sl
import pandas as pd

sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)

with col1:
	sl.image("images/image.png")

with col2:
	sl.subheader("Goutham Pedinedi")
	content = """
Hello there, fellow citizens. I am Goutham Pedinedi, a programmer with a year of experience 
in programming languages such as C++, Python, and Ruby. I live in the United States of America,
although I come from India. I haven't worked at any companies yet, but I hope to do so to gain
experience and set up my own business or work in Google or Microsoft (definitely not Apple because
I hate it).
	"""

	sl.info(content)

sl.write("Below you can find some of the apps I have built in Python:")

col3, space_col, col4 = sl.columns([1, 0.3, 1])

data = pd.read_csv("data.csv", sep=";")

with col3:
	for index, row in data[:11].iterrows():
		sl.header(row["title"])
		sl.write(row["description"])
		sl.image("images/" + row["image"])
		sl.write(f"[Source Code]({row['url']})")

with col4:
	for index, row in data[11:].iterrows():
		sl.header(row["title"])
		sl.write(row["description"])
		sl.image("images/" + row["image"])
		sl.write(f"[Source Code]({row['url']})")
