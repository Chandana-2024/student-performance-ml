import os
from pathlib import Path
from joblib import dump, load


MODELS_DIR = Path(__file__).resolve().parent.parent / 'models'
MODELS_DIR.mkdir(parents=True, exist_ok=True)


def _model_path(name: str) -> Path:
    safe = name.replace(' ', '_').replace('/', '_')
    return MODELS_DIR / f"{safe}.joblib"


def save_model(name: str, model) -> Path:
    path = _model_path(name)
    dump(model, path)
    return path


def load_model(name: str):
    path = _model_path(name)
    if not path.exists():
        raise FileNotFoundError(path)
    return load(path)


def list_models():
    return [p.stem for p in MODELS_DIR.glob('*.joblib')]
