import data

def get_item_information(item_code):
  
    for item in data.menu_items:
        item_number, item_name, item_price = item.split(' ')
        if item_number == item_code:
            return item_name.encode("ascii", "ignore").decode(), int(item_price)
    
    return None  

def display_items():
    
    print("Available Menu Items:")
    for item in data.menu_items:
        item_number, item_name, item_price = item.split(' ')
        print(f"{item_number}: {item_name} - ${item_price}")

    