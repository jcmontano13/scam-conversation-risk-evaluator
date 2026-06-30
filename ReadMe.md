# Scam Conversation Risk Evaluator

## Project Overview

This project builds a reproducible and interpretable machine learning pipeline for scam conversation detection using the BothBosu scam-dialogue dataset.

The project extracts compact thread-level structural features from redacted scam dialogue conversations and prepares them for later modelling using Logistic Regression and Decision Tree classifiers.

## Current Feature Set

The main engineered features are:

- `turn_count`
- `aggregate_num_urls`
- `aggregate_money_terms`
- `ratio_request_messages`

The target label is:

- `thread_label`

## Excluded Features

The project intentionally excludes:

- TF-IDF features
- Deep learning embeddings
- LLM-generated features
- LLM fine-tuning

These are excluded to preserve interpretability, reproducibility, and alignment with the project scope.

## Project Structure

```text
scam-conversation-risk-evaluator/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
├── outputs/
│   └── reports/
├── src/
│   ├── feature_engineering/
│   ├── preprocessing/
│   └── validation/
├── tests/
├── config.py
├── requirements.txt
└── README.md
```

## Setup
Create and activate a virtual environment:
```text
python -m venv .venv
.venv\Scripts\activate
```
Install Dependencies 
```text
pip install -r requirements.txt
```
## Exectution Order
1. Run the feature extraction script:
```text
python src/feature_engineering/parse_and_features.py
```
2. Run feature validation:
```text
python src/validation/check_features.py
```
3. Generate train/test split indices:
```text
python src/preprocessing/create_split_indices.py
```
4. Generate feature extraction metadata:
```text
python src/feature_engineering/generate_feature_metadata.py
```
5. Run unit checks:
```text
pytest tests/test_feature_extraction.py
```

## Generated Outputs
```text
data/processed/scam_dialogue_parsed.csv
data/processed/scam_dialogue_thread_features.csv
data/processed/split_indices.json
data/processed/feature_extraction_metadata.json
outputs/reports/feature_validation_report.txt
```

## Reproducibility
The project uses a fixed random seed:
```text
SEED = 42
```
The train/test split is saved in:
```text
data/processed/split_indices.json
```