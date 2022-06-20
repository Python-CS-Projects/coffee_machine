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
    """Returns true if there is enough resources."""
    ingredients = coffee_type["ingredients"]

    for ingredient in ingredients:
        needed_ingredient = ingredients[ingredient]
        current_resource = resources[ingredient]

        if current_resource < needed_ingredient:
            return False

    return True


def make_coffee(coffee_type):
    # Remove the ingredients from the resources
    ingredients = coffee_type["ingredients"]

    for ingredient in ingredients:
        needed_ingredient = ingredients[ingredient]
        current_resource = resources[ingredient]
        resources[ingredient] -= needed_ingredient

    print("Here is your coffee!")


def get_payment():
    """Returns the total paid."""
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def process_payment(coffee):
    coffee_type = MENU[coffee]
    cost_of_coffee = coffee_type["cost"]

    print(f"Costs for a {coffee}: ${cost_of_coffee}")
    total_paid = get_payment()

    if total_paid >= cost_of_coffee:
        print("paid ✅")
        global profit
        profit += total_paid
        make_coffee(coffee_type)
    else:
        print(f"Sorry that's not enough money. Money refunded. ${total_paid} ❌")


def process_order(coffee):
    print(f"Processing: {coffee}")
    coffee_type = MENU[coffee]
    if check_resources(coffee_type):
        process_payment(coffee)
    else:
        print("Not enough resources ❌")


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

