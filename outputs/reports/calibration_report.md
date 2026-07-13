# Calibration Report

## Description

This report summarises probability calibration experiments for the scam conversation classification project.

Only the saved training rows from `split_indices.json` were used. The held-out test set was not used during calibration experiments.

## Calibration Methods

- Sigmoid calibration, also known as Platt scaling
- Isotonic calibration

## Summary Results

| Model | Method | Accuracy | Precision | Recall | F1 | ROC-AUC | Brier Score |
|---|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | isotonic | 0.8922 | 0.9369 | 0.8406 | 0.8858 | 0.9471 | 0.0820 |
| Decision Tree | sigmoid | 0.8883 | 0.9253 | 0.8453 | 0.8832 | 0.9457 | 0.0835 |
| Logistic Regression | sigmoid | 0.8852 | 0.9081 | 0.8578 | 0.8815 | 0.9476 | 0.0836 |
| Decision Tree | isotonic | 0.8914 | 0.9395 | 0.8375 | 0.8850 | 0.9454 | 0.0847 |

## Selected Calibration Setup

The selected calibration setup is **Logistic Regression with isotonic calibration**.

The selection is based mainly on the lowest mean Brier score, because Brier score directly measures the quality of probability estimates.

## Proposed Risk Thresholds

| Risk Band | Probability Minimum | Probability Maximum | Recommended Action |
|---|---:|---:|---|
| Low | 0.00 | 0.26 | Low scam-risk score; no immediate alert, but still keep record for analysis. |
| Medium | 0.26 | 0.54 | Medium scam-risk score; conversation should be reviewed or monitored. |
| High | 0.54 | 1.01 | High scam-risk score; prioritize this conversation for warning or further review. |

## Interpretation

The calibration experiment provides a way to convert model probability outputs into practical risk bands. These thresholds are proposed using training-fold validation results only and should be reviewed again after the final held-out test evaluation.

Generated at: 2026-07-13T13:10:17
