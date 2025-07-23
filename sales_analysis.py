import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
sales_data = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataset
print(sales_data.head())

# Create a figure with subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Group by Region and sum the Sales
sales_summary = sales_data.groupby('Region')['Sales'].sum()
sales_summary.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title('Total Sales by Region')
ax1.set_xlabel('Region')
ax1.set_ylabel('Total Sales ($)')
ax1.tick_params(axis='x', rotation=0)

# Group by Product and sum the Sales
product_summary = sales_data.groupby('Product')['Sales'].sum()
product_summary.plot(kind='pie', ax=ax2, autopct='%1.1f%%', startangle=90)
ax2.set_title('Sales Distribution by Product')
ax2.set_ylabel('')  # Hide y-label for pie chart

# Calculate and plot average profit by Category
category_profit = sales_data.groupby('Category')['Profit'].mean()
category_profit.plot(kind='bar', ax=ax3, color='lightgreen')
ax3.set_title('Average Profit by Category')
ax3.set_xlabel('Category')
ax3.set_ylabel('Average Profit ($)')
ax3.tick_params(axis='x', rotation=45)

# Adjust layout and display all plots at once
plt.tight_layout()
plt.show()