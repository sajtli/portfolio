# Intrusion Detection on Imbalanced Data using Random Forest

This project explores machine learning techniques for detecting network intrusions using the KDDCUP99 dataset. The focus is on addressing **class imbalance**, **sampling strategies**, and **hyperparameter optimization** to improve model performance.

## Objective

To build a robust classifier that can accurately detect minority (attack) classes in highly imbalanced network traffic data using Random Forest and various resampling techniques.

## Dataset

- **Source**: KDDCUP99 10% subset
- **Classes**: Normal vs. various attack types
- **Issue**: Highly imbalanced distribution of classes

## Tools & Libraries

- Python 3.10+
- `scikit-learn`
- `imbalanced-learn`
- `pandas`, `numpy`
- `matplotlib`, `seaborn`

## Methodology

1. **Data Preprocessing**
   - Removal of duplicates
   - Label consolidation (Normal vs. Attack)
   - Feature scaling using `StandardScaler`
   - Feature selection using Random Forest feature importances
   - Redundancy filtering based on correlation matrix

2. **Modeling & Evaluation**
   - Classifier: `RandomForestClassifier`
   - Sampling Scenarios:
     - No sampling
     - Random over-sampling
     - SMOTE
   - Evaluation Metrics:
     - Precision, F1-Score
     - True Positive Rate (TPR)
     - False Positive Rate (FPR)
   - Cross-validation:
     - 5-fold Stratified CV
   - Optimization:
     - `RandomizedSearchCV` for hyperparameter tuning

## Results Summary

**Performance metrics without parameter optimization**

| Sampling strategy    | CV F1-score | Train F1-score | Test F1-score  | Train Precision | Test Precision | Train TPR | Test TPR | Train FPR | Test FPR |
| ---------------------| ----------- | -------------- | -------------- | --------------- | -------------- | --------- | -------- | --------- | -------- |
| No sampling          | 0.9988      | 1.0            | 0.9991         | 100 %           | 99.98 %        | 99.99 %   | 99.84 %  | 0.0 %     | 0.01 %   |
| Random over-sampling | 0.9993      | 1.0            | 0.9991         | 100 %           | 99.97 %        | 100 %     | 99.86 %  | 0.0 %     | 0.02 %   |
| SMOTE                | 0.9991      | 1.0            | 0.9990         | 100 %           | 99.96 %        | 100 %     | 99.85 %  | 0.0 %     | 0.03 %   |


**Performance metrics with parameter optimization**

| Sampling strategy    | CV F1-score | Train F1-score | Test F1-score  | Train Precision | Test Precision | Train TPR | Test TPR | Train FPR | Test FPR |
| ---------------------| ----------- | -------------- | -------------- | --------------- | -------------- | --------- | -------- | --------- | -------- |
| No sampling          | 0.9991      | 0.9999         | 0.9990         | 99.99 %         | 99.97 %        | 99.99 %   | 99.84 %  | 0.01 %    | 0.02 %   |
| Random over-sampling | 0.9993      | 0.9999         | 0.9991         | 99.99 %         | 99.96 %        | 99.99 %   | 99.87 %  | 0.01 %    | 0.03 %   |
| SMOTE                | 0.9991      | 0.9999         | 0.9991         | 99.99 %         | 99.97 %        | 99.99 %   | 99.86 %  | 0.01 %    | 0.02 %   |

Even with feature selection and dimensionality reduction, model performance remained high. Optimized parameters provided only marginal improvement over defaults, due to the dataset's clear class separation.

## Key Insights

- Random Forest handles the KDD dataset extremely well, even with default parameters.
- Sampling techniques slightly improve recall but risk overfitting on training data.
- Feature filtering and SMOTE yield realistic but only slightly different performance.
- Precision, recall, and F1-score should all be considered in imbalanced classification.

## Limitations

- KDDCUP99 is an outdated and highly separable dataset.
- High scores may not reflect real-world challenges.
- Results need validation on more complex intrusion detection datasets.

## Future Work

- Apply the same pipeline to modern, harder-to-predict datasets (e.g., NSL-KDD, UNSW-NB15)
- Use advanced models (e.g., XGBoost, ensemble methods)
- Incorporate real-time data and anomaly detection

---

Feel free to fork or star this repo if you find it useful!
