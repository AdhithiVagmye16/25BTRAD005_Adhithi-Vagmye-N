# ============================================================
# Mini Project: Shop Bill Generator
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# Dept   : B.Tech Computer Science Engineering (AI & Data Engineering)
# College: Jain University
# ============================================================
# Concepts used: dictionaries, functions, loops, conditionals, string formatting
#
# Aim: Shop Bill Generator — select items from a fixed price list,
#      add quantities to a cart, generate final formatted bill
#      including subtotal, discount, GST and total payable.

def display_menu(price_list):
    print("=" * 40)
    print(f"{'ITEM':<15}{'PRICE (Rs.)':>15}")
    print("=" * 40)
    for item, price in price_list.items():
        print(f"{item:<15}{price:>15.2f}")
    print("=" * 40)


def generate_bill(price_list):
    cart = {}   # item -> quantity

    print("\nWelcome to PyMart!")
    display_menu(price_list)

    while True:
        item = input("\nEnter item name to buy (or 'done' to finish): ").strip()
        if item.lower() == "done":
            break
        if item not in price_list:
            print("Item not found in menu. Please try again.")
            continue
        qty = int(input(f"Enter quantity of {item}: "))
        if qty <= 0:
            print("Quantity must be positive.")
            continue
        cart[item] = cart.get(item, 0) + qty
        print(f"Added {qty} x {item} to cart.")

    if not cart:
        print("\nNo items purchased. Bill generation cancelled.")
        return

    print_bill(cart, price_list)


def print_bill(cart, price_list):
    subtotal = 0
    print("\n" + "=" * 40)
    print(f"{'PyMart - Final Bill':^40}")
    print("=" * 40)
    print(f"{'Item':<12}{'Qty':>6}{'Price':>10}{'Amount':>12}")
    print("-" * 40)

    for item, qty in cart.items():
        price = price_list[item]
        amount = price * qty
        subtotal += amount
        print(f"{item:<12}{qty:>6}{price:>10.2f}{amount:>12.2f}")

    print("-" * 40)
    print(f"{'Subtotal':<28}{subtotal:>12.2f}")

    # Discount: 10% off if subtotal crosses Rs.500
    discount = subtotal * 0.10 if subtotal > 500 else 0
    print(f"{'Discount (10% if >500)':<28}{discount:>12.2f}")

    taxable_amount = subtotal - discount
    # GST: 5%
    gst = taxable_amount * 0.05
    print(f"{'GST (5%)':<28}{gst:>12.2f}")

    total = taxable_amount + gst
    print("=" * 40)
    print(f"{'TOTAL PAYABLE':<28}{total:>12.2f}")
    print("=" * 40)
    print("Thank you for shopping with PyMart!")


# ---- Program starts here ----
price_list = {
    "Rice": 60.00,
    "Wheat": 45.00,
    "Sugar": 42.00,
    "Milk": 28.00,
    "Oil": 150.00,
    "Soap": 35.00,
}

generate_bill(price_list)
