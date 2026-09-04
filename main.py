import pandas as pd
import os

# File path
file_path = os.path.join("Data", "sales_data.csv")

# Load the sales data
df = pd.read_csv(file_path)

# Display first 5 rows
print("\nFirst 5 rows of the sales data:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Total sales
total_sales = df["Total_Sales"].sum()

# Average sales
average_sales = df["Total_Sales"].mean()

# Total quantity sold
total_quantity = df["Quantity"].sum()

print("\nSales Analysis:")
print(f"Total Sales: {total_sales:.2f}")
print(f"Average Sales: {average_sales:.2f}")
print(f"Total Quantity Sold: {total_quantity}")

# Sales by product
print("\nSales by Product:")
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
print(product_sales)

# Sales by region
print("\nSales by Region:")
region_sales = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
print(region_sales)

# Top-selling product
top_product = product_sales.idxmax()
print(f"\nTop-Selling Product: {top_product}")

# Best-performing region
best_region = region_sales.idxmax()
print(f"Best-Performing Region: {best_region}")

print("\nSales analysis completed successfully!")


import matplotlib.pyplot as plt

# Sales by Product - Bar Chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Visualization/sales_by_product.png")
plt.show()

# Sales by Region - Bar Chart
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Visualization/sales_by_region.png")
plt.show()