# Sports Match Outcome Prediction

Final project for the course **Data Analysis with Python**.

This project aims to predict the outcome of football matches using historical data from the **European Soccer Database**. The problem is formulated as a **multi-class classification task**, where the target variable is the **match outcome**: **Home Win**, **Draw**, or **Away Win**.

---

## 1. Project Overview

Football match outcome prediction is a meaningful real-world data analysis problem because match results are influenced by many factors such as team strength, recent performance, league differences, and home advantage. In this project, we use historical European football match data to build machine learning models that can classify match outcomes.

The project follows a standard data analysis and machine learning workflow:

1. Understand the problem and the dataset
2. Clean the data
3. Perform exploratory data analysis (EDA)
4. Preprocess and engineer features
5. Build machine learning models
6. Evaluate and compare model performance
7. Draw conclusions and discuss limitations

---

## 2. Problem Definition

### Task type
**Classification**

### Target variable
**Match outcome**

The target variable is defined from the final score of each match:

- `HomeWin` if `home_team_goal > away_team_goal`
- `Draw` if `home_team_goal == away_team_goal`
- `AwayWin` if `home_team_goal < away_team_goal`

### Why this problem matters
Predicting match outcomes can support:
- sports analytics
- team performance analysis
- match preview systems
- football data-driven decision making

---

## 3. Dataset

### Dataset source
- **Name:** European Soccer Database
- **Platform:** Kaggle
- **Link:** https://www.kaggle.com/datasets/hugomathien/soccer

### Dataset description
The dataset contains historical football data from multiple European leagues and includes information about:
- matches
- teams
- leagues
- countries
- team attributes
- player attributes

In this project, the **Match** table is used as the main source, and additional information can be joined from tables such as:
- `League`
- `Country`
- `Team`
- `Team_Attributes`

### Main analysis unit
Each row in the final modeling dataset represents **one football match**.

---

## 4. Project Objectives

After completing this project, the group should be able to:

- understand and describe a real-world classification problem
- clean and preprocess a structured sports dataset
- perform exploratory data analysis and generate useful insights
- build at least two machine learning models
- compare model performance using appropriate evaluation metrics
- interpret results and explain practical implications

---

## 5. Project Workflow

## Step 1. Understand the problem and the dataset
In this step, we:
- study the structure of the SQLite database
- identify the main tables and relevant columns
- define the target variable
- identify candidate input features
- report the number of rows, columns, and data types

## Step 2. Data cleaning
In this step, we:
- check for missing values
- remove duplicate rows if necessary
- detect abnormal or inconsistent values
- convert data types (for example, date columns to datetime)
- remove unnecessary columns
- document every cleaning decision and explain why it was made

## Step 3. Exploratory Data Analysis (EDA)
In this step, we:
- compute descriptive statistics
- visualize the distribution of match outcomes
- analyze home vs away goal patterns
- explore relationships between key variables
- investigate how input features relate to the target
- summarize at least five meaningful insights

## Step 4. Data preprocessing
In this step, we:
- select the most relevant features
- handle categorical variables
- create train/test splits
- scale or transform features when needed
- engineer additional features such as recent team form or strength differences

## Step 5. Modeling
We build at least **two classification models**:

- **Decision Tree** as a simple and interpretable baseline model
- **Random Forest** as a stronger ensemble model

Optional additional models:
- Logistic Regression
- XGBoost
- Support Vector Machine
- K-Nearest Neighbors

## Step 6. Model evaluation
We evaluate model performance using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

We also answer:
- Which model performs better?
- Why is that model more suitable?
- Is there any sign of overfitting or underfitting?
- Which variables are the most important?

## Step 7. Conclusion
Finally, we summarize:
- key insights from the data
- the best-performing model
- practical implications
- limitations of the project
- possible future improvements

---

## 6. Feature Engineering

To improve model quality, we may create additional pre-match features such as:

- recent win rate of the home team
- recent win rate of the away team
- average goals scored in the last 5 matches
- average goals conceded in the last 5 matches
- team strength indicators from team attributes
- strength difference between home and away teams
- historical head-to-head statistics
- league and season information

### Important note
To avoid **data leakage**, the final score variables used to define the target must **not** be used as input features for prediction.

---

## 7. Models Used

### 1. Decision Tree
Decision Tree is used as the baseline model because it is:
- easy to train
- easy to interpret
- useful for understanding how features influence match outcomes

### 2. Random Forest
Random Forest is used as the main model because it:
- usually performs better than a single decision tree
- reduces overfitting
- provides feature importance scores

### 3. Optional benchmark models
Additional models may be tested for comparison, such as Logistic Regression or XGBoost.

---

## 8. Evaluation Metrics

Because this is a multi-class classification problem, we use:

- **Accuracy**: overall correctness
- **Precision**: how precise the predictions are for each class
- **Recall**: how well the model captures each class
- **F1-score**: balance between precision and recall
- **Confusion Matrix**: detailed prediction errors across classes

When class imbalance exists, **macro-averaged metrics** are especially useful.

---

## 9. Project Structure

```text
sports-match-outcome-prediction/
|
|-- data/
|   |-- database.sqlite
|   |-- processed/
|   `-- final/
|
|-- notebooks/
|   |-- 01_data_understanding.ipynb
|   |-- 02_data_cleaning_eda.ipynb
|   |-- 03_feature_engineering_modeling.ipynb
|   `-- final_project_notebook.ipynb
|
|-- reports/
|   |-- figures/
|   `-- final_report.pdf
|
|-- slides/
|   `-- final_presentation.pptx
|
|-- src/
|   |-- data_loader.py
|   |-- preprocessing.py
|   |-- feature_engineering.py
|   |-- train.py
|   `-- evaluate.py
|
|-- requirements.txt
|-- README.md
`-- .gitignore
```
