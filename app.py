import streamlit as st
from PIL import Image

# Set the page title and icon
st.set_page_config(page_title="Santa Claus Welcome", page_icon="🎅")

# Display a festive image
def load_santa_image():
    return Image.open("santa_claus.jpg")  # Ensure you have a suitable image in the same directory

# Main content
st.title("🎅 Welcome to Santa Claus' Greeting App! 🎅")

santa_image = None
try:
    santa_image = load_santa_image()
    st.image(santa_image, caption="Santa Claus is here to spread joy!", use_column_width=True)
except FileNotFoundError:
    st.warning("Santa's picture is missing! Please ensure the 'santa_claus.jpg' file is in the app directory.")

st.write("Hello and welcome! Santa Claus is delighted to greet you this festive season. 🎄✨")

st.write("\nFeel free to explore the app and enjoy the holiday cheer!")

# Add an interactive element
st.button("Say Hi to Santa 🎅")

