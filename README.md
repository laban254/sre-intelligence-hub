# Data Science & Machine Learning Learning Hub

A structured, reproducible, and engaging learning path for data science and ML—from foundations to deep learning—with clear goals, exercises, and quality gates.

[![CI Status](https://img.shields.io/badge/CI-pending-yellow)](#)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue)](#)
[![Notebooks Tested](https://img.shields.io/badge/Notebooks-TODO-orange)](#)

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/data-science-and-ml-exercises.git
cd data-science-and-ml-exercises

# Install dependencies
pip install -r requirements.txt

# Run a notebook
jupyter notebook numpy/numpy.ipynb
```

## 📚 Learning Track Map

```
Foundations (Week 1-2)
├── NumPy          → Array operations, broadcasting, linear algebra
├── Pandas         → DataFrames, cleaning, joins, groupby

Visualization (Week 2-3)
├── Matplotlib     → Custom plots, styling, annotations
└── Seaborn        → Statistical plots, faceting, colorblind-safe

Machine Learning (Week 3-5)
├── Scikit-learn   → Preprocessing, pipelines, supervised/unsupervised
└── Model Evaluation → Cross-validation, metrics, grid search

Deep Learning (Week 5-6)
└── Keras          → Neural networks, CNNs, regularization

Capstones (Week 7-8)
└── End-to-end projects with rubrics
```

---

## ⚡ Fast Track (6-8 hours)

Complete the essentials to get started quickly:

| Topic | Notebook | Time | Key Concepts |
|-------|----------|------|-------------|
| NumPy | [`numpy/numpy.ipynb`](numpy/numpy.ipynb) | 1h | Arrays, broadcasting, indexing |
| Pandas | [`pandas/Pandas.ipynb`](pandas/Pandas.ipynb) | 1.5h | DataFrames, cleaning, groupby |
| Matplotlib | [`matplotlib/matplotlib.ipynb`](matplotlib/matplotlib.ipynb) | 1h | Plots, styling, subplots |
| Seaborn | [`seaborn/seaborn.ipynb`](seaborn/seaborn.ipynb) | 1h | Statistical visualizations |
| Scikit-learn | [`scikit-learn/supervised-learning-algorithms/classification.ipynb`](scikit-learn/supervised-learning-algorithms/classification.ipynb) | 1.5h | Classification, metrics |
| Keras | [`keras/Basic_Keras_MNIST_Practice.ipynb`](keras/Basic_Keras_MNIST_Practice.ipynb) | 2h | Neural networks, MNIST |

---

## 🚀 Full Track (20-30 hours)

Complete all topics for a comprehensive education:

### Foundations (8-10 hours)
- [`numpy/numpy.ipynb`](numpy/numpy.ipynb) - Arrays, broadcasting, gotchas
- [`pandas/Pandas.ipynb`](pandas/Pandas.ipynb) - DataFrames, joins, missing data

### Visualization (3-4 hours)
- [`matplotlib/matplotlib.ipynb`](matplotlib/matplotlib.ipynb) - House style, annotations
- [`seaborn/seaborn.ipynb`](seaborn/seaborn.ipynb) - Statistical plots, faceting

### Machine Learning (8-10 hours)
- [`scikit-learn/preprocessing/`](scikit-learn/preprocessing/) - Scaling, encoding, imputation
- [`scikit-learn/supervised-learning-algorithms/`](scikit-learn/supervised-learning-algorithms/) - Classification, regression
- [`scikit-learn/unsupervised-learning-algorithms/`](scikit-learn/unsupervised-learning-algorithms/) - Clustering, dimensionality reduction
- [`scikit-learn/model-evaluation-and-selection/`](scikit-learn/model-evaluation-and-selection/) - Cross-validation, metrics, grid search
- [`scikit-learn/model-pipelines/`](scikit-learn/model-pipelines/) - Pipeline patterns
- [`scikit-learn/ensemble-methods/`](scikit-learn/ensemble-methods/) - Bagging, boosting

### Deep Learning (3-4 hours)
- [`keras/Basic_Keras_MNIST_Practice.ipynb`](keras/Basic_Keras_MNIST_Practice.ipynb) - MLP, CNN, regularization

---

## 📋 Prerequisites

- **Python 3.10+** fundamentals
- Basic statistics and linear algebra
- No prior ML experience required

---

## 🛠️ Installation

### Option 1: Unified Environment (recommended)
```bash
pip install -r requirements.txt
```

### Option 2: Per-topic Installation
Install only what you need:
```bash
pip install -r numpy/requirements.txt    # NumPy track
pip install -r pandas/requirements.txt     # Pandas track
# ... and so on
```

### Cloud Options
- **Google Colab**: Open notebooks directly (Keras notebooks have Colab badges)
- **Kaggle**: Notebooks available for fast-track

---

## ❓ FAQ

**Q: What hardware do I need?**
A: Fast-track runs on CPU (15-30 min). Full track benefits from GPU for Keras notebooks.

**Q: How long does the fast track take?**
A: 6-8 hours of hands-on practice. Plan for 2-3x that time for experimentation.

**Q: How do I run the notebooks?**
A: 
```bash
jupyter notebook <notebook>.ipynb
# or
jupyter lab <notebook>.ipynb
```

**Q: Where do I get the data?**
A: Most notebooks use sklearn's `make_*` functions for synthetic data. Real datasets are loaded from sklearn's built-in datasets.

**Q: Can I contribute?**
A: Yes! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📊 Notebook Structure

Each notebook follows this template:

```markdown
# Title
## Objectives
- What you'll learn
## Dataset
- Source and loading
## Expected Outcome
- What you'll produce
## Challenge
- Stretch goal
```

---

## 📁 Repository Structure

```
data-science-and-ml-exercises/
├── numpy/           # Array operations
├── pandas/          # Data manipulation
├── matplotlib/      # Visualization
├── seaborn/         # Statistical visualization
├── scikit-learn/    # Machine learning
├── keras/           # Deep learning
├── requirements.txt # Unified dependencies
├── README.md        # This file
└── CONTRIBUTING.md  # Contribution guidelines
```

---

## 🧪 Testing & Quality

- **Smoke tests**: Run `jupyter nbconvert --to notebook --execute *.ipynb`
- **Seeds**: Use `random_state=42` for reproducibility
- **Outputs**: Clear stored outputs before committing

---

## 👥 Community

- **GitHub Discussions**: Ask questions, share solutions, suggest features
- **Issues**: Report bugs, request clarity, propose features
- **Contributions**: See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines

**Enable Discussions**: Go to repo Settings → Features → Discussions

---

## 📝 License

Educational use. See individual notebooks for dataset licenses.

---

## 🙏 Acknowledgments

Built with NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, and Keras/TensorFlow.
