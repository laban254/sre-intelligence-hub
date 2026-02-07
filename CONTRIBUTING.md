# Contributing to DS/ML Learning Hub

Thank you for your interest in contributing! This guide outlines conventions and workflows for this repository.

## Table of Contents

- [Notebook Naming Conventions](#notebook-naming-conventions)
- [Notebook Template](#notebook-template)
- [Coding Standards](#coding-standards)
- [Reproducibility](#reproducibility)
- [Output Policy](#output-policy)
- [Submitting Changes](#submitting-changes)

---

## Notebook Naming Conventions

| Pattern | Example | Purpose |
|---------|---------|---------|
| `{topic}.ipynb` | `numpy.ipynb` | Main topic notebook |
| `{topic}-exercise.ipynb` | `classification-exercise.ipynb` | Exercise for learner |
| `{topic}-solution.ipynb` | `classification-solution.ipynb` | Solution to exercise |

**Rules:**
- Use lowercase with hyphens
- No spaces in filenames
- Group related notebooks in subdirectories

---

## Notebook Template

Each notebook should follow this structure:

```markdown
# Topic Title

## Objectives
- Learning objective 1
- Learning objective 2
- Learning objective 3

## Dataset
- Source: [where data comes from]
- Size: [approximate size]
- How to load: [code snippet]

## Expected Outcome
- What you'll produce (plot, model, metric)
- Expected runtime (CPU/GPU)

## Challenge (Optional)
- Stretch goal for advanced learners

---

## Code Section

```python
# imports
import numpy as np
import pandas as pd
```

---

## Notes

- Include markdown explanations between code cells
- Add comments in code for complex logic
- Reference common pitfalls in callout boxes
```

---

## Coding Standards

### Imports
```python
# Standard library imports first
import os
import sys

# Third-party imports
import numpy as np
import pandas as pd

# Local imports (if any)
# from .utils import helper
```

### Random Seeds
Always set seeds for reproducibility:
```python
import numpy as np
import random

# Set all seeds
np.random.seed(42)
random.seed(42)

# For sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# For tensorflow/keras
import tensorflow as tf
tf.random.set_seed(42)
```

### Plot Styling
```python
import matplotlib.pyplot as plt

# Use consistent style
plt.style.use('default')
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 12
```

---

## Reproducibility

### Fast/Slow Mode
Add a configuration cell at the top:

```python
# Configuration for runs
SMALL_RUN = True  # Set to False for full run

if SMALL_RUN:
    N_SAMPLES = 100
    N_ITERATIONS = 10
else:
    N_SAMPLES = 10000
    N_ITERATIONS = 100
```

### Synthetic Data
Use sklearn's `make_*` functions with `random_state=42`:
```python
from sklearn.datasets import make_classification, make_regression

# Classification
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Regression
X, y = make_regression(n_samples=1000, n_features=10, random_state=42)
```

---

## Output Policy

### Before Committing
**Clear all stored outputs** from notebooks before committing:

1. In Jupyter Lab: `Kernel > Restart Kernel and Run All...`
2. Or use nbconvert:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

3. Or use Jupytext for clean diffs:
   ```bash
   jupytext --to py:percent --clear-output notebook.ipynb
   ```

### Why Clear Outputs?
- Cleaner git diffs
- Smaller file sizes
- Ensures notebooks run from scratch

---

## Submitting Changes

### Pull Request Guidelines

1. **Small, focused changes** - One topic per PR
2. **Test your notebook** - Run all cells before submitting
3. **Clear outputs** - Remove all stored outputs
4. **Descriptive commits** - Explain what changed

### PR Title Format
- `feat: Add NumPy broadcasting challenges`
- `fix: Fix typo in pandas/README.md`
- `docs: Update classification notebook template`

---

## Getting Help

- Open an issue for questions
- Check existing issues before creating new ones
- Be respectful and constructive in discussions
