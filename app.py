import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Santa Claus App", layout="centered")

# Title and description
st.title("🎅 Santa Claus Viewer")
st.write("Welcome to the Santa Claus app! Enjoy the festive season with a picture of Santa.")

# Display the image from the URL
santa_image_url = "https://media.istockphoto.com/id/1757869500/de/foto/biker-weihnachtsmann-liefert-weihnachtsgeschenke-aus.jpg?s=612x612&w=0&k=20&c=4kZS-WFn56Ct2LqQEaaWveYBW2y1zi_OBiUrMQ4Phs8="
st.image(santa_image_url, caption="Santa Claus", use_column_width=True)

# Footer
st.write("Happy Holidays! 🎄")
