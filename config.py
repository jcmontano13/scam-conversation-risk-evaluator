from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

RAW_DATA = PROJECT_ROOT / "data" / "raw" / "scam-dialogue_all.csv"

SEED = 42

PARSED_DATA = PROJECT_ROOT / "data" / "processed" / "scam_dialogue_parsed.csv"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed" / "scam_dialogue_thread_features.csv"

VALIDATION_REPORT = PROJECT_ROOT / "outputs" / "reports" / "feature_validation_report.txt"

SPLIT_INDICES = PROJECT_ROOT / "data" / "processed" / "split_indices.json"

FEATURE_METADATA = PROJECT_ROOT / "data" / "processed" / "feature_extraction_metadata.json"