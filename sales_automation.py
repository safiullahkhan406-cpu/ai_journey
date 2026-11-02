# Day 22 - Sales Report Automation

# CSV module import kiya
import csv

# Counter import kiya
from collections import Counter

# Sales data
sales = [
    {"product": "Laptop", "quantity": 2, "price": 80000},
    {"product": "Mobile", "quantity": 5, "price": 30000},
    {"product": "Laptop", "quantity": 3, "price": 80000},
    {"product": "Keyboard", "quantity": 10, "price": 2000},
    {"product": "Mobile", "quantity": 2, "price": 30000},
    {"product": "Mouse", "quantity": 8, "price": 1500}
]

# Total revenue calculate karna
total_revenue = sum(
    item["quantity"] * item["price"]
    for item in sales
)

# Total products sold
total_quantity = sum(
    item["quantity"]
    for item in sales
)

# Product-wise quantity count
product_sales = Counter()

for item in sales:
    product_sales[item["product"]] += item["quantity"]

# Highest selling product
best_product = product_sales.most_common(1)[0]

# Sales report create karna
report = []

for product, quantity in product_sales.items():

    # Product ki price find karna
    price = next(
        item["price"]
        for item in sales
        if item["product"] == product
    )

    # Revenue calculate karna
    revenue = quantity * price

    report.append({
        "product": product,
        "quantity": quantity,
        "revenue": revenue
    })


# Report ko revenue ke mutabiq sort karna
report = sorted(
    report,
    key=lambda item: item["revenue"],
    reverse=True
)


# CSV file mein report save karna
with open("sales_report.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["product", "quantity", "revenue"]
    )

    writer.writeheader()
    writer.writerows(report)


# Final report display karna
print("\n===== SALES REPORT =====")

print("Total Products Sold:", total_quantity)

print("Total Revenue:", total_revenue)

print("Best Selling Product:", best_product[0])

print("Best Selling Quantity:", best_product[1])

print("\nProduct Wise Revenue:")

for item in report:
    print(
        item["product"],
        "- Quantity:", item["quantity"],
        "- Revenue:", item["revenue"]
    )

print("\nSales Report Saved Successfully!")
