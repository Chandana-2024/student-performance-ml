import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Evaluation
from sklearn.metrics import classification_report, confusion_matrix

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/StudentsPerformance.csv")

# Clean column names
df.columns = df.columns.str.strip()

# -----------------------------
# CREATE TARGET VARIABLE
# -----------------------------
def performance_label(row):
    avg = (row['math score'] + row['reading score'] + row['writing score']) / 3
    if avg >= 70:
        return "High"
    elif avg >= 50:
        return "Medium"
    else:
        return "Low"

df['performance'] = df.apply(performance_label, axis=1)

# -----------------------------
# ENCODING
# -----------------------------
le = LabelEncoder()

categorical_cols = [
    'gender',
    'race/ethnicity',
    'parental level of education',
    'lunch',
    'test preparation course',
    'performance'
]

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# -----------------------------
# FEATURE SCALING
# -----------------------------
scaler = StandardScaler()

num_cols = ['math score', 'reading score', 'writing score']
df[num_cols] = scaler.fit_transform(df[num_cols])

# -----------------------------
# SPLIT DATA
# -----------------------------
X = df.drop('performance', axis=1)
y = df['performance']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# MODELS
# -----------------------------

# Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# -----------------------------
# EVALUATION
# -----------------------------
print("\n===== Logistic Regression =====")
print(classification_report(y_test, y_pred_lr))

print("\n===== Decision Tree =====")
print(classification_report(y_test, y_pred_dt))

print("\n===== Random Forest =====")
print(classification_report(y_test, y_pred_rf))

# -----------------------------
# CONFUSION MATRIX (RF)
# -----------------------------
cm = confusion_matrix(y_test, y_pred_rf)

sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix - Random Forest")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()