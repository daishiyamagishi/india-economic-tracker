# India Economic & Structural Tracker 🇮🇳📈

An automated data pipeline that extracts, cleans, and tracks comprehensive historical macroeconomic and structural indicators for India directly from the **World Bank API**. 

The pipeline runs automatically via **GitHub Actions**, ensuring that the dataset is always up to date from 1960 to the present day.

---

## 📊 Tracked Economic Indicators

To capture a well-rounded view of India's growth engine beyond just GDP, this tracker pulls the following public indicators:

| Category | Indicator Name | World Bank API Code | Description |
| :--- | :--- | :--- | :--- |
| **Macroeconomic** | GDP Growth | `NY.GDP.MKTP.KD.ZG` | Annual percentage growth rate of GDP at constant local currency. |
| **Macroeconomic** | Inflation | `FP.CPI.TOTL.ZG` | Consumer price inflation (annual %). |
| **Labor Market** | Unemployment | `SL.UEM.TOTL.ZS` | Total unemployment as a percentage of the total labor force. |
| **Digital Infrastructure** | Mobile Subscriptions | `IT.CEL.SETS.P2` | Mobile cellular subscriptions per 100 people. |
| **Global Integration** | FDI Inflows | `BX.KLT.DINV.WD.GD.ZS` | Foreign direct investment, net inflows as a percentage of GDP. |
| **Investment & Capital** | Gross Capital Formation | `NE.GDI.TOTL.ZS` | Domestic investment and infrastructure spending as a percentage of GDP. |

---

## ⚙️ How It Works (Automation Pipeline)

1. **Extraction (`extract_india_data.py`)**: A Python script utilizes the `wbgapi` library to query World Bank databases for India (`IND`) across all available years (1960–Present).
2. **Transformation**: The data is flattened, cleaned, renamed into user-friendly headers, and sorted chronologically using **Pandas**.
3. **Storage (`india_economic_data.csv`)**: The finalized dataset is exported directly into the repository root directory as a CSV file.
4. **Scheduling (GitHub Actions)**: Configured via `.github/workflows/auto_collect.yml`, the workflow runs automatically **every Monday at 08:00 UTC**, committing and pushing fresh data updates back to the repository without manual intervention.

---

## 🚀 Getting Started Locally

If you want to run the extraction script locally on your machine:

1. Clone this repository:
   ```bash
   git clone [https://github.com/daishiyamagishi/india-economic-tracker.git](https://github.com/daishiyamagishi/india-economic-tracker.git)
   cd india-economic-tracker

pip install pandas wbgapi

python extract_india_data.py

