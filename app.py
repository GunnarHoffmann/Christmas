#test123456789012345
#test123456
#test12345678
# 123

#old123

#local1234567890123
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import yfinance as yf
import os
from dotenv import load_dotenv
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import json
import base64

# Load environment variables
load_dotenv()

# --- Seitenlayout ----
st.set_page_config(
    page_title="Gesundheits & Wellness Center",
    page_icon="🎄",
    layout="centered",

)

# --- Google OAuth Configuration ---
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')  # Will be set in Streamlit Cloud settings

def get_google_auth_url():
    """Generate Google OAuth URL for sign-in"""
    if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        return None

    try:
        # For local development use localhost, for production use the configured REDIRECT_URI
        redirect_uri = REDIRECT_URI if REDIRECT_URI else 'http://localhost:8501'

        client_config = {
            "web": {
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [redirect_uri],
            }
        }

        flow = Flow.from_client_config(
            client_config,
            scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
            redirect_uri=redirect_uri
        )

        auth_url, state = flow.authorization_url(prompt='consent')

        # Store state in session for verification
        st.session_state.oauth_state = state

        return auth_url
    except Exception as e:
        st.error(f"Error generating auth URL: {str(e)}")
        return None

def handle_oauth_callback(authorization_code):
    """Handle OAuth callback and get user info"""
    try:
        redirect_uri = REDIRECT_URI

        client_config = {
            "web": {
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [redirect_uri],
            }
        }

        flow = Flow.from_client_config(
            client_config,
            scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
            redirect_uri=redirect_uri
        )

        # Exchange authorization code for tokens
        flow.fetch_token(code=authorization_code)
        credentials = flow.credentials

        # Get user info
        import requests
        userinfo_response = requests.get(
            'https://www.googleapis.com/oauth2/v1/userinfo',
            headers={'Authorization': f'Bearer {credentials.token}'}
        )

        if userinfo_response.status_code == 200:
            user_info = userinfo_response.json()
            return user_info
        else:
            return None

    except Exception as e:
        st.error(f"Error handling OAuth callback: {str(e)}")
        return None

# --- Session State Initialisierung ---
if 'bmi_history' not in st.session_state:
    st.session_state.bmi_history = []
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
if 'music_playing' not in st.session_state:
    st.session_state.music_playing = False
if 'user_info' not in st.session_state:
    st.session_state.user_info = None
if 'oauth_state' not in st.session_state:
    st.session_state.oauth_state = None

# --- Handle OAuth Callback ---
query_params = st.query_params
if 'code' in query_params and st.session_state.user_info is None:
    auth_code = query_params['code']
    user_info = handle_oauth_callback(auth_code)
    if user_info:
        st.session_state.user_info = user_info
        # Clear query params after successful authentication
        st.query_params.clear()
        st.rerun()

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Dark Mode Toggle ---
dark_mode = st.session_state.dark_mode

# --- CSS-Stil ---
if dark_mode:
    bg_gradient = "linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)"
    text_color = "#eaeaea"
    card_bg = "#0f3460"
    border_color = "#e94560"
else:
    bg_gradient = "linear-gradient(135deg, #0a1929 0%, #1a2332 50%, #2d3e50 100%)"
    text_color = "#ffffff"
    card_bg = "#2d3e50"
    border_color = "#667eea"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, .main {{
        background: {bg_gradient} !important;
        color: {text_color} !important;
        font-family: 'Inter', sans-serif !important;
    }}

    /* Make all headings outside of boxed containers blue */
    h1, h2, h3, h4, h5, h6 {{
        color: #667eea !important; /* blue for titles outside boxes */
        font-weight: 600;
        margin-bottom: 0.5em;
    }}

    h1 {{
        font-size: 2.5em;
        text-align: center;
        font-weight: 700;
    }}

    .stButton>button {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 12px;
        padding: 0.75em 2em;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        width: 100%;
        font-size: 1.1em;
    }}

    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }}

    /* Input Felder */
    .stNumberInput > div > div > input {{
        border-radius: 10px;
        border: 2px solid #e0e7ff;
        padding: 0.75em;
        font-size: 1.1em;
        transition: all 0.3s ease;
    }}

    .stNumberInput > div > div > input:focus {{
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }}

    /* Info Boxen */
    .info-box {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 1.5em;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        margin: 1em 0;
        border-left: 4px solid white;
        color: white;
    }}

    /* Produktkarten */
    .product-card {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 1.5em;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        margin: 1em 0;
        transition: all 0.3s ease;
        min-height: 280px;
        display: flex;
        flex-direction: column;
        color: white;
    }}

    .product-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
    }}

    /* Text in boxed components should remain white */
    .info-box h1, .info-box h2, .info-box h3, .info-box h4, .info-box h5, .info-box h6, .info-box p {{
        color: white !important;
    }}

    .product-card h1, .product-card h2, .product-card h3, .product-card h4, .product-card h5, .product-card h6, .product-card p {{
        color: white !important;
    }}

    /* Links */
    a {{
        color: #667eea;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }}

    a:hover {{
        color: #764ba2;
    }}

    /* Divider */
    hr {{
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2em 0;
    }}

    /* Markdown Text */
    .markdown-text-container {{
        font-size: 1.05em;
        line-height: 1.8;
    }}

    /* Subheader Styling inside general markdown - blue unless inside a box */
    [data-testid="stMarkdownContainer"] h3 {{
        color: #667eea !important;
        font-weight: 600;
        margin-top: 1em;
    }}

    /* Santa Claus Animation */
    @keyframes santaSlide {{
        0% {{
            transform: translateX(-100px) rotate(-5deg);
        }}
        50% {{
            transform: translateX(calc(50vw - 50px)) rotate(5deg);
        }}
        100% {{
            transform: translateX(calc(100vw + 100px)) rotate(-5deg);
        }}
    }}

    .santa-container {{
        position: fixed;
        bottom: 20px;
        left: 0;
        z-index: 9999;
        animation: santaSlide 15s ease-in-out infinite;
        pointer-events: none;
    }}

    .santa {{
        font-size: 4em;
        filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
    }}

    /* Floating Santa near title */
    @keyframes santaFloat {{
        0%, 100% {{
            transform: translateY(0) rotate(-10deg);
        }}
        50% {{
            transform: translateY(-20px) rotate(10deg);
        }}
    }}

    .santa-title {{
        display: inline-block;
        animation: santaFloat 3s ease-in-out infinite;
        font-size: 3em;
        margin: 0 10px;
    }}

    /* Spider Animation */
    @keyframes spiderDangle {{
        0%, 100% {{
            transform: translateY(0) rotate(-5deg);
        }}
        50% {{
            transform: translateY(15px) rotate(5deg);
        }}
    }}

    .spider-container {{
        position: fixed;
        left: 20px;
        top: 100px;
        z-index: 9999;
        pointer-events: none;
    }}

    .spider-web {{
        width: 2px;
        height: 80px;
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.7));
        margin: 0 auto;
    }}

    .spider {{
        font-size: 3em;
        animation: spiderDangle 2s ease-in-out infinite;
        display: block;
        text-align: center;
        filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.5));
    }}

    /* Snowflake Animation */
    @keyframes snowfall {{
        0% {{
            transform: translateY(-10px) translateX(0);
            opacity: 1;
        }}
        100% {{
            transform: translateY(100vh) translateX(100px);
            opacity: 0.3;
        }}
    }}

    .snowflake {{
        position: fixed;
        top: -10px;
        color: white;
        font-size: 1em;
        animation: snowfall linear infinite;
        pointer-events: none;
        z-index: 9999;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.8);
    }}

    /* Spider Animation */
    @keyframes spiderSwing {{
        0%, 100% {{
            transform: rotate(-5deg);
        }}
        50% {{
            transform: rotate(5deg);
        }}
    }}

    .spider-container {{
        position: fixed;
        top: 50px;
        right: 50px;
        z-index: 9999;
        pointer-events: none;
    }}

    .spider-web {{
        width: 2px;
        height: 100px;
        background: linear-gradient(to bottom, rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.3));
        margin: 0 auto;
        box-shadow: 0 0 3px rgba(255, 255, 255, 0.5);
    }}

    .spider {{
        font-size: 3em;
        text-align: center;
        animation: spiderSwing 3s ease-in-out infinite;
        transform-origin: top center;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
    }}

    /* Cat Animation */
    @keyframes catSway {{
        0%, 100% {{
            transform: rotate(-3deg);
        }}
        50% {{
            transform: rotate(3deg);
        }}
    }}

    .cat-container {{
        position: fixed;
        top: 200px;
        right: 30px;
        z-index: 9999;
        pointer-events: none;
    }}

    .cat {{
        font-size: 3em;
        text-align: center;
        animation: catSway 2.5s ease-in-out infinite;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
    }}
    </style>
