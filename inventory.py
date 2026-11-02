# inventory.py
# Author: Ayme 
# Modle 10 Lab: Inventory List Manager

# Reflection Questions
# 1. What was surprising about Python lists is how flexible they are compared to traditional variables. The most surprising thing about Python lists is how flexible they are compared to traditional variables. I expected lists to only hold a fixed number of single-typed values, but learning that they are dynamic can hold mixed data types and allow negative indexing to grab items from the end was a really cool surprise.
# 2. In a retail inventory or a sales tracking scenario, manually sorting, filtering, and running calculations on thousands of rows in Excel can be slow and prone to human error. Using a python list to store inventory items allows you to loop through all records instantly and slice specifc data and calculate totals by updating quantities automatically with just a few lines of code. 
# Exercise 1: build a list

print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "tape", "marker"]
print(inventory)
print(len(inventory))


# Exercise 2: Index Practice

print("--- Exercise 2: Index practice ---")
print(inventory[0]) # always grabs the first item
print(inventory[-1]) # always grabs the last item 

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item (not hard coded)

print("--- Exercise 3: List Slicing ---")

print(inventory[:3]) # grabs the first three items
print(inventory[-2:]) # grabs the last two items 
print(inventory[::2])

print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # adds an item to the end of the list
print(inventory) 

inventory.remove("tape")
print(inventory)

inventory.sort() # sorts the list in alphabetical order
print(inventory)

print("--- Exercise 5: Tupple Comparison ---")
coords = (40.7128, -74.0060) # New York City coordinates

coords[0] = 99
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caght: {error}")
    print("Tupple protect coordinates from being changed by accident.")

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # an empty list
for price in prices:
    discounted.append(round(price * 0.9, 2)) # apply a 10% discount

print(prices)
print(discounted)

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = [] # an empty list

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / }")