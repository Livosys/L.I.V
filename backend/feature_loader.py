import importlib
import os

BASE_DIR = os.path.dirname(__file__)

def load_features(app):
    for name in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, name)
        if not os.path.isdir(path):
            continue
        if name.startswith("_"):
            continue
        if not os.path.exists(os.path.join(path, "core.py")):
            continue

        try:
            module = importlib.import_module(f"{name}.core")
            setup = getattr(module, "setup", None)
            if callable(setup):
                setup(app)
        except Exception as e:
            raise RuntimeError(f"Feature load failed: {name}: {e}")
