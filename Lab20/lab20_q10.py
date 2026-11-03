inventory = {
    "pen": (10.0, 50),
    "notebook": (45.0, 20),
    "eraser": (5.0, 100),
    "marker": (30.0, 15),
}

cart = {}

print("Welcome to the Billing System!")
print("Enter your items and quantity (e.g., 'pen 3'). Type 'done' to finish.\n")

while True:
    user_input = input("Enter item and quantity (or 'done'): ").strip()

    if user_input.lower() == 'done':
        break
    parts = user_input.split()
    if len(parts) != 2:
        print("Invalid format! Please enter both the item name and quantity (e.g., 'pen 3').")
        continue

    item, qty_str = parts[0].lower(), parts[1]

    if item not in inventory:
        print(f"'{item}' is not available in our inventory.")
        continue

    if not qty_str.isdigit() or int(qty_str) <= 0:
        print("Quantity must be a valid positive whole number.")
        continue

    quantity = int(qty_str)
    price, stock = inventory[item]

    if quantity > stock:
        print(f"Not enough stock! Only {stock} units of '{item}' left.")
        continue

    cart[item] = cart.get(item, 0) + quantity

    inventory[item] = (price, stock - quantity)
    print(f"Added {quantity} {item}(s) to your cart.")

print("\n" + "=" * 45)
print("RECEIPT".center(45))
print("=" * 45)
print(f"{'Item'.ljust(15)}{'Qty'.rjust(6)}{'Unit Price'.rjust(12)}{'Total'.rjust(12)}")
print("-" * 45)

subtotal = 0.0
for item, qty in cart.items():
    unit_price = inventory[item][0]
    line_total = qty * unit_price
    subtotal += line_total

    print(
        f"{item.capitalize().ljust(15)}{str(qty).rjust(6)}{f'₹{unit_price:.2f}'.rjust(12)}{f'₹{line_total:.2f}'.rjust(12)}")

print("-" * 45)
print(f"{'Subtotal:'.ljust(33)}{f'₹{subtotal:.2f}'.rjust(12)}")

discount = 0.0
if subtotal > 500:
    discount = subtotal * 0.10
    print(f"{'10% Discount:'.ljust(33)}{f'-₹{discount:.2f}'.rjust(12)}")

final_total = subtotal - discount
print("=" * 45)
print(f"{'Final Total:'.ljust(33)}{f'₹{final_total:.2f}'.rjust(12)}")
print("=" * 45)

print("\n" + "=" * 35)
print("UPDATED INVENTORY STATUS".center(35))
print("=" * 35)
print(f"{'Item'.ljust(15)}{'Stock Left'.rjust(10)}{' Status'.ljust(10)}")
print("-" * 35)

for item, (price, stock) in inventory.items():
    status = "LOW STOCK" if stock < 10 else "OK"
    print(f"{item.capitalize().ljust(15)}{str(stock).rjust(10)}  {status.ljust(10)}")
print("=" * 35)