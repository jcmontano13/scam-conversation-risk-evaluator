# Held-Out Test Evaluation Report

## Description

This report summarises the final held-out test evaluation for the baseline models.

The models are trained using only `train_row_indices` from `split_indices.json` and evaluated using only `test_row_indices`.

## Features Used

- `turn_count`
- `aggregate_num_urls`
- `aggregate_money_terms`
- `ratio_request_messages`

## Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | TN | FP | FN | TP |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9062 | 0.9333 | 0.8750 | 0.9032 | 0.9590 | 150 | 10 | 20 | 140 |
| Decision Tree | 0.8781 | 0.9231 | 0.8250 | 0.8713 | 0.9002 | 149 | 11 | 28 | 132 |

## Best Model Summary

- Best model by F1 score: `Logistic Regression` (0.9032)
- Best model by ROC-AUC: `Logistic Regression` (0.9590)

## Interpretation

This evaluation uses the held-out test set for final baseline comparison. The cross-validation stage was used earlier for training-set model comparison, while this report provides the final test-set performance.

For scam detection, recall and F1 are important because missed scam cases may be more harmful than false positives. ROC-AUC is also useful because it summarises ranking performance across possible classification thresholds.

Generated at: 2026-07-02T20:50:06
