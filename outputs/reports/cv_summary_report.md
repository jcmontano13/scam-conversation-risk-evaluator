# Cross-Validation Summary Report

## Description

This report summarises the baseline model cross-validation results for the Scam Conversation Risk Evaluator project.

The models compared are:

- Logistic Regression
- Decision Tree

The models use only the four structural thread-level features:

- `turn_count`
- `aggregate_num_urls`
- `aggregate_money_terms`
- `ratio_request_messages`

## Evaluation Method

Stratified 5-fold cross-validation was performed using the training split only.

The held-out test set was not used in this stage. It remains reserved for final model evaluation.

## Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8875 (+/- 0.0155) | 0.9097 (+/- 0.0153) | 0.8609 (+/- 0.0347) | 0.8841 (+/- 0.0177) | 0.9478 (+/- 0.0140) |
| Decision Tree | 0.8703 (+/- 0.0114) | 0.9102 (+/- 0.0147) | 0.8219 (+/- 0.0167) | 0.8637 (+/- 0.0124) | 0.9055 (+/- 0.0178) |

## Best Model Summary

- Best model by F1 score: `Logistic Regression` (0.8841)
- Best model by ROC-AUC: `Logistic Regression` (0.9478)

## Interpretation

The best model by mean F1 score is Logistic Regression with an F1 score of 0.8841. The best model by mean ROC-AUC is Logistic Regression with a ROC-AUC score of 0.9478. These cross-validation results suggest which baseline model performs better on the training split before final held-out test evaluation. For scam detection, recall and F1 are especially important because missed scam cases may be more harmful than false alarms.

## Reproducibility Note

These results were generated from `cv_results.csv`, which was created by `train_baseline_models.py`.

Generated at: 2026-07-01T23:05:26
