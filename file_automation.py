# Automation Lesson 2
# Read sales from a file and create a report
# Step 1: Read sales from the file
with open("sales.txt", "r") as file:
    lines = file.readlines()
# Step 2: Convert text into numbers
sales = [int(line.strip()) for line in lines]
# Step 3: Calculate total and average
total = sum(sales)
average = total / len(sales)
# Step 4: Create the report
report = f"""
DAILY SALES REPORT
------------------
Total Sales: Rs. {total}
Number of Sales: {len(sales)}
Average Sales: Rs. {average}
"""
# Step 5: Save the report
with open("sales_report.txt", "w") as file:
    file.write(report)
print("Report generated automatically!")
print(f"Total Sales: Rs. {total}")
print(f"Average Sales: Rs. {average}")
