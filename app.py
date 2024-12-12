import streamlit as st
from datetime import datetime

# Set the page title and icon
st.set_page_config(page_title="Santa Claus Welcome", page_icon="🎅", layout="centered")

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

# Add a slider for image scaling
scaling_factor = st.slider("Scale Santa's image:", min_value=0.1, max_value=1.0, value=0.5, step=0.1)

santa_image_url = "https://i.pinimg.com/736x/3a/d4/ae/3ad4aebc7cb02fe7ae7fac12dbd41c13.jpg"
st.image(santa_image_url, caption="Santa Claus is here to spread joy!", use_column_width=False, width=int(736 * scaling_factor))

st.markdown('<div class="content">Hello and welcome! Santa Claus is delighted to greet you this festive season. 🎄✨</div>', unsafe_allow_html=True)

# Calculate days until 24th December
today = datetime.now()
target_date = datetime(today.year, 12, 24)
days_remaining = (target_date - today).days

if days_remaining >= 0:
    st.markdown(f'<div class="days-remaining">There are <strong>{days_remaining} days</strong> remaining until 24th December! 🎁</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="days-remaining">It\'s already past 24th December! Hope you had a great holiday! 🎅</div>', unsafe_allow_html=True)

st.markdown('<div class="content">Feel free to explore the app and enjoy the holiday cheer!</div>', unsafe_allow_html=True)

# Add an interactive element
st.markdown('<div style="text-align: center; margin-top: 20px;">', unsafe_allow_html=True)
if st.button("Say Hi to Santa 🎅"):
    st.markdown('<div class="content">Santa says Hi back! 🎅✨</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
