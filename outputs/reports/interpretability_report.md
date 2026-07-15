# Interpretability Report

## Description

This report summarises simple interpretability artifacts for the Logistic Regression and Decision Tree models.

Only the saved training rows from `split_indices.json` were used. The held-out test set was not used to create these interpretability artifacts.

## Logistic Regression Coefficients

The Logistic Regression coefficients show how each standardized structural feature affects the predicted scam probability.

| Feature | Coefficient | Absolute Coefficient | Direction |
|---|---:|---:|---|
| turn_count | 2.147104 | 2.147104 | Increases predicted scam probability |
| aggregate_money_terms | 1.538966 | 1.538966 | Increases predicted scam probability |
| ratio_request_messages | 0.758210 | 0.758210 | Increases predicted scam probability |
| aggregate_num_urls | 0.082927 | 0.082927 | Increases predicted scam probability |

## Decision Tree Feature Importance

The Decision Tree feature importance values show which features contributed most to the tree splits.

| Feature | Importance |
|---|---:|
| turn_count | 0.665614 |
| aggregate_money_terms | 0.224456 |
| ratio_request_messages | 0.104989 |
| aggregate_num_urls | 0.004941 |

## Main Interpretation

For Logistic Regression, the strongest feature by absolute coefficient is `turn_count`. Its direction is: increases predicted scam probability.

For the Decision Tree, the most important feature is `turn_count` based on feature importance.

These outputs support the use of compact structural features because the model decisions can be explained using feature coefficients, feature importance values, and readable tree rules.

The Decision Tree rules are saved separately in `decision_tree_rules.txt`.

Generated at: 2026-07-15T19:45:32
