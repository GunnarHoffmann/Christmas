import streamlit as st
from PIL import Image
from datetime import datetime

# Set the page title and icon
st.set_page_config(page_title="Santa Claus Welcome", page_icon="🎅", layout="centered")

# Display a festive image
def load_santa_image():
    return Image.open("santa_claus.jpg")  # Ensure you have a suitable image in the same directory

# Main content
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        color: #ff0000;
        text-align: center;
    }
    .content {
        font-size: 20px;
        color: #333333;
        text-align: center;
    }
    .days-remaining {
        font-size: 24px;
        color: #007bff;
        text-align: center;
        margin: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🎅 Welcome to Santa Claus\' Greeting App! 🎅</div>', unsafe_allow_html=True)

santa_image = None
try:
    santa_image = load_santa_image()
    st.image(santa_image, caption="Santa Claus is here to spread joy!", use_column_width=True)
except FileNotFoundError:
    st.warning("Santa's picture is missing! Please ensure the 'santa_claus.jpg' file is in the app directory.")

st.markdown('<div class="content">Hello and welcome! Santa Claus is delighted to greet you this festive season. 🎄✨</div>', unsafe_allow_html=True)

# Calculate days until 24th December
today = datetime.now()
target_date = datetime(today.year, 12, 24)
days_remaining = (target_date - today).days

if days_remaining >= 0:
    st.markdown(f'<div class="days-remaining">There are **{days_remaining} days** remaining until 24th December! 🎁</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="days-remaining">It\'s already past 24th December! Hope you had a great holiday! 🎅</div>', unsafe_allow_html=True)

st.markdown('<div class="content">Feel free to explore the app and enjoy the holiday cheer!</div>', unsafe_allow_html=True)

# Add an interactive element
st.markdown('<div style="text-align: center; margin-top: 20px;">', unsafe_allow_html=True)
if st.button("Say Hi to Santa 🎅"):
    st.markdown('<div class="content">Santa says Hi back! 🎅✨</div>', unsafe_al
