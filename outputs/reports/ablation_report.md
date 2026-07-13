# Ablation Report

## Description

This report summarises the leave-one-feature-out ablation test for the scam conversation classification project.

Only the saved training rows from `split_indices.json` were used. The held-out test set was not used for feature importance decisions.

## Feature Set

The full feature set contains:

- `turn_count`
- `aggregate_num_urls`
- `aggregate_money_terms`
- `ratio_request_messages`

## Summary Results

| Model | Feature Set | Removed Feature | Accuracy | Precision | Recall | F1 | ROC-AUC | F1 Drop |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Decision Tree | full_feature_set | None | 0.9000 | 0.9655 | 0.8297 | 0.8921 | 0.9402 | 0.0000 |
| Decision Tree | without_aggregate_money_terms | aggregate_money_terms | 0.8453 | 0.9065 | 0.7719 | 0.8321 | 0.9150 | 0.0600 |
| Decision Tree | without_aggregate_num_urls | aggregate_num_urls | 0.9008 | 0.9673 | 0.8297 | 0.8929 | 0.9407 | -0.0008 |
| Decision Tree | without_ratio_request_messages | ratio_request_messages | 0.8828 | 0.9247 | 0.8359 | 0.8766 | 0.9200 | 0.0155 |
| Decision Tree | without_turn_count | turn_count | 0.7828 | 0.8589 | 0.6828 | 0.7564 | 0.8661 | 0.1357 |
| Logistic Regression | full_feature_set | None | 0.8938 | 0.9300 | 0.8516 | 0.8885 | 0.9477 | 0.0000 |
| Logistic Regression | without_aggregate_money_terms | aggregate_money_terms | 0.8547 | 0.8856 | 0.8156 | 0.8486 | 0.9234 | 0.0399 |
| Logistic Regression | without_aggregate_num_urls | aggregate_num_urls | 0.8938 | 0.9300 | 0.8516 | 0.8885 | 0.9477 | 0.0000 |
| Logistic Regression | without_ratio_request_messages | ratio_request_messages | 0.8859 | 0.9394 | 0.8250 | 0.8777 | 0.9356 | 0.0108 |
| Logistic Regression | without_turn_count | turn_count | 0.7867 | 0.8400 | 0.7078 | 0.7677 | 0.8598 | 0.1208 |

## Interpretation

For **Decision Tree**, removing `turn_count` caused the largest F1 drop of 0.1357.
For **Logistic Regression**, removing `turn_count` caused the largest F1 drop of 0.1208.

A positive drop means that model performance became worse after the feature was removed. A small or negative drop means the model did not depend strongly on that feature during cross-validation.

These results should be used together with model coefficients, decision tree rules, and final test results before making final conclusions.

Generated at: 2026-07-13T15:36:59