""", unsafe_allow_html=True)

# --- Titel ---
st.markdown("<h1>🎄 Gesundheits & Wellness Center <span class='santa-title'>🎅</span></h1>", unsafe_allow_html=True)

# --- Animated Santa sliding across the screen ---
st.markdown("""
<div class="santa-container">
    <div class="santa">🎅🛷</div>
</div>
""", unsafe_allow_html=True)

# --- Spider dangling on the left side ---
st.markdown("""
<div class="spider-container">
    <div class="spider-web"></div>
    <div class="spider">🕷️</div>
</div>
""", unsafe_allow_html=True)

# --- Falling Snowflakes ---
st.markdown("""
<div class="snowflake" style="left: 10%; animation-duration: 10s; animation-delay: 0s; font-size: 1.5em;">❄</div>
<div class="snowflake" style="left: 20%; animation-duration: 12s; animation-delay: 2s; font-size: 1.2em;">❄</div>
<div class="snowflake" style="left: 30%; animation-duration: 15s; animation-delay: 1s; font-size: 1.0em;">❄</div>
<div class="snowflake" style="left: 40%; animation-duration: 11s; animation-delay: 3s; font-size: 1.8em;">❄</div>
<div class="snowflake" style="left: 50%; animation-duration: 13s; animation-delay: 0.5s; font-size: 1.4em;">❄</div>
<div class="snowflake" style="left: 60%; animation-duration: 14s; animation-delay: 2.5s; font-size: 1.1em;">❄</div>
<div class="snowflake" style="left: 70%; animation-duration: 16s; animation-delay: 1.5s; font-size: 1.6em;">❄</div>
<div class="snowflake" style="left: 80%; animation-duration: 12s; animation-delay: 3.5s; font-size: 1.3em;">❄</div>
<div class="snowflake" style="left: 90%; animation-duration: 13s; animation-delay: 0.8s; font-size: 1.7em;">❄</div>
<div class="snowflake" style="left: 15%; animation-duration: 11s; animation-delay: 4s; font-size: 1.2em;">❄</div>
<div class="snowflake" style="left: 25%; animation-duration: 15s; animation-delay: 2.2s; font-size: 1.5em;">❄</div>
<div class="snowflake" style="left: 35%; animation-duration: 14s; animation-delay: 1.8s; font-size: 1.0em;">❄</div>
<div class="snowflake" style="left: 45%; animation-duration: 12s; animation-delay: 3.2s; font-size: 1.9em;">❄</div>
<div class="snowflake" style="left: 55%; animation-duration: 13s; animation-delay: 0.3s; font-size: 1.3em;">❄</div>
<div class="snowflake" style="left: 65%; animation-duration: 16s; animation-delay: 2.8s; font-size: 1.1em;">❄</div>
<div class="snowflake" style="left: 75%; animation-duration: 11s; animation-delay: 1.2s; font-size: 1.6em;">❄</div>
<div class="snowflake" style="left: 85%; animation-duration: 14s; animation-delay: 3.8s; font-size: 1.4em;">❄</div>
<div class="snowflake" style="left: 95%; animation-duration: 15s; animation-delay: 0.6s; font-size: 1.2em;">❄</div>
<div class="snowflake" style="left: 5%; animation-duration: 12s; animation-delay: 2.6s; font-size: 1.7em;">❄</div>
<div class="snowflake" style="left: 12%; animation-duration: 13s; animation-delay: 4.2s; font-size: 1.0em;">❄</div>
""", unsafe_allow_html=True)

# --- Spider hanging on the right ---
st.markdown("""
<div class="spider-container">
    <div class="spider-web"></div>
    <div class="spider">🕷️</div>
