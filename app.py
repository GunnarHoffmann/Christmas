import streamlit as st
import matplotlib.pyplot as plt

# --- Seitenlayout ---
st.set_page_config(page_title="BMI Rechner", page_icon="⚖️", layout="centered")

# --- Stil (zentriert und moderner Look) ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    h1 {
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

# --- Überschrift ---
st.title("⚖️ BMI-Rechner mit Visualisierung")

st.markdown("""
Berechne deinen **Body-Mass-Index (BMI)** und sieh auf einen Blick, wo du im Vergleich zu den offiziellen Kategorien stehst.
""")

# --- Eingaben ---
st.subheader("Gib deine Daten ein")

col1, col2 = st.columns(2)
with col1:
    gewicht = st.number_input("Gewicht (in kg)", min_value=30.0, max_value=300.0, value=75.0, help="Dein aktuelles Körpergewicht in Kilogramm")
with col2:
    groesse = st.number_input("Größe (in cm)", min_value=100.0, max_value=250.0, value=175.0, help="Deine Körpergröße in Zentimetern")

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

    # --- Grafik erstellen ---
    fig, ax = plt.subplots(figsize=(8, 1.5))

    # Bereiche und Farben
    bereiche = [
        (10, 18.5, 'Untergewicht', 'yellow'),
        (18.5, 25, 'Normalgewicht', 'green'),
        (25, 30, 'Übergewicht', 'orange'),
        (30, 40, 'Adipositas', 'red'),
    ]

    for start, end, label, color in bereiche:
        ax.axvspan(start, end, color=color, alpha=0.5)
        ax.text((start + end) / 2, 0.7, label, ha='center', va='center', fontsize=9)

    # BMI-Linie und Beschriftung darunter
    ax.axvline(bmi, color="black", linewidth=3)
    ax.text(bmi, 0.05, f"{bmi:.1f}", ha='center', va='bottom', fontsize=10, weight='bold')  # Unterhalb der Linie

    # Achsenformatierung
    ax.set_xlim(10, 40)
    ax.set_ylim(0, 1.2)
    ax.set_yticks([])
    ax.set_xlabel("BMI", fontsize=10)
    ax.set_title("Einordnung deines BMI", fontsize=12)

    st.pyplot(fig)

# --- Footer ---
st.markdown("---")
st.caption("© BMI-Rechner | Erstellt mit Streamlit.")
