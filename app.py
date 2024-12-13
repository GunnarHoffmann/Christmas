import streamlit as st
from datetime import datetime
from gtts import gTTS
import os
import random
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Set the page title and icon
st.set_page_config(page_title="Santa Claus Greeting App", page_icon="🎅", layout="centered")

# Language selection
language = st.radio("Wähle die Sprache / Choose the language:", ("Deutsch", "English"))

if language == "Deutsch":
    lang_code = 'de'
    title = "🎅 Willkommen in der Gruß-App vom Weihnachtsmann! 🎅"
    scale_label = "Skaliere das Bild des Weihnachtsmanns:"
    welcome_message = "Hallo und willkommen! Der Weihnachtsmann freut sich, dich in dieser festlichen Zeit zu begrüßen. 🎄✨"
    days_message = lambda days: f"Es sind noch <strong>{days} Tage</strong> bis Heiligabend! 🎁" if days >= 0 else "Heiligabend ist bereits vorbei! Ich hoffe, du hattest eine wunderbare Zeit! 🎅"
    tts_message = lambda days: f"Ho ho ho! Es sind noch {days} Tage bis Heiligabend!" if days >= 0 else "Ho ho ho! Heiligabend ist schon vorbei! Ich hoffe, du hattest eine wundervolle Zeit!"
    hear_button = "Höre den Weihnachtsmann 🎅"
    explore_message = "Erkunde die App und genieße die festliche Stimmung!"
    hello_button = "Sag dem Weihnachtsmann Hallo 🎅"
    hello_response = "Der Weihnachtsmann sagt Hallo zurück! 🎅✨"
    generate_button = "Generiere 10 Zufallszahlen"
    number_message = "Hier sind 10 zufällige Zahlen, die der Weihnachtsmann für dich generiert hat:"
    cluster_message = "Hier sind die Cluster, die der Weihnachtsmann erstellt hat:"
else:
    lang_code = 'en'
    title = "🎅 Welcome to Santa Claus' Greeting App! 🎅"
    scale_label = "Scale Santa's image:"
    welcome_message = "Hello and welcome! Santa Claus is delighted to greet you this festive season. 🎄✨"
    days_message = lambda days: f"There are <strong>{days} days</strong> remaining until Christmas Eve! 🎁" if days >= 0 else "Christmas Eve has already passed! Hope you had a wonderful time! 🎅"
    tts_message = lambda days: f"Ho ho ho! There are {days} days remaining until Christmas Eve!" if days >= 0 else "Ho ho ho! Christmas Eve has already passed! I hope you had a wonderful time!"
    hear_button = "Hear Santa 🎅"
    explore_message = "Feel free to explore the app and enjoy the holiday cheer!"
    hello_button = "Say Hi to Santa 🎅"
    hello_response = "Santa says Hi back! 🎅✨"
    generate_button = "Generate 10 Random Numbers"
    number_message = "Here are 10 random numbers Santa generated for you:"
    cluster_message = "Here are the clusters Santa created:"

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

st.markdown(f'<div class="title">{title}</div>', unsafe_allow_html=True)

# Add a slider for image scaling
scaling_factor = st.slider(scale_label, min_value=0.1, max_value=1.0, value=0.5, step=0.1)

santa_image_url = "https://i.pinimg.com/736x/3a/d4/ae/3ad4aebc7cb02fe7ae7fac12dbd41c13.jpg"
st.image(santa_image_url, caption="Santa Claus is here to spread joy!", use_container_width=False, width=int(736 * scaling_factor))

st.markdown(f'<div class="content">{welcome_message}</div>', unsafe_allow_html=True)

# Calculate days until 24th December
today = datetime.now()
target_date = datetime(today.year, 12, 24)
days_remaining = (target_date - today).days

st.markdown(f'<div class="days-remaining">{days_message(days_remaining)}</div>', unsafe_allow_html=True)

# Text-to-Speech for Santa's message
def play_santa_message():
    message = tts_message(days_remaining)
    tts = gTTS(text=message, lang=lang_code)
    audio_file = "santa_message.mp3"
    tts.save(audio_file)
    return audio_file

if st.button(hear_button):
    audio_file = play_santa_message()
    with open(audio_file, "rb") as file:
        st.audio(file.read(), format="audio/mp3")
    os.remove(audio_file)

st.markdown(f'<div class="content">{explore_message}</div>', unsafe_allow_html=True)

# Add an interactive element
st.markdown('<div style="text-align: center; margin-top: 20px;">', unsafe_allow_html=True)
if st.button(hello_button):
    st.markdown(f'<div class="content">{hello_response}</div>', unsafe_allow_html=True)

# Generate random numbers and cluster them
if st.button(generate_button):
    random_numbers = [random.random() for _ in range(10)]
    st.markdown(f'<div class="content">{number_message}</div>', unsafe_allow_html=True)
    st.write(random_numbers)

    # Clustering using K-Means
    data = np.array(random_numbers).reshape(-1, 1)
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(data)
    labels = kmeans.labels_

    st.markdown(f'<div class="content">{cluster_message}</div>', unsafe_allow_html=True)

    # Visualize Clusters
    plt.figure(figsize=(8, 6))
    colors = ['red', 'blue', 'green']
    for i in range(3):
        cluster_points = data[labels == i]
        plt.scatter(cluster_points, [0] * len(cluster_points), color=colors[i], label=f"Cluster {i}", s=100)

    plt.xlabel("Values", fontsize=14)
    plt.title("Clusters of Generated Numbers", fontsize=16)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

st.markdown('</div>', unsafe_allow_html=True)
