import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from gtts import gTTS
import os

# Set the page title and layout
st.set_page_config(page_title="Santa Claus App", layout="centered")

# Custom CSS for beautifying the app
st.markdown(
    """
    <style>
    body {
        background-color: #f7f9fc;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #f7f9fc;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .title-text {
        text-align: center;
        color: #ff6f61;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    .description-text {
        text-align: center;
        color: #444;
        font-size: 1.2em;
    }
    .countdown-text {
        text-align: center;
        color: #ff6f61;
        font-size: 1.5em;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .footer-text {
        text-align: center;
        color: #888;
        margin-top: 40px;
        font-size: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown('<div class="title-text">🎅 Santa Claus Viewer</div>', unsafe_allow_html=True)
st.markdown('<div class="description-text">Welcome to the Santa Claus app! Enjoy the festive season with a picture of Santa.</div>', unsafe_allow_html=True)

# Display the image from the URL
santa_image_url = "https://media.istockphoto.com/id/1757869500/de/foto/biker-weihnachtsmann-liefert-weihnachtsgeschenke-aus.jpg?s=612x612&w=0&k=20&c=4kZS-WFn56Ct2LqQEaaWveYBW2y1zi_OBiUrMQ4Phs8="
st.image(santa_image_url, caption="Santa Claus", use_container_width=True)

# Countdown to 24th December
today = datetime.now()
christmas_eve = datetime(today.year, 12, 24)
days_left = (christmas_eve - today).days
if days_left >= 0:
    countdown_message = f"Only {days_left} days left until Christmas Eve! 🎄"
else:
    countdown_message = "Christmas Eve has already passed. Happy Holidays! 🎅"
st.markdown(f'<div class="countdown-text">{countdown_message}</div>', unsafe_allow_html=True)

# Text-to-speech
if days_left >= 0:
    tts = gTTS(text=f"Hello! There are only {days_left} days left until Christmas Eve!", lang='en')
else:
    tts = gTTS(text="Hello! Christmas Eve has already passed. Happy Holidays!", lang='en')
tts.save("santa_message.mp3")
st.audio("santa_message.mp3")

# Footer
st.markdown('<div class="footer-text">Happy Holidays! 🎄</div>', unsafe_allow_html=True)
