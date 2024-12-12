import streamlit as st
from datetime import datetime
from gtts import gTTS
import os

# Set the page title and icon
st.set_page_config(page_title="Willkommen beim Weihnachtsmann", page_icon="🎅", layout="centered")

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

st.markdown('<div class="title">🎅 Willkommen in der Gruß-App vom Weihnachtsmann! 🎅</div>', unsafe_allow_html=True)

# Add a slider for image scaling
scaling_factor = st.slider("Skaliere das Bild des Weihnachtsmanns:", min_value=0.1, max_value=1.0, value=0.5, step=0.1)

santa_image_url = "https://i.pinimg.com/736x/3a/d4/ae/3ad4aebc7cb02fe7ae7fac12dbd41c13.jpg"
st.image(santa_image_url, caption="Der Weihnachtsmann verbreitet Freude!", use_container_width=False, width=int(736 * scaling_factor))

st.markdown('<div class="content">Hallo und willkommen! Der Weihnachtsmann freut sich, dich in dieser festlichen Zeit zu begrüßen. 🎄✨</div>', unsafe_allow_html=True)

# Calculate days until 24th December
today = datetime.now()
target_date = datetime(today.year, 12, 24)
days_remaining = (target_date - today).days

if days_remaining >= 0:
    st.markdown(f'<div class="days-remaining">Es sind noch <strong>{days_remaining} Tage</strong> bis Heiligabend! 🎁</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="days-remaining">Heiligabend ist bereits vorbei! Ich hoffe, du hattest eine wunderbare Zeit! 🎅</div>', unsafe_allow_html=True)

# Text-to-Speech for Santa's message in German
def play_santa_message():
    if days_remaining >= 0:
        message = f"Ho ho ho! Es sind noch {days_remaining} Tage bis Heiligabend!"
    else:
        message = "Ho ho ho! Heiligabend ist schon vorbei! Ich hoffe, du hattest eine wundervolle Zeit!"

    tts = gTTS(text=message, lang='de')
    audio_file = "santa_message.mp3"
    tts.save(audio_file)
    return audio_file

if st.button("Höre den Weihnachtsmann 🎅"):
    audio_file = play_santa_message()
    with open(audio_file, "rb") as file:
        st.audio(file.read(), format="audio/mp3")
    os.remove(audio_file)

st.markdown('<div class="content">Erkunde die App und genieße die festliche Stimmung!</div>', unsafe_allow_html=True)

# Add an interactive element
st.markdown('<div style="text-align: center; margin-top: 20px;">', unsafe_allow_html=True)
if st.button("Sag dem Weihnachtsmann Hallo 🎅"):
    st.markdown('<div class="content">Der Weihnachtsmann sagt Hallo zurück! 🎅✨</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
