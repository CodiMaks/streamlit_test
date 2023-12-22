import streamlit as st
import sqlite3


conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS names (username text)
""")

# cursor.execute("DELETE FROM names")

st.title("My Streamlit Web App")
st.write("Welcome to my first Streamlit web app!")


try:
    cursor.execute("SELECT username FROM names")
    username = cursor.fetchall()[0][0]
    st.write(f"Welcome back {username}")
except Exception as e:
    print(e)


name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")

if st.button("Save"):
    cursor.execute("SELECT username FROM names")
    if cursor.fetchall():
        cursor.execute("UPDATE names SET username = ?", (name, ))
    else:
        cursor.execute("INSERT INTO names VALUES (?)", (name, ))


conn.commit()
conn.close()
