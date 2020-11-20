# WRITE YOUR FUNCTIONS HERE

# 1.
def get_pet_shop_name(shop):
    return shop["name"]

# 2.
def get_total_cash(shop):
    return shop["admin"]["total_cash"]

# 3. & 4.
def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount

# 5. 
def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

# 6.
def increase_pets_sold(shop, num_pets):
    shop["admin"]["pets_sold"] += num_pets

# 7.
def get_stock_count(shop):
    return len(shop["pets"])

# 8. & 9.
def get_pets_by_breed(shop, breed):
    pet_list = []

    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
    return pet_list

# 10. & 11.
def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None

# 12.
def remove_pet_by_name(shop, pet_name):
    pets = shop["pets"]

    for pet in pets:
        if pet["name"] == pet_name:
            pets.remove(pet)

# 13.
def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

# 14.
def get_customer_cash(customer):
    return customer["cash"]

# 15.
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

# 16.
def get_customer_pet_count(customer):
    return len(customer["pets"])

# 17.
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# 18., 19. & 20.
def customer_can_afford_pet(customer, new_pet):
    if get_customer_cash(customer) >= new_pet["price"]:
        return True
    else:
        return False

# 21., 22. & 23.
def sell_pet_to_customer(shop, desired_pet, customer):
    # Check desired pet is in the shop
    if not desired_pet:
        return "Pet not found"
    else:
        pet_price = desired_pet["price"]

        # Check customer can afford the pet
        if customer_can_afford_pet(customer, desired_pet) == True:
            
            # If they can, proceed with purchase
            # Remove cash from customer
            remove_customer_cash(customer, pet_price)
            # Add cash to shop
            add_or_remove_cash(shop, pet_price)
            # Add pet to customer
            add_pet_to_customer(customer, desired_pet)
            # Remove pet from shop & increase pets sold
            remove_pet_by_name(shop, desired_pet) # Not in test but presumably only 1 of each pet in stock?
            increase_pets_sold(shop, 1)
        
        # Error if cannot afford
        else: 
            return "Customer cannot afford pet"
