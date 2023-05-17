spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    foods=[food.get("name") for food in spicy_foods]
    return foods
    pass

def get_spiciest_foods(spicy_foods):
    all_foods_above5=[food for food in spicy_foods if food.get("heat_level")>5]
    return all_foods_above5
    pass

def print_spicy_foods(spicy_foods):
    
    for food in spicy_foods:
        result = ""
        name = food.get("name")
        cuisine = food.get("cuisine")
        heat_level = food.get("heat_level")
        heat_level_emoji = "🌶" * heat_level
        result += f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}"
        print(result)


print(print_spicy_foods(spicy_foods))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
     return None
     pass

def print_spiciest_foods(spicy_foods):
     
     for food in spicy_foods:
        result = ""
        name = food.get("name")
        cuisine = food.get("cuisine")
        heat_level = food.get("heat_level")
        if heat_level>5:
            heat_level_emoji = "🌶" * heat_level
            result += f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}"
            print(result)
     pass

def get_average_heat_level(spicy_foods):
    total_heat = sum(food.get("heat_level") for food in spicy_foods)
    num_foods = len(spicy_foods)
    average_heat = total_heat / num_foods
    return average_heat
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
