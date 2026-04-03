#create a menu of 4 items for a cafe
menu= ["banana", "coffee", "tea", "cake"]
#create a dictionary called stock with the stock value of menu items
stock_menu = {"banana": 4, 
              "coffee": 5,
              "tea": 5,
              "cake": 7}
#dictionary called price that should contain the prices for each item on your menu
price_menu = {"banana": 1.50,
              "coffee": 5.00,
              "tea": 3.00,
              "cake": 6.00}
#calculate the total worth of the stock in the café and then store the results inside a variable called total_stock
#index the stock and price dictionaries to calculate the value of each item in the menu and then sum the total value of all items in the menu to get the total worth of the stock in the café
for item in menu:
    item_value = (stock_menu[item] * price_menu[item])
    print(item_value)
total_stock = sum(stock_menu[item] * price_menu[item] for item in menu)
print(total_stock)
