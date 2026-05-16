import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from pathlib import Path

_cache = {}


def performance_label(row):
    avg = (row.get('math score', 0) + row.get('reading score', 0) + row.get('writing score', 0)) / 3
    if avg >= 70:
        return "High"
    elif avg >= 50:
        return "Medium"
    else:
        return "Low"


def load_dataset(path: str = 'data/StudentsPerformance.csv') -> pd.DataFrame:
    if path in _cache:
        return _cache[path]
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Dataset not found at {path}")
    df = pd.read_csv(p)
    df.columns = df.columns.str.strip()
    # create performance label if not present
    if 'performance' not in df.columns:
        df['performance'] = df.apply(performance_label, axis=1)
    _cache[path] = df
    return df


def validate_dataframe(df: pd.DataFrame, target: str = 'performance'):
    warnings = []
    if target not in df.columns:
        warnings.append(f"Target column '{target}' not found; attempting to derive it.")
    if df.empty:
        warnings.append('Dataset is empty.')
    if df.isnull().any().any():
        warnings.append('Missing values detected; imputing them in preprocessing.')
    return warnings


def preprocess(df: pd.DataFrame, target: str = 'performance'):
    """Robust preprocessing pipeline.

    Returns: (X_prepared, y_encoded, preprocessor, label_encoder, metadata)
    """
    df = df.copy()
    warnings = validate_dataframe(df, target)

    if target not in df.columns:
        df[target] = df.apply(performance_label, axis=1)

    # separate features
    feature_cols = [c for c in df.columns if c != target]
    X_raw = df[feature_cols]
    y_raw = df[target].astype(str)

    numeric_cols = X_raw.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = [c for c in feature_cols if c not in numeric_cols]

    # preprocessing pipelines
    numeric_pipeline = Pipeline(
        steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False)),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_pipeline, numeric_cols),
            ('cat', categorical_pipeline, categorical_cols),
        ],
        remainder='drop',
    )

    X_prepared = preprocessor.fit_transform(X_raw)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y_raw)

    categorical_values = {c: sorted(df[c].dropna().astype(str).unique().tolist()) for c in categorical_cols}
    metadata = {
        'feature_cols': feature_cols,
        'numeric_cols': numeric_cols,
        'categorical_cols': categorical_cols,
        'categorical_values': categorical_values,
        'warnings': warnings,
    }

    return X_prepared, y_encoded, preprocessor, label_encoder, metadata
