inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

'''calculate the TotalRevenue
List Low stock item if stock is less than 5
calculte the categorywise Revenue'''

# 1. Total revenue 
total_revenue = 0
for item in inventory:
    revenue = item[2] * item[3]
    total_revenue += revenue

print("Total Revenue is: ", round(total_revenue, 2))

# 2. Low stock items 
print("Stock Items with less than 5 units :")
for item in inventory:
    if item[4] < 5:
        print("  ", item[0])

# 3. Category-wise revenue
category_revenue = {}

for item in inventory:
    category = item[1]
    revenue = item[2] * item[3]
    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print("Revenue by Category:")
for category, revenue in category_revenue.items():
    print("  ", category, ":", round(revenue, 2))