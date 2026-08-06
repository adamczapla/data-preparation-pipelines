from pathlib import Path
from typing import Final

PROJECT_ROOT: Final = Path(__file__).parent.parent
DATA_DIR: Final = PROJECT_ROOT / "data"
RAW_DATA_DIR: Final = DATA_DIR / "raw"
IMPORTED_DATA_DIR: Final = DATA_DIR / "imported"
CLEANED_DATA_DIR: Final = DATA_DIR / "cleaned"
TRANSFORMED_DATA_DIR: Final = DATA_DIR / "transformed"