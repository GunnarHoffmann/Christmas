import streamlit as st
import matplotlib.pyplot as plt

# --- Seitenlayout & Theme (muss ganz am Anfang stehen!) ---
st.set_page_config(
    page_title="BMI Rechner",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="auto",
    theme={"base": "light"}
)

# --- CSS-Stil: Weißer Hintergrund + moderne Buttons ---
st.markdown("""
    <style>
    html, body, .main {
        background-color: white !important;
        color: black !important;
    }
    h1 {
        font-size: 1.8em;
        color: #3e64ff;
        text-align: center;
    }
    .stButton>button {
        background-color: #3e64ff;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1e40ff;
    }
    </style>
""", unsafe_allow_html=True)
