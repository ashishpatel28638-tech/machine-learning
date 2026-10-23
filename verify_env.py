import sys

def verify():
    print(f"Python Version: {sys.version}\n")
    packages = [
        ("NumPy", "numpy"),
        ("Pandas", "pandas"),
        ("SciPy", "scipy"),
        ("Scikit-Learn", "sklearn"),
        ("Matplotlib", "matplotlib"),
        ("Seaborn", "seaborn"),
        ("XGBoost", "xgboost"),
        ("LightGBM", "lightgbm"),
        ("PyTorch", "torch"),
        ("Jupyter/IPython", "IPython"),
        ("tqdm", "tqdm"),
        ("Joblib", "joblib"),
    ]
    
    success = True
    print("Checking installed machine learning packages:")
    print("-" * 50)
    for name, module in packages:
        try:
            mod = __import__(module)
            version = getattr(mod, "__version__", "Available")
            print(f"[OK] {name:<18} -> Version: {version}")
        except ImportError as e:
            print(f"[FAILED] {name:<18} -> Error: {e}")
            success = False
            
    print("-" * 50)
    if success:
        print("\nAll essential machine learning packages are successfully installed and verified!")
    else:
        print("\nSome packages failed to import.")

if __name__ == "__main__":
    verify()
