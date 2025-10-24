import streamlit as st
import matplotlib.pyplot as plt

# --- Seitenlayout ---
st.set_page_config(
    page_title="BMI Rechner",
    page_icon="⚖️",
    layout="centered",
    
)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- CSS-Stil ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%) !important;
        color: #2c3e50 !important;
        font-family: 'Inter', sans-serif !important;
    }

    h1 {
        font-size: 2.5em;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        margin-bottom: 0.5em;
    }

    h2, h3 {
        color: #2c3e50;
        font-weight: 600;
    }

    .stButton>button {
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
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }

    /* Input Felder */
    .stNumberInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e7ff;
        padding: 0.75em;
        font-size: 1.1em;
        transition: all 0.3s ease;
    }

    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }

    /* Info Boxen */
    .info-box {
        background: white;
        border-radius: 15px;
        padding: 1.5em;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        margin: 1em 0;
        border-left: 4px solid #667eea;
    }

    /* Produktkarten */
    .product-card {
        background: white;
        border-radius: 15px;
        padding: 1.5em;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        margin: 1em 0;
        transition: all 0.3s ease;
    }

    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
    }

    /* Links */
    a {
        color: #667eea;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }

    a:hover {
        color: #764ba2;
    }

    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2em 0;
    }

    /* Markdown Text */
    .markdown-text-container {
        font-size: 1.05em;
        line-height: 1.8;
    }

    /* Subheader Styling */
    [data-testid="stMarkdownContainer"] h3 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
        margin-top: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# --- Titel ---
st.markdown("<h1>⚖️ BMI Rechner & Gesundheitsguide</h1>", unsafe_allow_html=True)

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

# --- Body Comp ---
st.markdown("""
<div class="product-card">
    <h4>📊 Körperfettwaagen</h4>
    <p>Sie messen neben dem Gewicht auch Körperfettanteil, Muskelmasse und Wasseranteil.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("[➜ Withings Body Comp ansehen](https://www.withings.com/de/de/body-comp)")
st.image("https://s3.us-west-2.amazonaws.com/gesundhait.de/bodycomp.png", caption="Withings Body Comp", width=200)

# --- ScanWatch Nova ---
st.markdown("""
<div class="product-card">
    <h4>⌚ Sportuhren / Fitness-Tracker</h4>
    <p>Diese liefern Daten zu Herzfrequenz, Schlafqualität, Aktivitätsniveau und mehr.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("[➜ Withings ScanWatch Nova ansehen](https://www.withings.com/de/de/scanwatch-nova)")
st.image("https://s3.us-west-2.amazonaws.com/gesundhait.de/swnova.png", caption="Withings ScanWatch Nova", width=200)

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
