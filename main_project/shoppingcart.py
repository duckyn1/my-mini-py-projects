items = []
prices = []
total_price = 0

while True:
    item = input("What item you gonna buy? (e to exit): ")
    if item.lower() == "e":
        break
    elif item == "":
        print("Pls enter a item you gonna buy")
        item = input("What item you gonna buy? (e to exit): ")
    else:
        price = float(input(f"Enter price of ur {item}: $"))
        print(f"{item} in ur cart!")
        items.append(item)
        prices.append(price)

print("         --- CART ---          ")
for x in range(len(items)):
    print(f" ITEM: {items[x]} | PRICE: ${prices[x]:.2f}")

for price in prices:
    total_price = sum(prices)

print()
print(f"Total price: ${total_price:.2f}")
