import streamlit as st
import joblib

# Load model
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="AI Spam Detector", page_icon="🤖")

st.title("🤖 AI Spam Message Detection System")

st.write("Enter a message and AI will detect if it is Spam or Not.")

msg = st.text_area("Enter Message")

if st.button("Check Message"):
    msg_vec = vectorizer.transform([msg])
    result = model.predict(msg_vec)

    if result[0] == 1:
        st.error("Spam Message 🚨")
    else:
        st.success("Not Spam Message ✅")