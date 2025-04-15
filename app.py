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

# BMI-Linie
ax.axvline(bmi, color="black", linewidth=3)
ax.text(bmi, 0.1, f"{bmi:.1f}", ha='center', va='bottom', fontsize=10, weight='bold')  # Unterhalb des Strichs

# Achsenformatierung
ax.set_xlim(10, 40)
ax.set_ylim(0, 1.2)
ax.set_yticks([])
ax.set_xlabel("BMI", fontsize=10)
ax.set_title("Einordnung deines BMI", fontsize=12)

# Anzeige
st.pyplot(fig)
