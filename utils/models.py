from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier, ExtraTreesClassifier, HistGradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
try:
    from xgboost import XGBClassifier
except Exception:
    XGBClassifier = None
from sklearn.neural_network import MLPClassifier

def get_model_constructors():
    return {
        'Logistic Regression': LogisticRegression,
        'Decision Tree': DecisionTreeClassifier,
        'Random Forest': RandomForestClassifier,
        'K-Nearest Neighbors': KNeighborsClassifier,
        'SVM (RBF)': lambda: SVC(probability=True),
        **({'XGBoost': XGBClassifier} if XGBClassifier is not None else {}),
        'Naive Bayes': GaussianNB,
        'Gradient Boosting': GradientBoostingClassifier,
        'AdaBoost': AdaBoostClassifier,
        'Extra Trees': ExtraTreesClassifier,
        'HistGradientBoosting': HistGradientBoostingClassifier,
        'MLP (Neural Net)': MLPClassifier,
    }

def train_all(X_train, y_train):
    models = {}
    for name, ctor in get_model_constructors().items():
        model = ctor()
        model.fit(X_train, y_train)
        models[name] = model
    return models
