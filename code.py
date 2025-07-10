import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment_rate_upto_11_2020.csv")

# Clean column names
df.columns = [col.strip() for col in df.columns]

# Check column names
print("Cleaned Column Names:")
print(df.columns)

# Show first 5 rows
print(df.head())

# Heatmap of correlation
plt.figure(figsize=(8, 6))

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Plot heatmap only on numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

# Unemployment rate by Region
plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")
plt.tight_layout()
plt.show()

# Time series plot if Date is available
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

plt.figure(figsize=(14, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', hue='Region', data=df)
plt.title("Unemployment Rate Over Time by Region")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Clean Date column
df['Date'] = pd.to_datetime(df['Date'])

# Rename 'Region.1' to 'Zone' for clarity
df.rename(columns={'Region.1': 'Zone'}, inplace=True)

# Correlation only on numeric data
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Numeric Columns)")
plt.show()

# Barplot: Unemployment Rate by Region
plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")
plt.tight_layout()
plt.show()

# Line plot: Trend over time
df = df.sort_values('Date')
plt.figure(figsize=(14, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', hue='Zone', data=df)
plt.title("Unemployment Rate Over Time by Zone")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
