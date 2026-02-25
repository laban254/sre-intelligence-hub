# 🧠 SRE Intelligence Hub
**Industrial-grade Machine Learning for Infrastructure & Operations.**

[![CI Status](https://github.com/laban254/sre-intelligence-hub/actions/workflows/ci.yml/badge.svg)](#)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue)](#)
[![Theme](https://img.shields.io/badge/Context-Observability--First-blueviolet)](#)
[![Reproducibility](https://img.shields.io/badge/Hashes-Verified-success)](#)

---

## 🤖 Infrastructure Intelligence
The **SRE Intelligence Hub** provides high-fidelity Machine Learning workflows tailored for modern observability. Every module leverages system telemetry—CPU, Memory, Network, and Log Levels—to solve critical production failure scenarios.

---

## ⚡ Capabilities

### �️‍🗨️ Intelligent Monitoring (`03_machine_learning/`)
Solving the "hard" problems in production using ML:
*   **Anomaly Detection:** Native **Isolation Forest** implementation to detect DDoS attacks and database locks without manual thresholds.
*   **Log Clustering:** Automatic grouping of millions of unstructured logs into "Healthy", "Slow", and "Failing" behaviors.
*   **Predictive scaling:** Forecasting application latency based on concurrent connection spikes using Regression models.

### 🤖 MLOps & Production Pipelines
ML is only useful if it runs reliably in a CI/CD environment.
*   **Leakage-Free Pipelines:** Preprocessing + models bundled for consistent deployment.
*   **Operational Metrics:** Prioritizing **Precision (Alert Fatigue)** and **Recall (Missed Outages)** over simple binary accuracy.
*   **Automated Tuning:** Self-optimizing hyperparameters for API timeout prediction via **GridSearchCV**.

### 🌌 Observability Visuals (`02_visualization/`)
Professional-grade reporting designed for post-mortems and incident analysis.
*   **RCA Dashboards:** Automated charts with alert thresholds and OOM event markers.
*   **Drift Detection:** Using statistical tests (KS-test) to detect when infrastructure performance shifts permanently.

---

## 🦾 Automation & Tooling
Built with a DevOps mindset, the hub includes CLI tools for speed and reproducibility.

### 🧬 Data Ingestion (`fetch_data.py`)
Centralized data fetching with built-in **Integrity Verification (MD5 Hashes)**.
```bash
python fetch_data.py --quick     # Ingest small samples for fast testing
python fetch_data.py --full      # Ingest full datasets for training
python fetch_data.py --verify    # Verify data integrity against known hashes
```

### 🎛️ Execution Modes (`notebook_toggle.py`)
Toggle between fast iteration and complete training directly from the CLI or within Jupyter.
*   **Quick Mode:** Uses 10% of data and 1/10th of iterations for instant feedback.
*   **Full Mode:** Leverages all CPU cores (`n_jobs=-1`) and full datasets for production-grade models.

---

## ⚡ Quick Start

1.  **Clone & Install**
    ```bash
    git clone https://github.com/laban254/sre-intelligence-hub.git
    cd sre-intelligence-hub
    pip install -r requirements.txt
    ```

2.  **Ingest Sample Data**
    ```bash
    python fetch_data.py --quick
    ```

3.  **Run a Scenario**
    Open `03_machine_learning/scikit-learn/unsupervised-learning-algorithms/anomality.ipynb` to see the Isolation Forest in action.

---

## ⚖️ Philosophy & License
We prioritize **Precision** (avoiding Alert Fatigue) ensuring that when a model fires, it's worth an engineer's attention.

*Distributed under the MIT license.*
