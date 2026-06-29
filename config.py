from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

RAW_DATA = PROJECT_ROOT / "data" / "raw" / "scam-dialogue_all.csv"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed" / "features.csv"

SEED = 42