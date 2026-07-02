# Model Stability and Overfitting Note

## Purpose

This note is comparing the results of baseline cross-validation, tuned cross-validation, and held-out test evaluation to evaluate and assess model stability and possible overfitting.

## Data Usage

Baseline cross-validation and grid search tuning used the saved training records from `split_indices.json`.

The held-out test records are not used during cross-validation or grid search. It is only used for the final test evaluation.

## Baseline Cross-Validation Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8875 | 0.9097 | 0.8609 | 0.8841 | 0.9478 |
| Decision Tree | 0.8703 | 0.9102 | 0.8219 | 0.8637 | 0.9055 |

## Tuned Cross-Validation Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8938 | 0.9300 | 0.8516 | 0.8885 | 0.9477 |
| Decision Tree | 0.9000 | 0.9655 | 0.8297 | 0.8921 | 0.9402 |

## Held-Out Test Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9063 | 0.9333 | 0.8750 | 0.9032 | 0.9590 |
| Decision Tree | 0.8781 | 0.9231 | 0.8250 | 0.8713 | 0.9002 |

## Stability Assessment

The Logistic Regression (LR) model shows a more stable performance across baseline cross-validation, tuned cross-validation, and held-out test evaluation. The F1 score increased from 0.8841 in baseline cross-validation to 0.8885 after tuning, and then reached 0.9032 using the held-out test set. ROC-AUC remained consistently high, changing from 0.9478 to 0.9477 and then 0.9590 when test set is used.

The Decision Tree (DT) improved after tuning during cross-validation, increasing from 0.8637 to 0.8921 F1. However, its held-out test F1 has a lower score at 0.8713. This means that the tuned Decision Tree are more sensitive using the training folds than Logistic Regression.

## Overfitting Assessment

There is no strong evidence of overfitting for Logistic Regression because its held-out test performance is consistent with, and slightly better than, its cross-validation performance.

For the Decision Tree, there may be mild overfitting or fold sensitivity because tuned cross-validation performance was higher than held-out test performance. This is expected because Decision Trees can be more sensitive to small changes in training data.

## Current Best Model

Logistic Regression currently appears to be the better and more stable model overall. Although the tuned Decision Tree achieved a slightly higher tuned cross-validation F1 score, Logistic Regression did performed better on the held-out test set and have a stronger ROC-AUC.

For scam detection, Logistic Regression is more preferred during this stage because it provides stronger recall, F1, ROC-AUC, and better stability across evaluation stages.