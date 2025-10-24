import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
from datetime import datetime

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
        min-height: 280px;
        display: flex;
        flex-direction: column;
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

# --- Datum ---
aktuelles_datum = datetime.now().strftime("%d.%m.%Y")
st.markdown(f"""
<div style="text-align: center; color: #667eea; font-size: 1.1em; margin-bottom: 1.5em; font-weight: 500;">
    🗓️ {aktuelles_datum}
</div>
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

# --- Tetris Game ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2em;">
    <h2>🎮 Tetris Game</h2>
    <p style="color: #667eea; font-size: 1.1em;">Entspanne dich mit einer Runde Tetris!</p>
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

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .game-container {
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 40px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            width: 100%;
        }

        .game-header {
            text-align: center;
            margin-bottom: 20px;
        }

        .game-header h1 {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2em;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .score-board {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            color: white;
        }

        .score-item {
            text-align: center;
        }

        .score-label {
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 5px;
        }

        .score-value {
            font-size: 1.8em;
            font-weight: 700;
        }

        .canvas-wrapper {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }

        canvas {
            border: 3px solid #667eea;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
        }

        .controls {
            text-align: center;
            margin-top: 20px;
        }

        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 10px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            transition: all 0.3s ease;
            margin: 5px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }

        .instructions {
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }

        .instructions h3 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.1em;
        }

        .instructions ul {
            list-style: none;
            padding-left: 0;
        }

        .instructions li {
            padding: 5px 0;
            color: #555;
        }

        .game-over {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 50px rgba(0, 0, 0, 0.3);
            text-align: center;
            z-index: 1000;
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
            background: rgba(0, 0, 0, 0.5);
            z-index: 999;
        }

        .overlay.show {
            display: block;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <div class="game-header">
            <h1>🎮 Tetris</h1>
        </div>

        <div class="score-board">
            <div class="score-item">
                <div class="score-label">Score</div>
                <div class="score-value" id="score">0</div>
            </div>
            <div class="score-item">
                <div class="score-label">Level</div>
                <div class="score-value" id="level">1</div>
            </div>
            <div class="score-item">
                <div class="score-label">Lines</div>
                <div class="score-value" id="lines">0</div>
            </div>
        </div>

        <div class="canvas-wrapper">
            <canvas id="tetris" width="240" height="400"></canvas>
        </div>

        <div class="controls">
            <button class="btn" onclick="startGame()">▶ Spiel starten</button>
            <button class="btn" onclick="pauseGame()">⏸ Pause</button>
        </div>

        <div class="instructions">
            <h3>📖 Steuerung</h3>
            <ul>
                <li>⬅️ ➡️ Pfeil links/rechts: Bewegen</li>
                <li>⬆️ Pfeil hoch: Drehen</li>
                <li>⬇️ Pfeil runter: Schneller fallen</li>
                <li>Leertaste: Sofort fallen lassen</li>
            </ul>
        </div>
    </div>

    <div class="overlay" id="overlay"></div>
    <div class="game-over" id="gameOver">
        <h2 style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5em; margin-bottom: 20px;">Game Over!</h2>
        <p style="font-size: 1.5em; margin-bottom: 10px;">Dein Score: <span id="finalScore">0</span></p>
        <p style="font-size: 1.2em; margin-bottom: 30px; color: #666;">Level: <span id="finalLevel">1</span> | Zeilen: <span id="finalLines">0</span></p>
        <button class="btn" onclick="restartGame()">🔄 Neues Spiel</button>
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
            '#667eea', // I
            '#764ba2', // O
            '#f093fb', // T
            '#4facfe', // L
            '#43e97b', // J
            '#fa709a', // S
            '#feca57'  // Z
        ];

        function drawBlock(x, y, color) {
            ctx.fillStyle = color;
            ctx.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
            ctx.strokeStyle = '#fff';
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
    </script>
</body>
</html>
"""

components.html(tetris_html, height=900, scrolling=False)
