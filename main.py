import pandas as pd

df = pd.read_csv(r"C:\Users\beesh\OneDrive\Desktop\E-Commerce\Dataset.csv",encoding="cp1252")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nCountries:")
print(df["Country"].value_counts().head())

print("\nTop Products:")
print(df["Description"].value_counts().head(10))

# Revenue Analysis
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("Total Revenue:", df["Revenue"].sum())
print("\nRevenue by Country:")
print(df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10))

print("\nTop Revenue Products:")
print(df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10))

# Remove cancelled orders (InvoiceNo starts with 'C')
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Remove null CustomerIDs
df = df.dropna(subset=["CustomerID"])

print("Clean data rows:", len(df))

# How many unique customers?
print("Unique Customers:", df["CustomerID"].nunique())

# Top customers by revenue
print("\nTop Customers:")
print(df.groupby("CustomerID")["Revenue"].sum().sort_values(ascending=False).head(10))

import matplotlib.pyplot as plt

# Top 10 countries by revenue
df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Revenue by Country")
plt.tight_layout()
plt.savefig("revenue_by_country.png")
plt.show()