</div>
""", unsafe_allow_html=True)

# --- Cat on the right side ---
st.markdown("""
<div class="cat-container">
    <div class="cat">🐱</div>
</div>
""", unsafe_allow_html=True)

# --- User Authentication Section ---
if st.session_state.user_info:
    # User is signed in - show welcome message with name and email
    user_name = st.session_state.user_info.get('name', 'Benutzer')
    user_email = st.session_state.user_info.get('email', '')
    user_picture = st.session_state.user_info.get('picture', '')

    # Build the user info display
    profile_img = f'<img src="{user_picture}" style="width: 60px; height: 60px; border-radius: 50%; border: 3px solid white; margin-bottom: 10px;" />' if user_picture else ''

    st.markdown(f"""
    <div class="info-box" style="text-align: center; margin: 1em 0; padding: 1.5em; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; border-left-color: white;">
        {profile_img}
        <h3 style="margin: 0; color: white !important; background: none !important; background-image: none !important; background-clip: initial !important; -webkit-background-clip: initial !important; -webkit-text-fill-color: white !important;">Willkommen, {user_name}! 👋</h3>
        <p style="margin: 0.5em 0 0 0; color: white !important; font-size: 1em;">📧 {user_email}</p>
        <p style="margin: 0.5em 0 0 0; color: white !important; font-size: 0.9em;">Schön, dass du da bist!</p>
    </div>
    """, unsafe_allow_html=True)
else:
    # User is not signed in - show optional sign-in
    if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
        st.markdown("""
        <div style="text-align: center; margin: 1em 0; padding: 1em; background: linear-gradient(135deg, #2d3e50 0%, #3d4e60 100%); border-radius: 15px; border: 2px solid #667eea;">
            <p style="margin: 0; color: white; font-weight: 600;">Melde dich optional mit deinem Google-Konto an für eine personalisierte Begrüßung</p>
        </div>
        """, unsafe_allow_html=True)

# --- Sign In / Sign Out Controls ---
auth_col1, auth_col2, auth_col3 = st.columns([1, 2, 1])
with auth_col2:
    if st.session_state.user_info:
        # Show sign-out button
        if st.button("🚪 Abmelden", key="sign_out", use_container_width=True):
            st.session_state.user_info = None
            st.session_state.oauth_state = None
            st.rerun()
    else:
        # Show sign-in button (optional)
        if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
            auth_url = get_google_auth_url()
            if auth_url:
                # Use native Streamlit link_button for better compatibility
                st.link_button(
                    "🔐 Mit Google anmelden (optional)",
                    auth_url,
                    use_container_width=True
                )

st.markdown("---")

# --- Dark Mode & Music Controls ---
col_left, col_center, col_right = st.columns([2, 3, 2])

with col_left:
    if st.button("🌙" if not dark_mode else "☀️", key="dark_mode_toggle"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

with col_center:
    aktuelles_datum = datetime.now().strftime("%d.%m.%Y")
    st.markdown(f"""
    <div style="text-align: center; color: #667eea; font-size: 1.1em; font-weight: 500;">
        🗓️ {aktuelles_datum}
    </div>
    """, unsafe_allow_html=True)

with col_right:
    if st.button("🎵 Weihnachtsmusik", key="music_toggle"):
        st.session_state.music_playing = not st.session_state.music_playing

# --- Weihnachtsmusik Player ---
if st.session_state.music_playing:
    st.markdown("""
    <div style="text-align: center; margin: 1em 0;">
        <audio autoplay loop>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
        </audio>
        <p style="color: #c41e3a; font-size: 0.9em;">🎵 Weihnachtsmusik spielt...</p>
    </div>
    """, unsafe_allow_html=True)

# --- Stock Price Tracker ---
st.markdown("---")
st.markdown("""
<div class="info-box">
    <h3 style="margin-top: 0;">📈 Aktien-Kurs Tracker</h3>
    <p>Gib einen Firmennamen oder ein Aktien-Symbol ein (z.B. MSFT, AAPL, TSLA)</p>
