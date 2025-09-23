"""
Superstore analysis using pandas + matplotlib.
This script works whether your files are in a "data/" folder or uploaded flat.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# Try a few likely paths (supports both folder & flat uploads)
candidates = ['data/superstore.csv', 'superstore.csv', 'data_superstore.csv']
csv_path = None
for c in candidates:
    if os.path.exists(c):
        csv_path = c
        break
if csv_path is None:
    raise FileNotFoundError("Couldn't locate the CSV. Put it at data/superstore.csv or next to this script.")

df = pd.read_csv(csv_path, engine="python")

# Detect common column names (Tableau Superstore compatible)
def pick(cols, *names):
    low = {{k.lower(): k for k in cols}}
    for n in names:
        if n.lower() in low: 
            return low[n.lower()]
    for n in names:
        for k,v in low.items():
            if n.lower() in k: 
                return v
    return None

col_date   = pick(df.columns, "Order Date","OrderDate","Order_Date","Date")
col_sales  = pick(df.columns, "Sales","Revenue","Amount")
col_profit = pick(df.columns, "Profit","Margin")
col_region = pick(df.columns, "Region","Market","Area")
col_prod   = pick(df.columns, "Product Name","Product","Sub-Category","Item")

# Ensure output directory
os.makedirs("images", exist_ok=True)

# 1) Monthly Sales Trend
if col_date and col_sales:
    d2 = df.copy()
    d2[col_date] = pd.to_datetime(d2[col_date], errors="coerce")
    trend = d2.dropna(subset=[col_date]).groupby(pd.Grouper(key=col_date, freq="MS"))[col_sales].sum().reset_index()
    plt.figure()
    plt.plot(trend[col_date], trend[col_sales])
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.savefig("images/monthly_sales_trend.png", bbox_inches="tight")

# 2) Top Products by Sales
if col_prod and col_sales:
    top = df.groupby(col_prod)[col_sales].sum().sort_values(ascending=False).head(10)
    plt.figure()
    top.plot(kind="bar")
    plt.title("Top Products by Sales")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.savefig("images/top_products.png", bbox_inches="tight")

# 3) Profit by Region
if col_region and col_profit:
    reg = df.groupby(col_region)[col_profit].sum()
    plt.figure()
    plt.pie(reg.values, labels=reg.index, autopct="%1.1f%%")
    plt.title("Profit by Region")
    plt.savefig("images/profit_by_region.png", bbox_inches="tight")

print("Charts saved in ./images")
