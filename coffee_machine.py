MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machineOn = True
availableCoffeeTypes = ["espresso", "latte", "cappuccino"]


def check_resources(coffee_type):
    print(f"Checking resources for: {coffee_type}")
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    ingredients = coffee_type["ingredients"]
    print(ingredients)
    return True


def make_coffee(coffee_type):
    print(f"Making: {coffee_type}")


def process_order(coffee):
    print(f"Processing: {coffee}")
    coffee_type = MENU[coffee]
    if check_resources(coffee_type):
        make_coffee(coffee)
    else:
        print("Not enough resources")


while machineOn:
    # 1.Ask costumer the following:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # 2.Here we check the customer answer
    if choice == "off":
        machineOn = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    elif choice in availableCoffeeTypes:
        process_order(choice)

