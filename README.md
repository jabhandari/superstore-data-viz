
# Superstore Data Visualization (Python)

Lightweight project for exploratory analysis and visualization of the Superstore dataset.

## Contents
- `analysis.py` — main script that loads `superstore.csv` and produces plots/tables
- `superstore.csv` — source dataset used for analysis

## Requirements
- Python 3.8+
- pandas
- matplotlib (or seaborn)

Install dependencies:

```bash
pip install pandas matplotlib seaborn
pip install -r requirements.txt

```

## Quickstart
Run the analysis script to generate visualizations and summary output:

```bash
python analysis.py
```

If you want to inspect the CSV first, open `superstore.csv` in a spreadsheet viewer.

## Notes
- The script expects `superstore.csv` in the repository root.
- Modify `analysis.py` to change plots or output locations.
# Excel Data Visualization – Superstore


Fast, interview-ready Excel dashboard built from your Superstore CSV.

## Files
- `data/superstore.csv` – (from your upload)
- `data/superstore.xlsx` – same data + **HowTo** sheet to build pivots quickly
- `images/` – charts generated from the dataset (if columns were detected)

## Build these in Excel
1. **Monthly Sales Trend (Line)** — Rows: `Date` (Group → Months) · Values: Sum `Sales`
2. **Top Products by Sales (Bar)** — Rows: `Product Name` · Values: Sum `Sales` · Sort Desc
3. **Profit by Region (Pie)** — Rows: `Region` · Values: Sum `Profit`

## License
MIT
