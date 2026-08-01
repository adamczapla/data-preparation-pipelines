from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
IMPORTED_DATA_DIR = DATA_DIR / "imported"
CLEANED_DATA_DIR = DATA_DIR / "cleaned"
TRANSFORMED_DATA_DIR = DATA_DIR / "transformed"