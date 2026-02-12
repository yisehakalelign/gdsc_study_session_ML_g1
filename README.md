# gdsc_study_session
# 🚖 Ride Price Estimation System (Machine Learning Project)

## 📌 Project Overview

This project builds a machine learning system that estimates the price of a ride based on trip and contextual features such as distance, duration, traffic level, weather, and demand.

The goal of this project is not only to build models, but to demonstrate understanding of:

- Problem framing
- Dataset design
- Data cleaning and preprocessing
- Regression and classification modeling
- Model evaluation and reflection

This project was completed as an individual mini-project for Semester One.

---

## 🎯 Problem Statement

The objective is to predict the **ride price** using machine learning.

The system also classifies rides into:

- High-cost rides
- Low-cost rides

This is solved using:

- Linear Regression (for price prediction)
- Logistic Regression (for classification)

---

## 🧠 Why Machine Learning?

Ride pricing depends on multiple interacting factors:

- Distance
- Trip duration
- Traffic
- Weather
- Demand

Instead of using fixed rules, machine learning can automatically learn patterns from data and make better predictions.

---

## 📊 Dataset Description

The dataset was synthetically generated and contains:

- 200 rows (minimum required was 150)
- 6 input features
- 1 continuous target variable (`ride_price`)
- Both numerical and categorical variables

### Features Used

| Feature | Type | Justification |
|----------|--------|---------------|
| distance_km | Numerical | Longer distance increases fuel cost and time |
| duration_min | Numerical | Longer trips increase operational cost |
| time_of_day | Categorical | Night rides may have different pricing |
| traffic_level | Categorical | Heavy traffic increases time and fuel |
| weather | Categorical | Rain may increase ride cost |
| demand_level | Categorical | High demand increases price |
| ride_price | Continuous Target | The value we want to predict |

### Feature Not Included

Driver rating was considered but excluded because:
- It may introduce bias
- It is less directly related to price estimation

---

## 🔎 Data Cleaning & Preparation

The following preprocessing steps were performed:

- Checked for missing values
- Encoded categorical variables using one-hot encoding
- Scaled numerical features using StandardScaler
- Split dataset into training and testing sets

Poor data quality could negatively affect model accuracy by:
- Creating biased predictions
- Causing unstable models
- Increasing prediction error

---

## 📈 Models Used

### 1️⃣ Linear Regression (Price Prediction)

- Predicts continuous ride price
- Evaluated using:
  - Mean Absolute Error (MAE)
  - R² Score
- Visualized using predicted vs actual plot

---

### 2️⃣ Logistic Regression (High-Cost Classification)

- Binary target created using median price
- Evaluated using:
  - Accuracy
  - Confusion Matrix

Classification works by estimating probabilities.
If probability > 0.5 → High Cost  
If probability ≤ 0.5 → Low Cost  

---

## 📊 Model Comparison

- Regression predicts exact price.
- Classification predicts cost category.
- Distance was found to be the most influential feature.
- Data quality strongly influenced both models.

---

## ⚖ Ethical & Practical Reflection

### Potential Unfair Pricing Behavior
High demand areas could consistently result in higher prices, potentially affecting certain communities unfairly.

### Real-World Risk
During emergencies (e.g., heavy rain), the model may increase prices excessively.

### Dataset Limitation
The dataset is synthetic and may not perfectly reflect real-world ride behavior.

---

## ▶ How to Run the Project (Google Colab)

1. Open Google Colab.
2. Upload the notebook: `ride_price_model.ipynb`
3. Run cells in order.
4. The dataset will be generated automatically.
5. Models will train and evaluation results will display.

No external datasets are required.

---

## 📂 Repository Structure

