# Kaizen-Sigma Methodology: Lattice Auditor 🛡️📉

> **Continuous Improvement (PDCA) meets Statistical Rigor (Six Sigma).**

Welcome to the **Kaizen-Sigma Methodology** repository. This project is a specialized transformation of the Sigma Lattice Auditor, pivoted towards a Kaizen-centered framework for continuous measurement, waste reduction (**Muda**), and standardized work stability.

---

## 🏗️ The Kaizen-Sigma Framework

This repository implements the **Continuous Improvement Loop (PDCA)** as a core engine for process reliability:

1.  **Plan**: Analyze logs for variance and waste (Muda).
2.  **Do**: Execute iterative improvements and data generation.
3.  **Check**: Verify stability against the **Standardization Wedge**.
4.  **Act**: Update standards to prevent quality backslide.

---

## 📊 Core Components

### 🔄 PDCA Engine (`scripts/audit_engine/`)

An automated audit engine that models the evolution of process maturity.

- **`kaizen_data_gen.py`**: Generates synthetic audit logs. It simulates the exponential decay of waste (**Muda**) and the tightening of process variance over time.

### 📜 Methodology & Standards (`methodology/`)

- **`kaizen_events/`**: Stores continuous improvement logs (`continuous_improvement_log.csv`).
- **`standard_work/`**: Contains the **Process Standards Wedge** (`process_standards.md`), defining the current "Best Practice" benchmarks.

---

## 🚀 Getting Started

### 📦 Installation

Ensure you have Python 3.11+ and a virtual environment ready:

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 🛠️ Running the Kaizen Cycle

1.  **Generate Audit Data**:

    ```powershell
    python scripts/audit_engine/kaizen_data_gen.py
    ```

    This will update `methodology/kaizen_events/continuous_improvement_log.csv` with 150 iterations of improvement data.

2.  **Verify Standards**:
    Review `methodology/standard_work/process_standards.md` to compare current performance against established stability thresholds (Target Mean: 8.5h).

---

## 📈 Quality Metrics Verified

- **PCE % (Process Cycle Efficiency)**: Ratio of value-add time to total lead time.
- **Sigma Stability**: Automated outlier detection based on the 1.2h Standard Deviation limit.
- **Muda Reduction**: Tracking the reduction of non-value-add hours across iterations.

---

## 🛡️ Governance & Safety

Powered by the **Antigravity AI Auditor**, ensuring that every code refactor adheres to the **Standardization Wedge** to prevent any regression in process quality.

---

_Ref: Kaizen Continuous Improvement (Pages 247-254)_
