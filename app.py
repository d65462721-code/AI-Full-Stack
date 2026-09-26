import streamlit as st

st.title("🤖 My AI ChatBot")
st.write("Welcome to my chatbot!")

question = st.text_input("You:")

if st.button("Generate"):
    if question:
        if question.lower() == "hello":
            response = "Hello! 👋 How can I help you?"
        elif question.lower() == "how are you":
            response = "I'm fine! 😊"
        elif question.lower() == "bye":
            response = "Goodbye! 👋"
        else:
            response = "You asked: " + question

        st.write("Bot:", response)
    else:
        st.warning("Please enter a prompt.")
