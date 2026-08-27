from pathlib import Path

# /data_generator.py

SEED = 42

# /main.py

NUM_CLIENTES = 2000

# /charts.py

FIGURE_SIZE = (12, 6)

TITLE_FONT_SIZE = 14

AZUL = '#636EFA'

LARANJA = '#EF553B'

DPI = 300

# Caminhos

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PATH = PROJECT_ROOT / "image"

PATH.mkdir(parents=True, exist_ok=True)