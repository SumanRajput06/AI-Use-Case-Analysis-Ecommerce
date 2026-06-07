import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Load Data
df = pd.read_csv(r"C:\Users\beesh\OneDrive\Desktop\E-Commerce\Dataset.csv", encoding="cp1252")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Basic Analysis
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

# Data Cleaning
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df.dropna(subset=["CustomerID"])
print("Clean data rows:", len(df))

# Customer Analysis
print("Unique Customers:", df["CustomerID"].nunique())
print("\nTop Customers:")
print(df.groupby("CustomerID")["Revenue"].sum().sort_values(ascending=False).head(10))

# Chart 1 - Revenue by Country
df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Revenue by Country")
plt.tight_layout()
plt.savefig("revenue_by_country.png")
plt.close()  # ← use close() instead of show() to avoid blocking
print("Revenue chart saved ✅")

# Time Analysis
print("\nStarting time analysis...")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
print("Date converted ✅")
df["Month"] = df["InvoiceDate"].dt.to_period("M")
print("Month extracted ✅")

monthly_revenue = df.groupby("Month")["Revenue"].sum()
print("Monthly Revenue calculated ✅")
print(monthly_revenue)

# Chart 2 - Monthly Revenue
monthly_revenue.plot(kind="line", figsize=(12,5), marker="o", color="blue")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()
print("Monthly chart saved ✅")

# RFM Analysis
snapshot_date = df["InvoiceDate"].max() + datetime.timedelta(days=1)
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "Revenue": "sum"
}).reset_index()
rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]
print("\nRFM Table:")
print(rfm.head(10))
rfm.to_csv("rfm_analysis.csv", index=False)
print("RFM saved to rfm_analysis.csv ✅")

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


print("\nStarting Machine Learning - Customer Segmentation...")

# Load RFM data
rfm = pd.read_csv("rfm_analysis.csv")

# Scale the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])

# KMeans Clustering - 4 customer segments
kmeans = KMeans(n_clusters=4, random_state=42)
rfm["Segment"] = kmeans.fit_predict(rfm_scaled)

# Label segments
segment_labels = {0: "Lost Customers", 1: "At Risk", 2: "Loyal Customers", 3: "Champions"}
rfm["Segment_Label"] = rfm["Segment"].map(segment_labels)

print("\nCustomer Segments:")
print(rfm["Segment_Label"].value_counts())

# Save results
rfm.to_csv("customer_segments.csv", index=False)
print("Segments saved to customer_segments.csv ✅")

# Plot segments
rfm["Segment_Label"].value_counts().plot(kind="bar", color=["red","orange","blue","green"])
plt.title("Customer Segments")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("customer_segments.png")
plt.close()
print("Segment chart saved ✅")

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("\nStarting Machine Learning - Customer Segmentation...")

# Load RFM data
rfm = pd.read_csv("rfm_analysis.csv")

# Scale the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])

# KMeans Clustering - 4 customer segments
kmeans = KMeans(n_clusters=4, random_state=42)
rfm["Segment"] = kmeans.fit_predict(rfm_scaled)

# Label segments
segment_labels = {0: "Lost Customers", 1: "At Risk", 2: "Loyal Customers", 3: "Champions"}
rfm["Segment_Label"] = rfm["Segment"].map(segment_labels)

print("\nCustomer Segments:")
print(rfm["Segment_Label"].value_counts())

# Save results
rfm.to_csv("customer_segments.csv", index=False)
print("Segments saved to customer_segments.csv ✅")

# Plot segments
rfm["Segment_Label"].value_counts().plot(kind="bar", color=["red","orange","blue","green"])
plt.title("Customer Segments")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("customer_segments.png")
plt.close()
print("Segment chart saved ✅")