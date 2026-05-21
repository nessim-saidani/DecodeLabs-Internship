# Project 2: Data Classification Using AI

## Overview

This project demonstrates supervised learning by building and training a classification model using the Iris dataset. The model learns patterns from labeled data and makes predictions on unseen data.

**Accuracy Achieved:** 100%

---

## Project Goals

1. Load and understand a dataset
2. Split data into training and testing sets
3. Apply a simple classification algorithm
4. Evaluate model performance
---

## Key Concepts

### Supervised Learning

Supervised learning uses labeled data to train models. Each example has:
- Features (input variables)
- Label (target variable/class)

### Classification

Classification predicts which category (class) a new example belongs to.

### Training vs Testing

- Training Set: Model learns from this data (80%)
- Testing Set: Model's performance is evaluated here (20%)

### Accuracy

Percentage of correct predictions on the testing set.

Formula:
```
Accuracy = (Correct Predictions) / (Total Predictions) * 100
```

---

## Dataset: Iris

The Iris dataset contains 150 flower samples with 4 measurements:

- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

Target: Flower species (3 classes)
- Setosa
- Versicolor
- Virginica

---

## Project Structure

```
DecodeLabs-Internship/
├── classification_model.py      # Main classification script
├── Iris.csv                     # Dataset file
├── PROJECT_2_README.md          # This file
└── requirements.txt             # Python dependencies
```

---

## Installation

### System Requirements

- Python 3.6 or higher
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Install Required Libraries

Option 1: Install individually
```bash
pip install pandas scikit-learn numpy matplotlib
```

Option 2: Use requirements.txt
```bash
pip install -r requirements.txt
```

### Create requirements.txt

If you don't have a requirements.txt file, create one with:
```
pandas>=1.0.0
scikit-learn>=0.24.0
numpy>=1.19.0
matplotlib>=3.3.0
```

Then install:
```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Classification Model

```bash
python classification_model.py
```

### Expected Output

```
==============================================================
PROJECT 2: DATA CLASSIFICATION USING AI
==============================================================

STEP 1: LOADING AND EXPLORING DATA
--------------------------------------------------------------
Dataset shape: (150, 5)
Number of features: 4
Number of samples: 150
Number of classes: 3
Classes: ['setosa' 'versicolor' 'virginica']

STEP 2: SPLITTING DATA INTO TRAINING AND TESTING
--------------------------------------------------------------
Training samples: 120 (80%)
Testing samples: 30 (20%)

STEP 3: TRAINING CLASSIFICATION MODELS
--------------------------------------------------------------
KNeighborsClassifier (k=3): 100.00%
KNeighborsClassifier (k=5): 96.67%
DecisionTreeClassifier: 100.00%
LogisticRegression: 100.00%

STEP 4: DETAILED ANALYSIS OF BEST MODEL
--------------------------------------------------------------
Classification Report:
              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00        10
   virginica       1.00      1.00      1.00        10
    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30

Confusion Matrix:
[[10  0  0]
 [ 0 10  0]
 [ 0  0 10]]
```

---

## Algorithm Used

### K-Nearest Neighbors (KNN)

KNN classifies a point based on the majority class of its k nearest neighbors.

Advantages:
- Simple to understand and implement
- No training phase needed
- Works well with small datasets
- Flexible with non-linear boundaries

Disadvantages:
- Slow prediction for large datasets
- Sensitive to feature scaling
- Sensitive to the choice of k value
- Memory intensive

## Results and Analysis

### Accuracy Achieved

- KNeighborsClassifier (k=3): 100%
- KNeighborsClassifier (k=5): 96.67%

### Confusion Matrix Interpretation

The confusion matrix shows:
```
        Predicted
        Setosa  Versicolor  Virginica
Actual
Setosa    10        0          0
Versicolor 0        10         0
Virginica  0         0         10
```

Diagonal values = Correct predictions
Off-diagonal values = Incorrect predictions

### Classification Report Metrics

- Precision: Of predicted positives, how many were correct
- Recall: Of actual positives, how many were found
- F1-Score: Harmonic mean of precision and recall
- Support: Number of samples in that class

---

## Skills Demonstrated

### Programming Skills
- Data loading and manipulation with Pandas
- Array operations with NumPy
- Data splitting and preprocessing
- Function usage and library integration
- Error handling and debugging

### Machine Learning Skills
- Supervised learning concepts
- Classification techniques
- Training and testing methodology
- Model evaluation and metrics

### Data Science Skills
- Exploratory data analysis
- Data preprocessing
- Feature understanding
- Result interpretation
- Performance metrics analysis

---

## Common Challenges and Solutions

### Challenge 1: Column Name Error

Problem: KeyError when trying to drop column

Solution:
```python
# Check actual column names
print(df.columns.tolist())

# Use dynamic approach
target_column = df.columns[-1]
x = df.drop(target_column, axis=1)
y = df[target_column]
```

### Challenge 2: Low Accuracy

Problem: Model accuracy is below expectations

Solutions:
- Check data quality and for missing values
- Try different algorithms
- Tune hyperparameters
- Use feature scaling
- Collect more training data
- Engineer new features

### Challenge 3: Overfitting

Problem: High training accuracy but low testing accuracy

Solutions:
- Use simpler models
- Increase training data
- Add regularization
- Use cross-validation
- Reduce number of features
- Increase test set size

---

## Interpretation of Results

### What 100% Accuracy Means

- All flowers in the test set were correctly classified
- The model learned the patterns effectively
- The Iris dataset is well-separated and simple for classification

### Important Notes

100% accuracy doesn't guarantee:
- Good performance on completely new data
- Good generalization to other datasets
- Robustness to real-world scenarios
- No overfitting (especially with small test sets)

---

## Limitations

- Only tested on one well-known dataset
- Training and testing sets are relatively small
- Features are predefined, not engineered
- No feature importance analysis initially

---


## File Descriptions

### classification_model.py

Main script that:
- Loads the Iris dataset
- Explores data characteristics
- Splits data into training and testing sets
- Evaluates model performance

### Iris.csv

Dataset containing:
- 150 iris flower samples
- 4 numerical features (measurements)
- 1 target column (species classification)
- No missing values
- Well-balanced classes

### requirements.txt

Lists all Python packages needed:
- pandas: Data manipulation
- scikit-learn: Machine learning
- numpy: Numerical computation
- matplotlib: Data visualization

---


## Learning Outcomes

Upon completing this project, you will understand:

1. How supervised learning works
2. Importance of train-test splitting
3. How classification algorithms make decisions
4. How to evaluate model performance
5. How to interpret evaluation metrics
6. Concept of overfitting and underfitting

---

## Troubleshooting

### Issue: ImportError for pandas, sklearn, etc.

Solution:
```bash
pip install pandas scikit-learn numpy matplotlib
```

### Issue: FileNotFoundError for Iris.csv

Solution:
- Ensure Iris.csv is in the same directory as the script
- Or provide full path to the file:
```python
df = pd.read_csv('/full/path/to/Iris.csv')
```

### Issue: NameError: name 'X' is not defined

Solution:
- Check variable names are consistent
- Python is case-sensitive (X vs x)

---

## Additional Resources

Learning Materials:
- Scikit-learn documentation: https://scikit-learn.org
- Pandas documentation: https://pandas.pydata.org
- Classification algorithms: https://scikit-learn.org/stable/modules/classification.html
- Model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html


---