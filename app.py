import streamlit as st
import matplotlib.pyplot as plt

# Seiteneinstellungen
st.set_page_config(page_title="BMI Rechner", page_icon="⚖️", layout="centered")

st.title("⚖️ BMI Rechner mit Visualisierung")
st.markdown("Berechne deinen Body-Mass-Index und sieh, wo du im Vergleich zu den BMI-Kategorien stehst.")

# Eingaben
gewicht = st.number_input("Gewicht (in kg)", min_value=30.0, max_value=300.0, value=75.0)
groesse = st.number_input("Größe (in cm)", min_value=100.0, max_value=250.0, value=175.0)

# Berechnung
if st.button("BMI berechnen"):
    bmi = gewicht / ((groesse / 100) ** 2)
    st.subheader(f"Dein BMI: {bmi:.1f}")

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

    st.markdown(f"**Kategorie:** {kategorie}")

    # Grafik erstellen
    fig, ax = plt.subplots(figsize=(8, 1.5))

    # Bereiche
    bereiche = [
        (0, 18.5, 'Untergewicht', 'yellow'),
        (18.5, 25, 'Normalgewicht', 'green'),
        (25, 30, 'Übergewicht', 'orange'),
        (30, 40, 'Adipositas', 'red'),
    ]

    for start, end, label, color in bereiche:
        ax.axvspan(start, end, color=color, alpha=0.6)
        ax.text((start + end) / 2, 0.6, label, ha='center', va='center', fontsize=9)

    # BMI-Linie
    ax.axvline(bmi, color="black", linewidth=3)
    ax.text(bmi, 1.1, f"{bmi:.1f}", ha='center', va='bottom', fontsize=10, weight='bold')

    # Achse
    ax.set_xlim(10, 40)
    ax.set_yticks([])
    ax.set_xlabel("BMI")
    ax.set_title("BMI-Klassifikation", fontsize=12)
    st.pyplot(fig)

# Fußzeile
st.markdown("---")
st.caption("Erstellt mit Streamlit – Dein BMI-Vergleichsrechner.")
