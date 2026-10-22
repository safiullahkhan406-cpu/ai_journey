# Day 14: Daily Sales Analyzer
# Shop ki daily sales calculate karna
sales = [1500, 2500, 1800, 3200, 2000]
# Tamam sales ka total calculate karo
total_sales = sum(sales)
# Sales ki tadaad count karo
total_days = len(sales)
# Average sales calculate karo
average_sales = total_sales / total_days
# Report display karo
print("DAILY SALES REPORT")
print("-" * 25)
print(f"Total Sales: Rs. {total_sales}")
print(f"Total Days: {total_days}")
print(f"Average Sales: Rs. {average_sales}")
