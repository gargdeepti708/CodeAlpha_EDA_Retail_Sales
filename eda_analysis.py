import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# 1. LOAD DATASET
# =========================================================

file_path = "dataset/Supermart Grocery Sales - Retail Analytics Dataset.csv"

df = pd.read_csv(file_path)


# =========================================================
# 2. BASIC DATA UNDERSTANDING
# =========================================================

print("\n========== DATASET INFORMATION ==========")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNumerical Summary:")
print(df.describe())


# =========================================================
# 3. DATE CONVERSION
# =========================================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed"
)


# =========================================================
# 4. CATEGORY-WISE SALES
# =========================================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== CATEGORY-WISE SALES ==========")
print(category_sales)

plt.figure(figsize=(10, 5))
category_sales.plot(kind="bar")

plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output/category_sales.png")
plt.show()


# =========================================================
# 5. CATEGORY-WISE PROFIT
# =========================================================

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== CATEGORY-WISE PROFIT ==========")
print(category_profit)

plt.figure(figsize=(10, 5))
category_profit.plot(kind="bar")

plt.title("Category-wise Total Profit")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output/category_profit.png")
plt.show()


# =========================================================
# 6. REGION-WISE SALES
# =========================================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REGION-WISE SALES ==========")
print(region_sales)

plt.figure(figsize=(10, 5))
region_sales.plot(kind="bar")

plt.title("Region-wise Total Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output/region_sales.png")
plt.show()


# =========================================================
# 7. MONTHLY SALES TREND
# =========================================================

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output/monthly_sales.png")
plt.show()


# =========================================================
# 8. SUB-CATEGORY-WISE SALES
# =========================================================

subcategory_sales = (
    df.groupby("Sub Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SUB-CATEGORY-WISE SALES ==========")
print(subcategory_sales)

plt.figure(figsize=(10, 5))
subcategory_sales.plot(kind="bar")

plt.title("Sub-Category-wise Total Sales")
plt.xlabel("Sub Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output/subcategory_sales.png")
plt.show()


# =========================================================
# 9. DISCOUNT VS PROFIT
# =========================================================

print("\n========== DISCOUNT VS PROFIT ==========")

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("output/discount_vs_profit.png")
plt.show()


# =========================================================
# 10. REGION DATA QUALITY CHECK
# =========================================================

region_check = df.groupby("Region")["Sales"].agg(
    ["count", "sum", "mean"]
)

print("\n========== REGION DATA QUALITY CHECK ==========")
print(region_check)


# =========================================================
# 11. SUB-CATEGORY-WISE PROFIT
# =========================================================

subcategory_profit = (
    df.groupby("Sub Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SUB-CATEGORY-WISE PROFIT ==========")
print(subcategory_profit)

plt.figure(figsize=(10, 5))
subcategory_profit.plot(kind="bar")

plt.title("Sub-Category-wise Total Profit")
plt.xlabel("Sub Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output/subcategory_profit.png")
plt.show()


# =========================================================
# 12. OVERALL BUSINESS PERFORMANCE
# =========================================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
profit_margin = (total_profit / total_sales) * 100

print("\n========== OVERALL PERFORMANCE ==========")

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Profit Margin (%):", profit_margin)


print("\n========== EDA COMPLETED SUCCESSFULLY ==========")
import matplotlib.pyplot as plt

# 1. Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/sales_by_region.png")
plt.show()


# 2. Monthly Sales Trend
monthly_sales = df.groupby("Order Date")["Sales"].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/monthly_sales_trend.png")
plt.show()


# 3. Top 10 Sub-Categories by Sales
subcat_sales = df.groupby("Sub Category")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
subcat_sales.plot(kind="bar")
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub Category")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("output/top_10_subcategories_sales.png")
plt.show()


# 4. Sub-Category Profit
subcat_profit = df.groupby("Sub Category")["Profit"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
subcat_profit.plot(kind="bar")
plt.title("Top 10 Sub-Categories by Profit")
plt.xlabel("Sub Category")
plt.ylabel("Profit")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("output/top_10_subcategories_profit.png")
plt.show()


print("\n========== VISUALIZATION COMPLETED ==========")
# ==========================================
# BUSINESS INSIGHTS
# ==========================================

print("\n========== BUSINESS INSIGHTS ==========")

# 1. Best Region by Sales
best_region = df.groupby("Region")["Sales"].sum().idxmax()
best_region_sales = df.groupby("Region")["Sales"].sum().max()

print(f"1. Highest Sales Region: {best_region}")
print(f"   Sales: ₹{best_region_sales:,.2f}")


# 2. Best Sub-category by Sales
best_sales_subcat = df.groupby("Sub Category")["Sales"].sum().idxmax()
best_sales_value = df.groupby("Sub Category")["Sales"].sum().max()

print(f"\n2. Highest Sales Sub-category: {best_sales_subcat}")
print(f"   Sales: ₹{best_sales_value:,.2f}")


# 3. Best Sub-category by Profit
best_profit_subcat = df.groupby("Sub Category")["Profit"].sum().idxmax()
best_profit_value = df.groupby("Sub Category")["Profit"].sum().max()

print(f"\n3. Highest Profit Sub-category: {best_profit_subcat}")
print(f"   Profit: ₹{best_profit_value:,.2f}")


# 4. Best Sales Month
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

print(f"\n4. Highest Sales Month: {best_month}")
print(f"   Sales: ₹{best_month_sales:,.2f}")
# 6. Data Quality Check
region_counts = df["Region"].value_counts()

print("\n6. Region Data Quality")
print(region_counts)

if region_counts.min() < 10:
    print("\n   WARNING: Some regions have very few records.")
    print("   Regional comparison should be interpreted carefully.")


print("\n========== BUSINESS INSIGHTS COMPLETED ==========")
