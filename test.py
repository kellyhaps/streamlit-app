import streamlit as st

# Title and description
st.title("Simple Streamlit App om te testen")
st.write("Is het ook live nadat we het private hebben gezet??")

# User input
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
color = st.sidebar.selectbox("Choose your favorite color:", ["Red", "Blue", "Green","yellow"])
st.sidebar.write(f"You selected {color}.")
