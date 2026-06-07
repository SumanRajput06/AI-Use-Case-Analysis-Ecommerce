import pandas as pd

df = pd.read_csv(r"C:\Users\beesh\OneDrive\Desktop\E-Commerce\Dataset.csv",encoding="cp1252")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nCountries:")
print(df["Country"].value_counts().head())

print("\nTop Products:")
print(df["Description"].value_counts().head(10))