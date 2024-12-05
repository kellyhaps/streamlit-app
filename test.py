import streamlit as st
import json
import requests
#import os

# Title and description
st.title("Simple Streamlit App 1.4")
st.write("Test for request module.")
#API_KEY = os.environ["API_KEY"]
API_KEY = st.secrets["API_KEY"]
API_KEY2 = st.secrets["Number2"]

#request test
url = "https://api.bundeling.com/V2/users??page_size=5&page=1"
headers = {"Content-Type": "application/json", "Api-Key": "6f604e7f2422421c9acf6acbd45e4c91"}
results = requests.get(url, headers=headers)
data = results.json()
print(data)
temp_list = data['data']
st.write(temp_list)

#print(API_KEY2)

# User input
apiKey = st.text_input("ApiKey:")
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# Button click
if st.button("Submit"):
	name = name[:10]
	age = int(age)+10
	if name and age:
		st.success(f"Hello, {name}! and {API_KEY2} You are {age} years old. Your apikey; {API_KEY}")
	else:
		st.warning("Please fill in all the fields.")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar section.")

test = ["hoi1","hoi2","hoi3"]

color = st.sidebar.selectbox("Choose your favorite color:", test)
st.sidebar.write(f"You selected {color}.")
