import streamlit as st

st.title("📞 Contact Us")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send Message"):
    st.success("Your message has been sent successfully!")