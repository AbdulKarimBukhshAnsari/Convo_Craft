import pickle   # to Serializing the object to a file to convert into byte vales
from pathlib import Path # to remove the differnce of path of differnt operating system 
import streamlit_authenticator as st_auth

names = ["Karim","Abyaz"]
user_names = ["karim","abyaz"]
passwords = ["abc123","abc456"]

#to generate the hashed Passwords
hashed_passwords = st_auth.Hasher(passwords).generate()

#locate the current location 
file_path = Path(__file__).parent / "hashed_password.pkl"

#Saved the hash password in the form of binary 
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)


