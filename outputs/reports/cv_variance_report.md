# Cross-Validation Variance Report

## Description

This report summarises grid search cross-validation results for the baseline models.

Only the saved training rows were used. The held-out test set was not used during grid search.

The main selection metric was F1 score.

## Selected Model Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8938 (+/- 0.0223) | 0.9300 (+/- 0.0107) | 0.8516 (+/- 0.0434) | 0.8885 (+/- 0.0256) | 0.9477 (+/- 0.0147) |
| Decision Tree | 0.9000 (+/- 0.0149) | 0.9655 (+/- 0.0061) | 0.8297 (+/- 0.0314) | 0.8921 (+/- 0.0178) | 0.9402 (+/- 0.0145) |

## Selected Hyperparameters

### Logistic Regression

```json
{
    "model__C": 0.1,
    "model__class_weight": null,
    "model__l1_ratio": 1.0
}
```

### Decision Tree

```json
{
    "class_weight": null,
    "criterion": "entropy",
    "max_depth": 5,
    "min_samples_leaf": 1,
    "min_samples_split": 2
}
```

## Interpretation

Lower standard deviation indicates more stable cross-validation performance across folds.
The selected hyperparameters should be compared with earlier baseline results before deciding whether tuning provides meaningful improvement.

Generated at: 2026-07-02T22:58:22