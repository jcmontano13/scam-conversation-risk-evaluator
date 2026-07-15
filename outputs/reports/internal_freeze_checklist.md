# Internal Freeze Checklist

## Project Status Summary

The project has completed the main technical pipeline from feature extraction to model evaluation. Weeks 1 to 5 are complete, and Week 6 deliverables for final test evaluation, ablation, and interpretability artifacts have also been completed. The project is now ready for final report preparation and repository packaging.

## Completed Deliverables

| Week | Deliverable | Status |
|---|---|---|
| Week 1 | Parsed turns, thread-level features, metadata, split indices | Complete |
| Week 2 | Feature dictionary, unit test log, updated feature file | Complete |
| Week 3 | Baseline model pipelines and initial CV outputs | Complete |
| Week 4 | Grid search, selected hyperparameters, CV variance report | Complete |
| Week 5 | Calibration report and proposed risk thresholds | Complete |
| Week 6 | Test results, ablation results, interpretability artifacts | Complete |

## Scripts and Run Commands

| Script | Purpose | Run Command |
|---|---|---|
| parse_and_features.py | Extract parsed turns and thread-level features | python src/feature_engineering/parse_and_features.py |
| check_features.py | Validate feature outputs | python src/validation/check_features.py |
| create_split_indices.py | Create fixed train/test split | python src/preprocessing/create_split_indices.py |
| train_baseline_models.py | Run baseline CV | python src/models/train_baseline_models.py |
| tune_baseline_models.py | Run grid search | python src/models/tune_baseline_models.py |
| calibration_experiments.py | Run calibration experiments | python src/evaluation/calibration_experiments.py |
| ablation_test.py | Run leave-one-feature-out ablation | python src/evaluation/ablation_test.py |
| interpretability_artifacts.py | Generate interpretability outputs | python src/evaluation/interpretability_artifacts.py |

## Output Evidence Files

| Evidence File | Status |
|---|---|
| scam_dialogue_parsed.csv | Complete |
| scam_dialogue_thread_features.csv | Complete |
| feature_extraction_metadata.json | Complete |
| split_indices.json | Complete |
| feature_validation_report.txt | Complete |
| unit_test_log.txt | Complete |
| cv_results.csv | Complete |
| selected_hyperparams.json | Complete |
| cv_variance_report.md | Complete |
| calibration_report.md | Complete |
| proposed_risk_thresholds.csv | Complete |
| test_results.csv | Complete |
| ablation_results.csv | Complete |
| coefficients_table.csv | Complete |
| tree_feature_importance.csv | Complete |
| decision_tree_rules.txt | Complete |
| interpretability_report.md | Complete |

## Validation and Reproducibility Checks

The project uses a fixed random seed of 42. The train/test split is saved in split_indices.json to support reproducibility. Cross-validation, tuning, calibration, ablation, and interpretability steps used the saved training rows where appropriate. The held-out test set was reserved for final evaluation and was not used for calibration, ablation, or feature importance decisions.

## Remaining Risks or Cleanup Items

The main remaining task is final report writing and repository packaging. Some results need to be summarized clearly in the final report, especially calibration, ablation, and interpretability findings. The README should also be checked to make sure all final run commands and outputs are listed.

## Freeze Decision

The technical pipeline is ready for internal freeze. The project can now move to final report preparation and submission packaging.