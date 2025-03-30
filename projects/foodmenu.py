menu = {
  'Pizza':120,
  'Pasta':200,
  'Burger':90,
  'Salad':70,
  'Coffee':130,
  'Tea':20,
  'Juice':50,

}.lower()
# greeting
print("welcome to the restraunt!:")
print("here is the menu:")
print("  Pizza: Rs120,\nPasta: Rs200\nBurger: Rs90\nSalad: Rs70\nCoffee: Rs130\nTea: Rs20\nJuice: Rs50")
  #take order
#display the menu
order_total = 0

item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
  order_total += menu[item_1]
  print(f"Added {item_1} to your order. Total: Rs{order_total}")
else:
  print(f"{item_1} is not available in the menu.")
  
  

another_order = input("Do you want to order another item? (yes/no): ")
if another_order.lower() == "yes":
    item_2= input("Enter the name of the item you want to order: ")
    if item_2 in menu:
      order_total += menu[item_2]
      print(f"Added {item_2} to your order. Total: Rs{order_total}")
    else:
      print(f"{item_2} is not available in the menu.")

    print(f"Your final order total is Rs{order_total}.")