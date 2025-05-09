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
st.markdown("- **Körperfettwaagen**: Sie messen neben dem Gewicht auch Körperfettanteil, Muskelmasse und Wasseranteil.")
st.markdown("[Withings Body Comp ansehen](https://www.withings.com/de/de/body-comp)")
st.image("https://s3.us-west-2.amazonaws.com/gesundhait.de/bodycomp.png", caption="Withings Body Comp", width=150)

# --- ScanWatch Nova ---
st.markdown("- **Sportuhren / Fitness-Tracker**: Diese liefern Daten zu Herzfrequenz, Schlafqualität, Aktivitätsniveau und mehr.")
st.markdown("[Withings ScanWatch Nova ansehen](https://www.withings.com/de/de/scanwatch-nova)")
st.image("https://s3.us-west-2.amazonaws.com/gesundhait.de/swnova.png", caption="Withings ScanWatch Nova", width=150)

st.markdown("""
In Kombination geben diese Werte ein umfassenderes Bild deiner körperlichen Verfassung.
""")
st.markdown("---")

# --- Eingaben ---
st.subheader("Gib deine Daten ein")

col1, col2 = st.columns(2)
with col1:
    gewicht = st.number_input("Gewicht (in kg)", min_value=30.0, max_value=300.0, value=75.0)
with col2:
    groesse = st.number_input("Größe (in cm)", min_value=100.0, max_value=250.0, value=175.0)

# --- Button ---
if st.button("BMI berechnen"):
    bmi = gewicht / ((groesse / 100) ** 2)
    st.subheader(f"Dein BMI beträgt: **{bmi:.1f}**")

    # Bewertung
    if bmi < 18.5:
        kategorie = "Untergewicht"
        farbe = "yellow"
    elif bmi < 25:
        kategorie = "Normalgewicht"
        farbe = "green"
    elif bmi < 30:
        kategorie = "Übergewicht"
        farbe = "orange"
    else:
        kategorie = "Adipositas"
        farbe = "red"

    st.markdown(f"**Kategorie:** _{kategorie}_")

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
