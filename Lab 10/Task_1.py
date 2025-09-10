def discount(price, category):
    if category == "student":
        return price * (0.9 if price > 1000 else 0.95)
    return price * 0.85 if price > 2000 else price

price = float(input("Enter the price: "))
category = input("Enter the category (student/other): ")
print(f"Discounted price: {discount(price, category):.2f}")