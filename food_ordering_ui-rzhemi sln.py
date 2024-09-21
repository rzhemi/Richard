#user interface to the main menu
import data
import functions

def show_main_menu():
  diner_name = input("Please enter your name:")
  print(f"Welcome to the Diner,{diner_name}")

  while True:
    print("Your name diner")
    print("__________Main Menu_______")
    print('N - start a new order')
    print('X - close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
    elif user_menu_choice in 'Nn':
      print('New order')
    else:
      make_order(user_menu_choice.upper())  

  def new_order():
    print("Starting a new oder...")
    current_order = []
    while True:
      show_main_menu
      menu_choice = input('Enter item code to add to your order type or Type D for done')

      if menu_choice == 'D':
        break
      else:
        add_item_to_order(menu_choice,current_order))

print(f"Order complete:{current_order}")
def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  print("Returning to main menu...")

def show_menu():
  print("__________Menu__________")
    print("Drinks: D1 - Coffee ($2), D2 - Tea ($1.5)")
    print("Appetizers: A1 - Garlic Bread ($3), A2 - Salad ($4)")
    print("Entrees: E1 - Steak ($20), E2 - Pasta ($15)")
    print("Desserts: DS1 - Ice Cream ($5), DS2 - Cake ($6)")
    print("________________________")

def add_item_to_order(menu_choice, current_order):
  
    item_info = functions.get_item_information(menu_choice)
    
    if item_info:
        current_order.append(item_info)
        print(f"Added {item_info['name']} to the order - ${item_info['price']}")
    else:
        print(f"Item with code {menu_choice} not found.")



def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    print(functions.get_item_information('D1'))
    #show_main_menu()


