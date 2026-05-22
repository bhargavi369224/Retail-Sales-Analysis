import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

print("Dataset:")
print(df)

# Statistics
print("\nSummary Statistics:")
print(df.describe())

# Total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Category wise sales
category_sales = df.groupby("Category")["Sales"].sum()
print("\nCategory Sales:")
print(category_sales)

# Plot
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales Amount")
plt.savefig("sales_chart.png")
plt.show()