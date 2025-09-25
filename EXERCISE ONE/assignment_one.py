
import array

ecom_orders = [
    {'id': 101, 'name': 'Laptop', 'quantity': 2, 'price': 1200.50},
    {'id': 102, 'name': 'Mouse', 'quantity': 15, 'price': 25.00},
    {'id': 103, 'name': 'Keyboard', 'quantity': 8, 'price': 75.99},
    {'id': 104, 'name': 'Monitor', 'quantity': 3, 'price': 350.25},
    {'id': 105, 'name': 'USB Hub', 'quantity': 20, 'price': 15.00},
    {'id': 106, 'name': 'Headphones', 'quantity': 10, 'price': 99.99}
]


quantities = [order['quantity'] for order in ecom_orders]
total_quantity = sum(quantities)
average_quantity = total_quantity / len(quantities)
min_quantity = min(quantities)
max_quantity = max(quantities)
print("original list ")
for order in ecom_orders:
    print(order)
print(f"Ints: The total quantity of items is {total_quantity}.")
print(f"Ints: The average quantity is {average_quantity:.2f}.")
print(f"Ints: The minimum quantity is {min_quantity} and the maximum is {max_quantity}.")
orders_list_copy = ecom_orders.copy()
new_order = {'id': 107, 'name': 'Webcam', 'quantity': 5, 'price': 59.99}
orders_list_copy.append(new_order)
print("\nLists: List after adding 'Webcam':")
for order in orders_list_copy:
    print(order)