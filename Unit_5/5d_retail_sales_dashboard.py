import csv
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter number of products: "))
products = []
sales = []
for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    amount = float(input("Enter sales amount: "))
    products.append(name)
    sales.append(amount)

# Store data in CSV file
with open("sales.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Sales"])
    writer.writerows(zip(products, sales))

# Read CSV file
with open("sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)
products = [row[0] for row in data]
sales = np.array([float(row[1]) for row in data])

# Display sales data
print("\nRETAIL SALES DATA")
for p, s in zip(products, sales):
    print(p, ":", s)

# Sales analysis using NumPy
print("\nTotal Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))

# Bar Chart
plt.bar(products, sales)
plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# Line Chart
plt.plot(products, sales, marker='o')
plt.title("Product Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# Scatter Plot
plt.scatter(products, sales)
plt.title("Product Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
