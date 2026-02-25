# SRE Intelligence Hub

Learn the machine learning skills needed to build modern infrastructure intelligence tools: anomaly detection, log clustering, time series forecasting, and production deployment — all applied to real infrastructure data.

[![CI Status](https://github.com/laban254/sre-intelligence-hub/actions/workflows/ci.yml/badge.svg)](#)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue)](#)

---

## 🎯 Outcomes

After completing this track, you will be able to:
1.  **Detect Anomalies:** Automatically flag unusual behavior in Prometheus-style metrics using Isolation Forests and Autoencoders.
2.  **Cluster Error Logs:** Parse unstructured system logs and use NLP (TF-IDF) + K-Means to automatically group new error patterns.
3.  **Forecast Infrastructure Load:** Predict future CPU/Memory constraints using time-series forecasting (LSTMs).
4.  **Deploy ML to Production:** Take a model from a Jupyter Notebook and deploy it as a FastAPI endpoint inside a Docker container.

## 👥 Who This Is For

This repository is built specifically for **Site Reliability Engineers (SREs), DevOps Engineers, and Platform Engineers** who want to understand modern AI/ML tooling. It strips away the generic "house price prediction" examples found in most data science tutorials and replaces them with real problems you face in production.

### Why This Repository?

| Feature | Standard Data Science Courses | This Repository |
| :--- | :--- | :--- |
| **Primary Audience** | Aspiring Data Scientists | Software/Infrastructure Engineers |
| **Datasets** | Synthetic or Generic (Titanic, Iris) | Real System Logs, Infrastructure Metrics |
| **End Goal** | Training a static model | Deploying an API + Docker Container |
| **Key Topics** | Pandas, Matplotlib, Scikit-Learn | Anomaly Detection, MLOps, LLM Fine-Tuning |

---

## 🗺️ The Learning Journey

This curriculum is organized progressively. You don't need to finish it in one weekend; treat it as an evolving toolkit for your daily engineering tasks.

### `01_foundations/`
*   **NumPy:** Arrays, broadcasting, and numerical performance.
*   **Pandas:** Data manipulation, cleaning messy data, and complex aggregations.
*   **Distributed Data:** Using **PySpark** on a local cluster to group logs that won't fit entirely in memory.

### `02_visualization/`
*   **Matplotlib & Seaborn:** Creating operational dashboards and visualizing statistical anomalies.

### `03_machine_learning/`
*   **Scikit-learn:** Preprocessing, classification, regression, and clustering algorithms.

### `04_deep_learning/`
*   **Keras:** Historical neural network applications.
*   **PyTorch:** Modern industrial implementations focusing on Time Series prediction (LSTMs) for infrastructure forecasting.

### `05_sre_applications/`
*   **Anomaly Detection:** Finding the needle in the haystack of Prometheus metrics.
*   **Log Intelligence:** Grouping millions of log lines into actionable categories using K-Means and TF-IDF.
*   **MLOps Tracking:** Wrapping Scikit-Learn training in **MLflow** to track metrics and save model artifacts inside a local SQLite database.
*   **Model Monitoring:** Utilizing **Kolmogorov-Smirnov (KS) tests** to detect data drift (statistical shifts) in your infrastructure metrics over time.
*   **LLM Fine-Tuning:** Tailoring small LLMs (like Llama 3) via LoRA Adapters to understand your specific system architecture.

### `06_capstones/` (Upcoming)
*   **Predictive Maintenance:** End-to-end XGBoost model with SHAP explainability and CLI tool deployment.

---

## 🛠️ Installation

**Unified Environment (recommended)**
```bash
pip install -r requirements.txt
```

**Per-topic Installation**
Install only what you need (e.g., just the foundations):
```bash
pip install -r 01_foundations/numpy/requirements.txt
```

---

## 🧪 Quality & Reproducibility

*   **Smoke tests**: Automatically executed via GitHub Actions (`.github/workflows/ci.yml`) on every PR.
*   **Format & Linting**: Enforced with `black` and `ruff`.
*   **Data Fetching**: The `fetch_data.py` supports standard HTTP, AWS S3 (`s3://`), and Hugging Face (`hf://`) protocols with integrity verification hashes built-in.
*   **Seeds**: Use `random_state=42` across all notebooks for deterministic results.
*   **Clean Commits**: Output cells are cleared before committing to reduce noise.

---

## 📝 License

Educational use. See individual notebooks for dataset licenses.
