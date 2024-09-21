# Define the list of cars and prices
luxury_cars = [
    ('Lamborghini', 200000),
    ('Ferrari', 250000),
    ('Porsche', 150000),
    ('Rolls Royce', 350000),
    ('Bentley', 300000)
]

def get_vehicle_information(car_name):
  
    for car, price in luxury_cars:
        if car.lower() == car_name.lower():
            return car, price
    return None  # If car not found

def display_vehicles():
    
    print("Available Luxury Cars:")
    for car, price in luxury_cars:
        print(f"{car}: ${price}")

# Example usage
if __name__ == "__main__":
    display_vehicles()
    
    car_name = input("Enter the car name to get its price: ")
    result = get_vehicle_information(car_name)
    
    if result:
        car, price = result
        print(f"The price of the {car} is ${price}.")
    else:
        print(f"Sorry, the {car_name} is not available.")
