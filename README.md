# Machine Learning Workspace

This repository contains machine learning projects, notebook lessons, and environment configuration for machine learning development.

## 🛠️ Environment Setup

### 1. Prerequisites
- Python 3.13 (recommended for maximum library compatibility) or 3.14

### 2. Virtual Environment Setup
To set up a local virtual environment:

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Verify Environment
Run the verification script to verify that all machine learning and deep learning packages are loaded properly:

```powershell
python verify_env.py
```

## 📦 Installed Libraries

- **Data Processing & Scientific Computing:** `numpy`, `pandas`, `scipy`
- **Visualization:** `matplotlib`, `seaborn`
- **Classical Machine Learning:** `scikit-learn`, `xgboost`, `lightgbm`
- **Deep Learning:** `torch`
- **Interactive Workflows:** `jupyter`, `ipykernel`, `notebook`
- **Utilities:** `tqdm`, `joblib`, `openpyxl`, `requests`

## 🚀 Getting Started

Launch Jupyter Notebook or Jupyter Lab:
```powershell
jupyter notebook
```
Open `class_1.ipynb` to begin.