</div>
""", unsafe_allow_html=True)

company_input = st.text_input("Firmenname oder Aktien-Symbol", placeholder="z.B. MSFT, AAPL, GOOGL, TSLA")

if company_input:
    try:
        # Fetch stock data
        ticker = yf.Ticker(company_input.upper())

        # Get current data
        info = ticker.info
        hist = ticker.history(period="6mo")  # Get 6 months of historical data

        if not hist.empty:
            current_price = hist['Close'].iloc[-1]
            prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else current_price
            price_change = current_price - prev_close
            price_change_pct = (price_change / prev_close * 100) if prev_close != 0 else 0

            # Display current price
            change_color = "green" if price_change >= 0 else "red"
            change_symbol = "📈" if price_change >= 0 else "📉"

            company_name = info.get('longName', company_input.upper())

            st.markdown(f"""
            <div class="info-box" style="border-left-color: {change_color};">
                <h2 style="margin-top: 0; text-align: center;">{company_name}</h2>
                <p style="text-align: center; font-size: 2em; font-weight: 700; color: {change_color};">
                    ${current_price:.2f}
                </p>
                <p style="text-align: center; font-size: 1.2em; color: {change_color};">
                    {change_symbol} {price_change:+.2f} ({price_change_pct:+.2f}%)
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Create historical price chart
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(hist.index, hist['Close'], linewidth=2, color='#667eea', label='Schlusskurs')
            ax.fill_between(hist.index, hist['Close'], alpha=0.3, color='#667eea')

            ax.set_xlabel('Datum', fontsize=11)
            ax.set_ylabel('Preis (USD)', fontsize=11)
            ax.set_title(f'{company_name} - Kursverlauf (6 Monate)', fontsize=13, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()

            st.pyplot(fig)

            # Additional stock information
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                <div style="text-align: center; padding: 10px;">
                    <p style="font-size: 0.9em; color: #667eea;">📊 Höchstkurs (52 Wo.)</p>
                    <p style="font-size: 1.3em; font-weight: 600;">${info.get('fiftyTwoWeekHigh', 'N/A')}</p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div style="text-align: center; padding: 10px;">
                    <p style="font-size: 0.9em; color: #667eea;">📉 Tiefstkurs (52 Wo.)</p>
                    <p style="font-size: 1.3em; font-weight: 600;">${info.get('fiftyTwoWeekLow', 'N/A')}</p>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                market_cap = info.get('marketCap', 0)
                if market_cap:
                    market_cap_b = market_cap / 1_000_000_000
                    st.markdown(f"""
                    <div style="text-align: center; padding: 10px;">
                        <p style="font-size: 0.9em; color: #667eea;">💰 Marktkapitalisierung</p>
                        <p style="font-size: 1.3em; font-weight: 600;">${market_cap_b:.2f}B</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="text-align: center; padding: 10px;">
                        <p style="font-size: 0.9em; color: #667eea;">💰 Marktkapitalisierung</p>
                        <p style="font-size: 1.3em; font-weight: 600;">N/A</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.warning(f"⚠️ Keine Daten für '{company_input}' gefunden. Bitte überprüfe das Symbol.")

    except Exception as e:
        st.error(f"❌ Fehler beim Abrufen der Aktiendaten: {str(e)}")
        st.info("💡 Tipp: Versuche es mit einem bekannten Aktien-Symbol wie MSFT, AAPL, GOOGL oder TSLA")

st.markdown("---")

# --- Einführungstext ---
st.markdown("""
### Gesundheit verstehen – Ernährung, Bewegung und mehr

Eine ausgewogene **Ernährung** und regelmäßige **Bewegung** sind die Basis für körperliche und geistige Gesundheit. Sie tragen wesentlich dazu bei, Krankheiten vorzubeugen, das Wohlbefinden zu steigern und die Leistungsfähigkeit zu erhalten.

Ein einfaches, aber weit verbreitetes Maß zur Einschätzung des Körpergewichts in Relation zur Körpergröße ist der **Body-Mass-Index (BMI)**. Auch wenn der BMI nicht zwischen Muskel- und Fettmasse unterscheidet und damit nur eine grobe Orientierung bietet, kann er helfen, erste Hinweise auf mögliche gesundheitliche Risiken zu geben.
""")

st.markdown("---")
st.markdown("### Fit mit Technik: Was dein Körper dir sonst noch sagt")

st.markdown("""
Mit dem folgenden **BMI-Rechner** kannst du deinen persönlichen Wert berechnen und in einer farblich gekennzeichneten Grafik sehen, in welche Kategorie dein Ergebnis fällt – von *Untergewicht* über *Normalgewicht* bis zu *Adipositas*. Die Darstellung macht deine Einordnung im Gesamtspektrum leicht verständlich.

Der **BMI** ist allerdings nur ein Baustein in der Beurteilung der Gesundheit. Weitere wichtige Messgrößen lassen sich mit moderner Technik erfassen, zum Beispiel:
""")

# --- Produktempfehlungen ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="product-card">
        <div style="text-align: center; font-size: 4em; margin-bottom: 0.3em;">📊</div>
        <h4 style="text-align: center; margin-top: 0;">Körperfettwaagen</h4>
        <p style="text-align: center;">Sie messen neben dem Gewicht auch Körperfettanteil, Muskelmasse und Wasseranteil.</p>
        <div style="text-align: center; margin-top: 1em;">
            <a href="https://www.withings.com/de/de/body-comp" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.6em 1.5em; border-radius: 8px; text-decoration: none; font-weight: 600;">Mehr erfahren →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="product-card">
        <div style="text-align: center; font-size: 4em; margin-bottom: 0.3em;">⌚</div>
        <h4 style="text-align: center; margin-top: 0;">Fitness-Tracker</h4>
        <p style="text-align: center;">Diese liefern Daten zu Herzfrequenz, Schlafqualität, Aktivitätsniveau und mehr.</p>
        <div style="text-align: center; margin-top: 1em;">
            <a href="https://www.withings.com/de/de/scanwatch-nova" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.6em 1.5em; border-radius: 8px; text-decoration: none; font-weight: 600;">Mehr erfahren →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
In Kombination geben diese Werte ein umfassenderes Bild deiner körperlichen Verfassung.
""")
st.markdown("---")

# --- Eingaben ---
st.markdown("""
<div class="info-box">
    <h3 style="margin-top: 0;">🧮 Berechne deinen BMI</h3>
    <p>Gib deine Daten ein, um deinen persönlichen Body-Mass-Index zu berechnen.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    gewicht = st.number_input("Gewicht (in kg)", min_value=30.0, max_value=300.0, value=75.0)
with col2:
    groesse = st.number_input("Größe (in cm)", min_value=100.0, max_value=250.0, value=175.0)

# --- Button ---
if st.button("✨ BMI berechnen"):
    bmi = gewicht / ((groesse / 100) ** 2)

    # Bewertung
    if bmi < 18.5:
        kategorie = "Untergewicht"
        farbe = "yellow"
        kategorie_emoji = "⚠️"
    elif bmi < 25:
        kategorie = "Normalgewicht"
        farbe = "green"
        kategorie_emoji = "✅"
    elif bmi < 30:
        kategorie = "Übergewicht"
        farbe = "orange"
        kategorie_emoji = "⚠️"
    else:
        kategorie = "Adipositas"
        farbe = "red"
        kategorie_emoji = "🔴"

    st.markdown(f"""
    <div class="info-box" style="border-left-color: {farbe};">
        <h2 style="margin-top: 0; text-align: center;">Dein BMI: <strong>{bmi:.1f}</strong></h2>
        <p style="text-align: center; font-size: 1.2em;">{kategorie_emoji} <strong>Kategorie:</strong> {kategorie}</p>
    </div>
    """, unsafe_allow_html=True)

    # BMI Verlauf speichern
    st.session_state.bmi_history.append({
        'datum': datetime.now(),
        'bmi': bmi,
        'gewicht': gewicht,
        'groesse': groesse
    })

    # --- Grafik ---
    fig, ax = plt.subplots(figsize=(8, 1.5))

    bereiche = [
        (10, 18.5, 'Untergewicht', 'yellow'),
        (18.5, 25, 'Normalgewicht', 'green'),
        (25, 30, 'Übergewicht', 'orange'),
        (30, 40, 'Adipositas', 'red'),
    ]

    for start, end, label, color in bereiche:
        ax.axvspan(start, end, color=color, alpha=0.5)
        ax.text((start + end) / 2, 0.7, label, ha='center', va='center', fontsize=9)

    ax.axvline(bmi, color="black", linewidth=3)
    ax.text(bmi + 0.4, 0.05, f"{bmi:.1f}", ha='left', va='bottom', fontsize=10, weight='bold')

    ax.set_xlim(10, 40)
    ax.set_ylim(0, 1.2)
    ax.set_yticks([])
    ax.set_xlabel("BMI", fontsize=10)
    ax.set_title("Einordnung deines BMI", fontsize=12)

    st.pyplot(fig)

# --- BMI Verlauf anzeigen ---
if len(st.session_state.bmi_history) > 0:
    st.markdown("---")
    st.markdown("### 📈 Dein BMI-Verlauf")

    df = pd.DataFrame(st.session_state.bmi_history)

    if len(df) > 1:
        fig2, ax2 = plt.subplots(figsize=(10, 4))
        ax2.plot(df['datum'], df['bmi'], marker='o', linewidth=2, markersize=8, color='#667eea')
        ax2.axhline(y=18.5, color='yellow', linestyle='--', alpha=0.5, label='Untergewicht')
        ax2.axhline(y=25, color='green', linestyle='--', alpha=0.5, label='Normalgewicht')
        ax2.axhline(y=30, color='orange', linestyle='--', alpha=0.5, label='Übergewicht')
        ax2.set_ylabel('BMI', fontsize=11)
        ax2.set_xlabel('Datum', fontsize=11)
        ax2.set_title('BMI-Entwicklung über Zeit', fontsize=13, fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig2)
    else:
        st.info("📊 Berechne deinen BMI mehrmals, um den Verlauf zu sehen!")

    # Reset-Button für Verlauf
    if st.button("🗑️ Verlauf löschen"):
        st.session_state.bmi_history = []
        st.rerun()

# --- Kalorienbedarf-Rechner ---
st.markdown("---")
st.markdown("""
<div class="info-box">
    <h3 style="margin-top: 0;">🔥 Kalorienbedarf berechnen</h3>
    <p>Berechne deinen täglichen Kalorienbedarf basierend auf der Harris-Benedict-Formel.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    alter = st.number_input("Alter (Jahre)", min_value=10, max_value=120, value=30)
with col2:
    geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])
