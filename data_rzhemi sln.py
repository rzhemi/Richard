#use this list of menu items
menu_items = [
'D1 ​​SODA 3',
'D2 ​​LEMONADE 3',
'D3 ​​TEA 2',
'D4 WATER 0',
'A1 ​​POTATO_CAKES 7',
'A2 ​​SPINACH_DIP 5',
'A3 ​​OYSTERS 13',
'A4 ​​CHEESE_FRIES 4',
'A5 ​​ONION_RINGS 7',
'S1 ​​COBB 14',
'S2 ​​CAESAR 13',
'S3 ​​GREEK 12',
'E1 ​​BURGER 16',
'E2 ​​PASTA 15',
'E3 ​​GNOCCHI​   14',
'E4 ​​GRILLED_STEAK_SANDWICH 17',
'T1 ​​CARAMEL_CHEESECAKE 13',
'T2 ​​APPLE_COBBLER 12',
'T3 ​​BROWNIE_SUNDAE 9',
'T4 ​​FLAN 8'
]

drink_items = ['D1', 'D2',  'D3', 'D4']
appetizer_items = ['A1', 'A2',  'A3', 'A4', 'A5']
salad_items = ['S1', 'S2', 'S3']
entree_items = ['E1', 'E2',  'E3', 'E4']
dessert_items =['T1', 'T2',  'T3', 'T4']


price_of_category_list ={
    "drink_items" :5,
    "appetizer_items":6,
    "salad_items": 7,
    "entree_items":8,
    "dessert_items" :10,
    }
def categorize_menu_items (item_code):
 if item_code in drink_items:
     return "Drink", price_of_category_list, ["drink_items"]
 elif item_code in appetizer_items:
     return "Appetizer", price_of_category_list,["After dinner washdown"]
 elif item_code in salad_items:
     return "Salad", price_of_category_list, ["Salad_items"]
 elif  item_code in entree_items:
     return "Entree", price_of_category_list, ["entree_items"]
 elif item_code in dessert_items:
     return "dessert", price_of_category_list, ["dessert_items"]
 else:
     return "Invalid item code", 0
 

item_code = input("Enter menu items code")


category, price = categorize_menu_items(item_code)
if category == "Invalid item code":
    print(f"Item is a {category}. Price:$price")
else:
    print(f"{category}.Please enter a valid item code")


