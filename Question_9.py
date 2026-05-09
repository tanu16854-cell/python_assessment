# Q9. Develop a dictionary-based inventory management system where users can add products, update quantity,
# search products, and display low-stock items

inventory = {}

while True:
    print("\n1.Add 2.Update 3.Search 4.Low Stock 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        p = input("Product name: ")
        q = int(input("Quantity: "))
        inventory[p] = q

    elif ch == 2:
        p = input("Product name: ")
        if p in inventory:
            inventory[p] = int(input("New quantity: "))

    elif ch == 3:
        p = input("Search product: ")
        print(inventory.get(p, "Not Found"))

    elif ch == 4:
        for k, v in inventory.items():
            if v < 5:
                print(k, "Low Stock:", v)

    elif ch == 5:
        break