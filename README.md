# 🎓 Student Performance Prediction using Machine Learning

## 📌 Overview
This project focuses on predicting student academic performance using Machine Learning techniques. The dataset includes demographic, socio-economic, and academic features.

---

## 🎯 Objective
To classify students into performance categories (High, Medium, Low) using ML models.

---

## 📊 Dataset Features
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Handled categorical variables using Label Encoding
- Scaled numerical features using StandardScaler

### 2. Feature Engineering
- Created new target variable: `performance`

### 3. Models Used
- Logistic Regression
- Decision Tree
- Random Forest

---

## 📈 Results

| Model                | Performance |
|---------------------|------------|
| Logistic Regression | Good       |
| Decision Tree       | Moderate   |
| Random Forest       | Best       |

---

## 🧠 Key Insights
- Students completing test preparation perform better
- Reading and writing scores are highly correlated
- Socio-economic factors influence performance

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py