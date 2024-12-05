import streamlit as st
import json

# Title and description
st.title("Simple Streamlit App 1.3")
st.write("This is a simple app demonstrating basic Streamlit features.")

# User input
apiKey = st.text_input("ApiKey:")
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# Button click
if st.button("Submit"):
	name = name[:10]
	age = int(age)+10
	if name and age:
		st.success(f"Hello, {name}! You are {age} years old.")
	else:
		st.warning("Please fill in all the fields.")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar section.")

# Selectbox example
with open ('test.json') as f:
	test = json.load(f)

#test = ["hoi1","hoi2","hoi3"]

color = st.sidebar.selectbox("Choose your favorite color:", test)
st.sidebar.write(f"You selected {color}.")
