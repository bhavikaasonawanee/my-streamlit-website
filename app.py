import streamlit as st

st.set_page_config(
    page_title="My Professional Website",
    page_icon="👑",
    layout="wide"
)

st.title("👑 Welcome to My Streamlit Website")

st.header("Home Page")

st.write("""
This is my **professional website built with Streamlit**.

Use the sidebar to navigate:
""")

st.write("✔ About")
st.write("✔ Services")
st.write("✔ Portfolio")
st.write("✔ Blog")
st.write("✔ Contact")

st.success("Website is running successfully 🚀")