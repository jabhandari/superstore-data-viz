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

## Push to GitHub
```bash
git init
git remote add origin https://github.com/YOUR-USERNAME/excel-data-viz.git
git add .
git commit -m "Add Excel Data Viz (Superstore)"
git branch -M main
git push -u origin main
```

## License
MIT
