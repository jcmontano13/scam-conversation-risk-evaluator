# Scam Conversation Risk Evaluator

## Project Overview

This project builds a reproducible and interpretable machine learning pipeline for scam conversation detection using the BothBosu scam-dialogue dataset.

The project extracts compact thread-level structural features from redacted scam dialogue conversations and evaluates explainable machine learning models, specifically Logistic Regression and Decision Tree classifiers.

The main goal is to compare whether a small set of structural conversation features can support scam conversation classification while keeping the pipeline transparent, auditable, and reproducible.

## Current Project Status

The technical pipeline is currently complete from feature extraction to internal freeze.

| Week | Focus | Status |
|---|---|---|
| Week 1 | Feature extraction, parsed turns, metadata, split indices | Complete |
| Week 2 | Feature dictionary, unit tests, README update | Complete |
| Week 3 | Baseline Logistic Regression and Decision Tree pipelines | Complete |
| Week 4 | Grid search, selected hyperparameters, CV variance report | Complete |
| Week 5 | Calibration experiments and proposed risk thresholds | Complete |
| Week 6 | Final test evaluation, ablation, interpretability, internal freeze | Complete |
| Week 7 | Final report and repository packaging | Pending |

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
- Real-time deployment
- New data collection
- User study

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
│   ├── evaluation/
│   ├── feature_engineering/
│   ├── models/
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
## Dataset Location
Place the raw dataset file in:
```text
data/raw/scam-dialogue_all.csv
```
## Execution Order
### 1. Feature Extraction
Run the feature extraction script:
```text
python src/feature_engineering/parse_and_features.py
```
Expected outputs:
```text
data/processed/scam_dialogue_parsed.csv
data/processed/scam_dialogue_thread_features.csv
```
### 2. Feature Validation
Run feature validation:
```text
python src/validation/check_features.py
```
Expected outputs:
```text
outputs/reports/feature_validation_report.txt
```
### 3. Train / Test Split
Generate train/test split indices:
```text
python src/preprocessing/create_split_indices.py
```
Expected outputs:
```text
data/processed/split_indices.json
```
### 4. Feature Metadata
Generate feature extraction metadata:
```text
python src/feature_engineering/generate_feature_metadata.py
```
Expected outputs:
```text
data/processed/feature_extraction_metadata.json
```
### 5. Unit Checks
Run unit checks:
```text
pytest tests/test_feature_extraction.py
```
Expected outputs:
```text
outputs/reports/unit_test_log.txt
```
### 6. Baseline Model Cross-Validation
Run baseline model cross-validation:
```text
python src/models/train_baseline_models.py
```
Expected outputs:
```text
outputs/reports/cv_results.csv
```
### 7. Cross-Validation Summary Report
Generate cross-validation summary report:
```text
python src/evaluation/generate_cv_summary_report.py
```
Expected outputs:
```text
outputs/reports/cv_summary_report.md
```
### 8. Held-Out Test Evaluation
Run final held-out test evaluation:
```text
python src/evaluation/evaluate_test_set.py
```
Expected outputs:
```text
outputs/reports/test_results.csv
outputs/reports/test_evaluation_report.md
```
### 9. Grid Search and Model Stability
Run grid search for selected baseline models:
```text
python src/models/tune_baseline_models.py
```
Expected outputs:
```text
outputs/reports/grid_search_results.csv
outputs/reports/selected_hyperparams.json
outputs/reports/cv_variance_report.md
outputs/reports/model_stability_note.md
```
### 10. Calibration Experiments
Run probability calibration experiments:
```text
python src/evaluation/calibration_experiments.py
```
Expected outputs:
```text
outputs/reports/calibration_results.csv
outputs/reports/calibration_report.md
outputs/reports/proposed_risk_thresholds.csv
```
### 11. Ablation Test
Run leave-one-feature-out ablation testing:
```text
python src/evaluation/ablation_test.py
```
Expected outputs:
```text
outputs/reports/ablation_results.csv
outputs/reports/ablation_report.md
```
### 12. Interpretability Artifacts
Generate model interpretability artifacts:
```text
python src/evaluation/interpretability_artifacts.py
```
Expected outputs:
```text
outputs/reports/coefficients_table.csv
outputs/reports/tree_feature_importance.csv
outputs/reports/decision_tree_rules.txt
outputs/reports/interpretability_report.md
```
## Generated Outputs
### Processed Data
```text
data/processed/scam_dialogue_parsed.csv
data/processed/scam_dialogue_thread_features.csv
data/processed/split_indices.json
data/processed/feature_extraction_metadata.json
```
### Documentation
```text
docs/feature_dictionary.md
README.md
```
### Validation and Testing Outputs
```text
outputs/reports/feature_validation_report.txt
outputs/reports/unit_test_log.txt
```
### Model Evaluation Outputs
```text
outputs/reports/cv_results.csv
outputs/reports/cv_summary_report.md
outputs/reports/test_results.csv
outputs/reports/test_evaluation_report.md
outputs/reports/grid_search_results.csv
outputs/reports/selected_hyperparams.json
outputs/reports/cv_variance_report.md
outputs/reports/model_stability_note.md
```
### Calibration Outputs
```text
outputs/reports/calibration_results.csv
outputs/reports/calibration_report.md
outputs/reports/proposed_risk_thresholds.csv
```
### Ablation Outputs
```text
outputs/reports/ablation_results.csv
outputs/reports/ablation_report.md
```
### Interpretability Outputs
```text
outputs/reports/coefficients_table.csv
outputs/reports/tree_feature_importance.csv
outputs/reports/decision_tree_rules.txt
outputs/reports/interpretability_report.md
```

## Results Summary
### Baseline Cross-Validation Results
 | Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8875 | 0.9097 | 0.8609 | 0.8841 | 0.9478 |
| Decision Tree | 0.8703 | 0.9102 | 0.8219 | 0.8637 | 0.9055 |
### Held-Out Test Evaluation
| Model               | Accuracy | Precision | Recall |     F1 | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -----: | ------: |
| Logistic Regression |   0.9063 |    0.9333 | 0.8750 | 0.9032 |  0.9590 |
| Decision Tree       |   0.8781 |    0.9231 | 0.8250 | 0.8713 |  0.9002 |

### Calibration Result
The selected calibration setup is:
```text
Logistic Regression with isotonic calibration
```
The proposed risk bands are:
| Risk Band | Probability Range |
| --------- | ----------------- |
| Low       | 0.00 to 0.26      |
| Medium    | 0.26 to 0.54      |
| High      | 0.54 to 1.01      |
### Ablation and Interpretability Summary
The strongest feature identified by ablation and interpretability analysis is:
```text
turn_count
```
Removing turn_count caused the largest F1 drop for both Logistic Regression and Decision Tree.

The feature importance order is:
```text
1. turn_count
2. aggregate_money_terms
3. ratio_request_messages
4. aggregate_num_urls
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
The dataset split is:
```text
Training rows: 1,280
Held-out test rows: 320
Total rows: 1,600
```
Cross-validation, grid search, calibration, ablation, and interpretability steps use the saved training rows where appropriate.

The held-out test set is reserved for final model evaluation and is not used for calibration, ablation, or interpretability decisions.
## Notebook Use
A notebook was used only for initial dataset exploration.

The main project pipeline was implemented using Python scripts instead of notebooks because scripts are easier to rerun, test, version-control, and audit. This supports the project goal of reproducibility.

