# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Project Overview
Data Science & ML Learning Hub - A collection of Jupyter notebooks for learning data science and machine learning topics (NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Keras).

## Commands

### Run a Notebook
```bash
jupyter notebook numpy/numpy.ipynb
# or
jupyter lab <notebook>.ipynb
```

### Test Notebooks (Smoke Tests)
```bash
jupyter nbconvert --to notebook --execute *.ipynb
```

### Clear Notebook Outputs
```bash
jupyter nbconvert --clear-output --inplace notebook.ipynb
```

### Data Fetching
```bash
python fetch_data.py --quick          # Fast mode (small samples)
python fetch_data.py --full            # Full mode (complete datasets)
python fetch_data.py --verify          # Verify existing data hashes
python fetch_data.py --status          # Show data status
# Or set environment variable:
export DATA_MODE=quick
python fetch_data.py --status
```

### Notebook Mode Toggle
```bash
python notebook_toggle.py --show       # Show current mode and settings
python notebook_toggle.py --mode quick # Set quick mode
python notebook_toggle.py --mode full  # Set full mode
```

## Key Conventions

- **Seeds**: Always use `random_state=42` or `np.random.seed(42)` for reproducibility
- **Notebook naming**: lowercase with hyphens (e.g., `numpy.ipynb`, `classification-exercise.ipynb`)
- **Each topic directory** (numpy/, pandas/, etc.) has its own `requirements.txt`
- **Output files** (like `output.csv`) are gitignored per directory - check each topic's `.gitignore`
- **Clear outputs** before committing notebooks (cleaner diffs, smaller files)
- **Quick/Full mode**: Use `DATA_MODE` env var, `--quick/--full` flags, or `notebook_toggle.py`

## Quick/Full Mode System
- **Quick Mode**: n_samples=100, n_iter=10, n_folds=2, n_jobs=1
- **Full Mode**: n_samples=1000, n_iter=100, n_folds=5, n_jobs=-1
- Controlled via `NOTEBOOK_MODE` environment variable or `notebook_toggle.py`

## Project Structure
- Topic directories contain notebooks, README.md, requirements.txt, and .gitignore
- numpy/ has a GOTCHAS.md documenting NumPy-specific pitfalls
- `fetch_data.py` provides centralized data fetching with hash verification
- `notebook_toggle.py` provides quick/full mode toggle for notebooks
- See CONTRIBUTING.md for full notebook template and coding standards