with col3:
    aktivitaet = st.selectbox("Aktivitätslevel",
                              ["Sitzend", "Leicht aktiv", "Mäßig aktiv", "Sehr aktiv", "Extrem aktiv"])

if st.button("🔥 Kalorienbedarf berechnen"):
    # Harris-Benedict-Formel
    if geschlecht == "Männlich":
        grundumsatz = 88.362 + (13.397 * gewicht) + (4.799 * groesse) - (5.677 * alter)
    else:
        grundumsatz = 447.593 + (9.247 * gewicht) + (3.098 * groesse) - (4.330 * alter)

    # PAL-Faktoren
    pal_faktoren = {
        "Sitzend": 1.2,
        "Leicht aktiv": 1.375,
        "Mäßig aktiv": 1.55,
        "Sehr aktiv": 1.725,
        "Extrem aktiv": 1.9
    }

    gesamtumsatz = grundumsatz * pal_faktoren[aktivitaet]

    st.markdown(f"""
    <div class="info-box">
        <h3 style="text-align: center;">Dein Kalorienbedarf</h3>
        <p style="text-align: center; font-size: 1.1em;">
            💪 <strong>Grundumsatz:</strong> {grundumsatz:.0f} kcal/Tag<br>
            🔥 <strong>Gesamtumsatz:</strong> {gesamtumsatz:.0f} kcal/Tag
        </p>
        <hr>
        <p style="font-size: 0.95em;">
            📉 <strong>Abnehmen:</strong> {gesamtumsatz - 500:.0f} kcal/Tag (-500 kcal)<br>
            ⚖️ <strong>Gewicht halten:</strong> {gesamtumsatz:.0f} kcal/Tag<br>
            📈 <strong>Zunehmen:</strong> {gesamtumsatz + 500:.0f} kcal/Tag (+500 kcal)
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- Wasserbedarf-Rechner ---
st.markdown("---")
st.markdown("""
<div class="info-box">
    <h3 style="margin-top: 0;">💧 Täglicher Wasserbedarf</h3>
    <p>Berechne, wie viel Wasser du täglich trinken solltest.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    sport_minuten = st.number_input("Sport pro Tag (Minuten)", min_value=0, max_value=300, value=30)
with col2:
    temperatur = st.selectbox("Außentemperatur", ["< 20°C", "20-25°C", "> 25°C"])

if st.button("💧 Wasserbedarf berechnen"):
    # Grundformel: 35ml pro kg Körpergewicht
    basis_wasserbedarf = gewicht * 0.035

    # Zusätzlicher Bedarf durch Sport (0.5L pro 30min)
    sport_zusatz = (sport_minuten / 30) * 0.5

    # Temperatur-Zuschlag
    temp_faktoren = {
        "< 20°C": 0,
        "20-25°C": 0.3,
        "> 25°C": 0.6
    }
    temp_zusatz = temp_faktoren[temperatur]

    gesamt_wasser = basis_wasserbedarf + sport_zusatz + temp_zusatz

    st.markdown(f"""
    <div class="info-box">
        <h3 style="text-align: center;">💧 Dein Wasserbedarf</h3>
        <p style="text-align: center; font-size: 1.3em;">
            <strong>{gesamt_wasser:.1f} Liter</strong> pro Tag
        </p>
        <p style="text-align: center; font-size: 0.95em;">
            Das entspricht etwa <strong>{int(gesamt_wasser * 4)} Gläser</strong> (à 250ml)
        </p>
        <hr>
        <p style="font-size: 0.9em;">
            💡 <strong>Tipp:</strong> Trinke regelmäßig über den Tag verteilt.<br>
            🏃 Bei Sport: Zusätzlich ca. {sport_zusatz:.1f}L<br>
            🌡️ Bei Hitze: Zusätzlich ca. {temp_zusatz:.1f}L
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- Essen Zeche & Stahl Tetris Game ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2em;">
    <h2>⚒️ Essen Zeche & Stahl Tetris - Ruhrpott Challenge! 🏭</h2>
    <p style="color: #1a1a1a; font-size: 1.1em;">Stapel Kohle und Stahl wie in den alten Zechen und Hochöfen des Ruhrgebiets!</p>
    <p style="color: #666; font-size: 0.95em;">Eine Hommage an die Industriegeschichte von Essen - Zeche Zollverein, ThyssenKrupp & mehr</p>
</div>
""", unsafe_allow_html=True)

tetris_html = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        @keyframes snowfall {
            0% {
                transform: translateY(-10px) translateX(0);
                opacity: 1;
            }
            100% {
                transform: translateY(100vh) translateX(50px);
                opacity: 0.3;
            }
        }

        @keyframes sleighMove {
            0%, 100% {
                transform: translateX(-10px);
            }
            50% {
                transform: translateX(10px);
            }
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 50%, #3d3d3d 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }

        .spark {
            position: fixed;
            top: -10px;
            color: #ff6b35;
            font-size: 1em;
            animation: snowfall linear infinite;
            pointer-events: none;
            z-index: 1;
        }

        .game-container {
            background: linear-gradient(135deg, #e8e8e8 0%, #d0d0d0 100%);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 40px rgba(0, 0, 0, 0.4), 0 0 60px rgba(255, 107, 53, 0.3);
            max-width: 500px;
            width: 100%;
            position: relative;
            z-index: 10;
            border: 3px solid #2d2d2d;
        }

        .game-header {
            text-align: center;
            margin-bottom: 20px;
            position: relative;
        }

        .game-header h1 {
            background: linear-gradient(135deg, #1a1a1a 0%, #ff6b35 50%, #4a4a4a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 1.8em;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        .industrial-icon {
            font-size: 3em;
            animation: sleighMove 3s ease-in-out infinite;
            display: inline-block;
        }

        .score-board {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
            padding: 15px;
            background: linear-gradient(135deg, #1a1a1a 0%, #ff6b35 50%, #4a4a4a 100%);
            border-radius: 12px;
            color: white;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
        }

        .score-item {
            text-align: center;
        }

        .score-label {
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 5px;
            font-weight: 600;
        }

        .score-value {
            font-size: 1.8em;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .canvas-wrapper {
            display: flex;
            justify-content: center;
            margin: 20px 0;
            position: relative;
        }

        canvas {
            border: 4px solid #2d2d2d;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(255, 107, 53, 0.1);
            background: linear-gradient(180deg, #f5f5f5 0%, #e0e0e0 100%);
        }

        .controls {
            text-align: center;
            margin-top: 20px;
        }

        .btn {
            background: linear-gradient(135deg, #2d2d2d 0%, #ff6b35 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 10px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
            transition: all 0.3s ease;
            margin: 5px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(255, 107, 53, 0.6);
            background: linear-gradient(135deg, #1a1a1a 0%, #ff8c5a 100%);
        }

        .instructions {
            margin-top: 20px;
            padding: 15px;
            background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
            border-radius: 10px;
            border-left: 4px solid #2d2d2d;
            border-right: 4px solid #ff6b35;
        }

        .instructions h3 {
            color: #2d2d2d;
            margin-bottom: 10px;
            font-size: 1.1em;
        }

        .instructions ul {
            list-style: none;
            padding-left: 0;
        }

        .instructions li {
            padding: 5px 0;
            color: #4a4a4a;
            font-weight: 500;
        }

        .game-over {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, #e8e8e8 0%, #d0d0d0 100%);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 50px rgba(0, 0, 0, 0.5);
            text-align: center;
            z-index: 1000;
            border: 3px solid #2d2d2d;
        }

        .game-over.show {
            display: block;
        }

        .overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(26, 26, 26, 0.85);
            z-index: 999;
        }

        .overlay.show {
            display: block;
        }

        .christmas-lights {
            display: flex;
            justify-content: space-around;
            margin-bottom: 15px;
        }

        .light {
            width: 15px;
            height: 20px;
            border-radius: 50% 50% 40% 40%;
            animation: blink 1s infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }

        .light:nth-child(1) { background: #1a1a1a; animation-delay: 0s; }
        .light:nth-child(2) { background: #ff6b35; animation-delay: 0.2s; }
        .light:nth-child(3) { background: #808080; animation-delay: 0.4s; }
        .light:nth-child(4) { background: #4a4a4a; animation-delay: 0.6s; }
        .light:nth-child(5) { background: #ff8c5a; animation-delay: 0.8s; }
        .light:nth-child(6) { background: #2d2d2d; animation-delay: 1s; }
    </style>
</head>
<body>
    <div class="game-container">
        <div class="christmas-lights">
            <div class="light"></div>
            <div class="light"></div>
            <div class="light"></div>
            <div class="light"></div>
            <div class="light"></div>
            <div class="light"></div>
        </div>

        <div class="game-header">
            <div class="industrial-icon">⚒️🏭</div>
            <h1>⛏️ Essen Zeche & Stahl Tetris ⚙️</h1>
            <p style="color: #2d2d2d; font-size: 0.9em; margin-top: 5px;">Stapel Kohle und Stahl wie im Ruhrpott!</p>
        </div>

        <div class="score-board">
            <div class="score-item">
                <div class="score-label">⚙️ Punkte</div>
                <div class="score-value" id="score">0</div>
            </div>
            <div class="score-item">
                <div class="score-label">🏭 Level</div>
                <div class="score-value" id="level">1</div>
            </div>
            <div class="score-item">
                <div class="score-label">⚒️ Zeilen</div>
                <div class="score-value" id="lines">0</div>
            </div>
        </div>

        <div class="canvas-wrapper">
            <canvas id="tetris" width="240" height="400"></canvas>
        </div>

        <div class="controls">
            <button class="btn" onclick="startGame()">⚒️ Schicht beginnen</button>
            <button class="btn" onclick="pauseGame()">⏸ Pause</button>
        </div>

        <div class="instructions">
            <h3>⚙️ Steuerung</h3>
            <ul>
                <li>⬅️ ➡️ Pfeiltasten: Material bewegen</li>
                <li>⬆️ Pfeil hoch: Material drehen</li>
                <li>⬇️ Pfeil runter: Schneller fallen lassen</li>
                <li>🏭 Leertaste: Sofort im Hochofen verstauen</li>
            </ul>
        </div>
    </div>

    <div class="overlay" id="overlay"></div>
    <div class="game-over" id="gameOver">
        <h2 style="background: linear-gradient(135deg, #1a1a1a 0%, #ff6b35 50%, #4a4a4a 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5em; margin-bottom: 20px;">⚒️ Feierabend! 🏭</h2>
        <p style="font-size: 1.3em; margin-bottom: 10px; color: #2d2d2d;">Die Zeche ist voll!</p>
        <p style="font-size: 1.5em; margin-bottom: 10px;">⚙️ Punkte: <span id="finalScore">0</span></p>
        <p style="font-size: 1.2em; margin-bottom: 30px; color: #4a4a4a;">🏭 Level: <span id="finalLevel">1</span> | ⚒️ Zeilen: <span id="finalLines">0</span></p>
        <button class="btn" onclick="restartGame()">🔄 Neue Schicht starten</button>
    </div>

    <script>
        const canvas = document.getElementById('tetris');
        const ctx = canvas.getContext('2d');
        const ROWS = 20;
        const COLS = 12;
        const BLOCK_SIZE = 20;

        let board = Array(ROWS).fill().map(() => Array(COLS).fill(0));
        let score = 0;
        let level = 1;
        let lines = 0;
        let gameRunning = false;
        let gamePaused = false;
        let dropInterval;
        let currentPiece;
        let currentX;
        let currentY;

        const SHAPES = [
            [[1,1,1,1]], // I
            [[1,1],[1,1]], // O
            [[0,1,0],[1,1,1]], // T
            [[1,0,0],[1,1,1]], // L
            [[0,0,1],[1,1,1]], // J
            [[0,1,1],[1,1,0]], // S
            [[1,1,0],[0,1,1]]  // Z
        ];

        const COLORS = [
            '#1a1a1a', // I - Kohle (Schwarz)
            '#808080', // O - Stahl (Grau)
            '#ff6b35', // T - Glühender Stahl (Orange)
            '#4a4a4a', // L - Dunkelgrau (Eisen)
            '#c0c0c0', // J - Silber (Stahl)
            '#ff8c5a', // S - Helles Orange (Hochofen)
            '#2d2d2d'  // Z - Anthrazit (Kohle)
        ];

        function drawBlock(x, y, color) {
            ctx.fillStyle = color;
            ctx.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);

            // Add a slight gradient for 3D effect
            const gradient = ctx.createLinearGradient(
                x * BLOCK_SIZE, y * BLOCK_SIZE,
                (x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE
            );
            gradient.addColorStop(0, 'rgba(255, 255, 255, 0.3)');
            gradient.addColorStop(1, 'rgba(0, 0, 0, 0.3)');
            ctx.fillStyle = gradient;
            ctx.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);

            // Draw border
            ctx.strokeStyle = color === '#ffffff' ? '#c0c0c0' : '#fff';
            ctx.lineWidth = 2;
            ctx.strokeRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
        }

        function drawBoard() {
            ctx.fillStyle = '#f5f7fa';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            for (let row = 0; row < ROWS; row++) {
                for (let col = 0; col < COLS; col++) {
                    if (board[row][col]) {
                        drawBlock(col, row, COLORS[board[row][col] - 1]);
                    }
                }
            }
        }

        function drawPiece() {
            const shape = SHAPES[currentPiece];
            const color = COLORS[currentPiece];

            for (let row = 0; row < shape.length; row++) {
                for (let col = 0; col < shape[row].length; col++) {
                    if (shape[row][col]) {
                        drawBlock(currentX + col, currentY + row, color);
                    }
                }
            }
        }

        function collision(piece, x, y) {
            const shape = SHAPES[piece];
            for (let row = 0; row < shape.length; row++) {
                for (let col = 0; col < shape[row].length; col++) {
                    if (shape[row][col]) {
                        const newX = x + col;
                        const newY = y + row;

                        if (newX < 0 || newX >= COLS || newY >= ROWS) {
                            return true;
                        }
                        if (newY >= 0 && board[newY][newX]) {
                            return true;
                        }
                    }
                }
            }
            return false;
        }

        function merge() {
            const shape = SHAPES[currentPiece];
            for (let row = 0; row < shape.length; row++) {
                for (let col = 0; col < shape[row].length; col++) {
                    if (shape[row][col]) {
                        const y = currentY + row;
                        const x = currentX + col;
                        if (y >= 0) {
                            board[y][x] = currentPiece + 1;
                        }
                    }
                }
            }
        }

        function rotate(piece) {
            const shape = SHAPES[piece];
            const newShape = [];
            for (let i = 0; i < shape[0].length; i++) {
                newShape[i] = [];
                for (let j = shape.length - 1; j >= 0; j--) {
                    newShape[i][shape.length - 1 - j] = shape[j][i];
                }
            }
            return newShape;
        }

        function clearLines() {
            let linesCleared = 0;
            for (let row = ROWS - 1; row >= 0; row--) {
                if (board[row].every(cell => cell !== 0)) {
                    board.splice(row, 1);
                    board.unshift(Array(COLS).fill(0));
                    linesCleared++;
                    row++;
                }
            }

            if (linesCleared > 0) {
                lines += linesCleared;
                score += linesCleared * 100 * level;
                level = Math.floor(lines / 10) + 1;
                updateScore();

                clearInterval(dropInterval);
                dropInterval = setInterval(drop, Math.max(100, 1000 - (level - 1) * 100));
            }
        }

        function newPiece() {
            currentPiece = Math.floor(Math.random() * SHAPES.length);
            currentX = Math.floor(COLS / 2) - 1;
            currentY = 0;

            if (collision(currentPiece, currentX, currentY)) {
                gameOver();
            }
        }

        function drop() {
            if (!gamePaused && gameRunning) {
                if (!collision(currentPiece, currentX, currentY + 1)) {
                    currentY++;
                } else {
                    merge();
                    clearLines();
                    newPiece();
                }
                draw();
            }
        }

        function draw() {
            drawBoard();
            drawPiece();
        }

        function updateScore() {
            document.getElementById('score').textContent = score;
            document.getElementById('level').textContent = level;
            document.getElementById('lines').textContent = lines;
        }

        function startGame() {
            if (!gameRunning) {
                board = Array(ROWS).fill().map(() => Array(COLS).fill(0));
                score = 0;
                level = 1;
                lines = 0;
                updateScore();
                gameRunning = true;
                gamePaused = false;

                newPiece();
                clearInterval(dropInterval);
                dropInterval = setInterval(drop, 1000);
                draw();
            }
        }

        function pauseGame() {
            if (gameRunning) {
                gamePaused = !gamePaused;
            }
        }

        function gameOver() {
            gameRunning = false;
            clearInterval(dropInterval);

            document.getElementById('finalScore').textContent = score;
            document.getElementById('finalLevel').textContent = level;
            document.getElementById('finalLines').textContent = lines;

            document.getElementById('overlay').classList.add('show');
            document.getElementById('gameOver').classList.add('show');
        }

        function restartGame() {
            document.getElementById('overlay').classList.remove('show');
            document.getElementById('gameOver').classList.remove('show');
            startGame();
        }

        document.addEventListener('keydown', (e) => {
            if (!gameRunning || gamePaused) return;

            e.preventDefault();

            switch(e.key) {
                case 'ArrowLeft':
                    if (!collision(currentPiece, currentX - 1, currentY)) {
                        currentX--;
                    }
                    break;
                case 'ArrowRight':
                    if (!collision(currentPiece, currentX + 1, currentY)) {
                        currentX++;
                    }
                    break;
                case 'ArrowDown':
                    if (!collision(currentPiece, currentX, currentY + 1)) {
                        currentY++;
                        score += 1;
                        updateScore();
                    }
                    break;
                case 'ArrowUp':
                    const originalShape = SHAPES[currentPiece];
                    SHAPES[currentPiece] = rotate(currentPiece);
                    if (collision(currentPiece, currentX, currentY)) {
                        SHAPES[currentPiece] = originalShape;
                    }
                    break;
                case ' ':
                    while (!collision(currentPiece, currentX, currentY + 1)) {
                        currentY++;
                        score += 2;
                    }
                    updateScore();
                    break;
            }

            draw();
        });

        // Initial draw
        drawBoard();

        // Create sparks (industrial particles)
        function createSparks() {
            const sparkChars = ['⚙', '⚒', '🔩', '⚡'];
            for (let i = 0; i < 30; i++) {
                const spark = document.createElement('div');
                spark.classList.add('spark');
                spark.textContent = sparkChars[Math.floor(Math.random() * sparkChars.length)];
                spark.style.left = Math.random() * 100 + '%';
                spark.style.animationDuration = (Math.random() * 3 + 2) + 's';
                spark.style.animationDelay = Math.random() * 5 + 's';
                spark.style.fontSize = (Math.random() * 1 + 0.5) + 'em';
                spark.style.opacity = Math.random() * 0.6 + 0.4;
                document.body.appendChild(spark);
            }
        }

        // Initialize sparks
        createSparks();
    </script>
</body>
</html>
"""

components.html(tetris_html, height=900, scrolling=False)

# --- PayPal Donation Section ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2em; margin-bottom: 2em;">
    <div class="product-card" style="max-width: 600px; margin: 0 auto; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border: 3px solid #667eea;">
        <div style="text-align: center; font-size: 3em; margin-bottom: 0.5em;">💝</div>
        <h3 style="text-align: center; color: white !important; margin-bottom: 0.5em;">
            Gefällt dir diese App?
        </h3>
        <p style="text-align: center; color: white; margin-bottom: 1.5em; font-size: 1.05em;">
            Wenn dir diese App weitergeholfen hat und du meine Arbeit unterstützen möchtest, freue ich mich über eine kleine Spende!
        </p>
        <div style="text-align: center;">
            <a href="https://paypal.me/GunnarHoffmann2/1" target="_blank" rel="noopener noreferrer" style="display: inline-block; background: linear-gradient(135deg, #0070ba 0%, #1546a0 100%); color: white; padding: 1em 2.5em; border-radius: 12px; text-decoration: none; font-weight: 700; font-size: 1.15em; box-shadow: 0 4px 15px rgba(0, 112, 186, 0.4); transition: all 0.3s ease;">
                <span style="font-size: 1.3em; margin-right: 0.3em;">💙</span> Spende via PayPal
            </a>
        </div>
        <p style="text-align: center; color: white; margin-top: 1em; font-size: 0.95em; font-weight: 600;">
            Vielen Dank für deine Unterstützung!
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
