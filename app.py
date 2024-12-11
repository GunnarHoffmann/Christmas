import streamlit as st
from PIL import Image

# Set the page title and layout
st.set_page_config(page_title="Santa Claus App", layout="centered")

# Title and description
st.title("🎅 Santa Claus Viewer")
st.write("Welcome to the Santa Claus app! Enjoy the festive season with a picture of Santa.")

# Load and display the image
try:
    # Load the Santa image
    santa_image = Image.open("santa_claus.jpg")

    # Display the image
    st.image(santa_image, caption="Santa Claus", use_column_width=True)
except FileNotFoundError:
    st.error("Santa Claus image not found. Please make sure 'santa_claus.jpg' is in the same directory as this app.")

# Footer
st.write("Happy Holidays! 🎄")
