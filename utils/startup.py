import importlib
from pathlib import Path
from typing import List, Tuple

REQUIRED = [
    'streamlit', 'pandas', 'numpy', 'sklearn', 'matplotlib', 'seaborn', 'plotly',
    'xgboost', 'shap', 'joblib', 'scipy', 'streamlit_option_menu', 'streamlit_lottie', 'PIL', 'requests'
]

DATA_PATHS = [
    Path('data/StudentsPerformance.csv'),
    Path('DATA/StudentsPerformance.csv'),
    Path('exam/StudentsPerformance.csv'),
]


def check_packages() -> Tuple[List[str], List[str]]:
    missing = []
    present = []
    for pkg in REQUIRED:
        try:
            importlib.import_module(pkg)
            present.append(pkg)
        except Exception:
            missing.append(pkg)
    return missing, present


def find_dataset() -> Path:
    for p in DATA_PATHS:
        if p.exists():
            return p
    return None


def ensure_models_dir() -> Path:
    md = Path(__file__).resolve().parent.parent / 'models'
    md.mkdir(parents=True, exist_ok=True)
    return md


def get_install_command() -> str:
    return 'python -m pip install -r requirements.txt'


def verify_startup():
    missing, present = check_packages()
    dataset = find_dataset()
    models_dir = ensure_models_dir()
    return {
        'missing_packages': missing,
        'present_packages': present,
        'dataset_path': str(dataset) if dataset is not None else None,
        'models_dir': str(models_dir),
        'install_cmd': get_install_command(),
    }
