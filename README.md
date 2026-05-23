# 🎓 Student Performance Prediction using Machine Learning

A Machine Learning-powered Streamlit web application that predicts student academic performance based on demographic, socio-economic, and educational factors.

---

## 📸 Project Preview

<img width="1907" height="962" alt="st4" src="https://github.com/user-attachments/assets/363b24d2-9690-4d8e-99ab-9b66cd9aedfb" />

<img width="1542" height="652" alt="st2" src="https://github.com/user-attachments/assets/7503d232-65ca-4b08-a9a5-9c95c410b6a9" />

<img width="1552" height="776" alt="s3" src="https://github.com/user-attachments/assets/13a5c06c-47b4-4bb5-8952-b911eb418c25" />

---

## 📌 Overview

This project analyzes student-related data and predicts performance using different Machine Learning algorithms.

It helps understand how factors like parental education, lunch type, and test preparation influence academic success.

---

## 🚀 Features

- 📊 Student Performance Prediction
- 🧠 Multiple ML Models
- 🌐 Interactive Streamlit Web App
- 📈 Data Visualization & Analysis
- ⚡ Fast and Responsive UI
- 🗂️ Organized Project Structure

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```bash
StudentPerformance_ML/
│
├── .streamlit/
├── .venv/
├── assets/
├── components/
├── DATA/
├── models/
├── notebook/
├── pages/
├── styles/
├── utils/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── setup_and_run.ps1
├── setup.bat
└── setup.sh
```

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

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Preprocessing

- Handled missing values
- Encoded categorical variables
- Scaled numerical features

### 2️⃣ Feature Engineering

- Created target performance categories
- Selected important features

### 3️⃣ Models Used

- Logistic Regression
- Decision Tree
- Random Forest

---

## 📈 Results

| Model | Performance |
|------|-------------|
| Logistic Regression | Good |
| Decision Tree | Moderate |
| Random Forest | Best |

---

## 🧠 Key Insights

- Students completing test preparation courses perform better.
- Reading and writing scores are highly correlated.
- Socio-economic conditions influence academic performance.

---

## 🚀 Installation & Setup

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/StudentPerformance_ML.git
```

### Move to Project Folder

```bash
cd StudentPerformance_ML
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows (PowerShell)

```bash
.\.venv\Scripts\Activate.ps1
```

#### Windows (CMD)

```bash
.venv\Scripts\activate
```

---

## 📦 Install Dependencies

```bash
python -m pip install --upgrade pip setuptools wheel
```

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

App will run at:

```bash
http://localhost:8501
```

---

## ⚡ Quick Setup (Windows)

Open PowerShell as Administrator and run:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```bash
cd path\to\StudentPerformance_ML
```

```bash
.\setup_and_run.ps1
```

---

## ❗ Troubleshooting

If installation fails for heavy packages like:

- xgboost
- shap

Try:
- Installing pre-built wheels
- Using Conda environment

---

## 🎯 Future Improvements

- Add Deep Learning models
- Deploy on Streamlit Cloud
- Add Authentication
- Improve UI/UX
- Add Real-time Analytics

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Sree Chandana**

GitHub: https://github.com/Chandana_2024

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
