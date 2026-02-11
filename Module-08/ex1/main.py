import importlib
print("\nOPERATOR STATUS: Loading programs...")
print("\nChecking dependencies:")

try:
    pnd = importlib.import_module('pandas')
    print(f"[OK] {pnd.__name__} ({pnd.__version__}) - Data manipulation ready")
except ModuleNotFoundError as e:
    pnd = None
    print("[ERROR]", e)

try:
    req = importlib.import_module('requests')
    print(f"[OK] {req.__name__} ({req.__version__}) - Network access ready")
except ModuleNotFoundError as e:
    req = None
    print("[ERROR]", e)

try:
    mplt = importlib.import_module('matplotlib')
    print(f"[OK] {mplt.__name__} ({mplt.__version__}) - Visualization ready")
except ModuleNotFoundError as e:
    mplt = None
    print("[ERROR]", e)


