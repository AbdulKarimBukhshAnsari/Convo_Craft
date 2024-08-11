import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as st_auth

#user authentication
names = ["Karim","Abyaz"]
user_names = ["karim","abyaz"]



file_path = Path(__file__).parent /"hashed_password.pkl" 

with file_path.open("rb") as file:
    passwords = pickle.load(file)



authenticator = st_auth.Authenticate(names,user_names,passwords,"convo_craft","abc123",cookie_expiry_days=30)

name, authentication_status ,username = authenticator.login("Login","main")

if authentication_status == False:
    st.error("Enter Correct password or user name")

elif authentication_status == None:
    st.warning("Kindly write username and password")

else:
    st.write("Log in successfully...")