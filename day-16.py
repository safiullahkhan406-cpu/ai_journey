# Day 16: Smart Price Filter
# Products ki prices ki list
prices = [500, 1200, 2500, 800, 4000, 1500]
# Lambda har price ko check karega ke woh 1000 se zyada hai ya nahi
expensive_prices = list(filter(lambda price: price > 1000, prices))
# Har mehngi price par 10% discount lagao
discounted_prices = list(map(lambda price: price * 0.90, expensive_prices))
# Original result print karo
print("Original Prices:", prices)
# Sirf 1000 se zyada prices print karo
print("Expensive Prices:", expensive_prices)
# Discount ke baad prices print karo
print("Discounted Prices:", discounted_prices)
