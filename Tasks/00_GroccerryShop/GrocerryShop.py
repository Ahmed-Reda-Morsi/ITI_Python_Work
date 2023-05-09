# Define a dictionary to store the grocery items and their prices
Grocery_Items = {
    "carrot":   {"Category":"vegetables","price":15},
    "cucumber": {"Category":"vegetables","price":8},
    "tomato":   {"Category":"vegetables","price":12},
    "onion":    {"Category":"vegetables","price":17},
    "eggplant": {"Category":"vegetables","price":9},
    "potato":   {"Category":"vegetables","price":15},
    "banana":   {"Category":"Fruits","price":20},
    "pear":     {"Category":"Fruits","price":25},
    "peach":    {"Category":"Fruits","price":27}
}

# Define a set to store the unique categories of grocery items
grocery_categories ={"vegetables","Fruits"}

# Define an empty list to store the grocery items that the customer wants to buy
customer_cart = []

# Define a function to add a grocery item and its price to the grocery_items dictionary
def add_item():
    item_name = input("Enter the name of the item: ")
    item_price = float(input("Enter the price of one kilo of item: "))
    item_category = input("Enter the category of the item: ")
    Grocery_Items[item_name] = {"Category": item_category,"price": item_price}
    grocery_categories.add(item_category)
    print(f"{item_name} added to the grocery list.")

# Define a function to display the grocery items and their prices
def display_items():
    print("___________|Grocery List:")
    for item_name, item_details in Grocery_Items.items():
        print(f"{item_name}: {item_details['price']}")

# Define a function to display the categories of grocery items
def display_categories():
    print("___________|Grocery Categories:")
    for category in grocery_categories:
        print(category)

# Define a function to add items to the customer's cart
def add_to_cart():
    item_name  = input("Enter the name of the item you want to buy: ")
    item_amount= float(input("Enter the amount(Kilo) of the item : "))
    if item_name in Grocery_Items:
        customer_cart.append([item_name,item_amount])
        print(f"{item_name} added to your cart.\n")
    else:
        print(f"{item_name} is not in the grocery list.\n")

# Define a function to display the customer's cart
def display_cart():
    print("____________|Your Cart:")
    for item in customer_cart:
        itemAmountPrice=item[1]*Grocery_Items[item[0]]["price"]
        print(f"Item: {item[0]}    |  Amount : {item[1]} |    price :{itemAmountPrice}" )

# Define a function to calculate the total cost of the items in the customer's cart
def calculate_total():
    display_cart()
    total = 0
    for item_name in customer_cart:
        total += Grocery_Items[item_name[0]]["price"] * item_name[1]
    print(f"Total cost: {total}\n")

# Define the main function to run the grocery shop program
def Grocery_Shop():
    while True:
        print("______________________|Groccerry Shop System|________________")
        print("-> 1. Add item")
        print("-> 2. Display grocery list")
        print("-> 3. Display grocery categories")
        print("-> 4. Add item to cart")
        print("-> 5. Display cart")
        print("-> 6. Calculate total")
        print("-> 7. Exit")
        choice = int(input("Enter your choice (1-7): "))
        print("______________________________________________________________")
        if choice == 1:
            add_item()
        elif choice == 2:
            display_items()
        elif choice == 3:
            display_categories()
        elif choice == 4:
            add_to_cart()
        elif choice == 5:
            display_cart()
        elif choice == 6:
            calculate_total()
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


Grocery_Shop()
