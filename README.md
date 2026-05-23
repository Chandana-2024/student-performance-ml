<img width="1907" height="962" alt="st4" src="https://github.com/user-attachments/assets/363b24d2-9690-4d8e-99ab-9b66cd9aedfb" />
<img width="1542" height="652" alt="st2" src="https://github.com/user-attachments/assets/7503d232-65ca-4b08-a9a5-9c95c410b6a9" />
<img width="1552" height="776" alt="s3" src="https://github.com/user-attachments/assets/13a5c06c-47b4-4bb5-8952-b911eb418c25" />
# StudentPerformance_ML — Setup & Run

Quick instructions to prepare and run the Streamlit app locally.

1) Create a Python venv (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell
# or .venv\Scripts\activate for cmd
```

2) Upgrade pip and install dependencies:

```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

3) Run the app:

```powershell
streamlit run app.py
```

If installation fails for heavy packages (xgboost, shap) consider installing pre-built wheels or using conda.
Student Performance Streamlit App
=================================

Quick steps to run (Windows):

1. Open PowerShell as Administrator.
2. Allow the script to run for this session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

3. Run the helper script (installs Python if missing, creates venv, installs deps, launches app):

```powershell
cd path\to\landt\StudentPerformance_ML
.\setup_and_run.ps1
```

If you prefer manual steps:

```powershell
# Install Python from https://www.python.org/downloads/windows/ (Add to PATH)
py -m pip install -r requirements.txt
py -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

App URL: http://localhost:8501# 🎓 Student Performance Prediction using Machine Learning

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
