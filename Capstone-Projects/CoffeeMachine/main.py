# Import required modules.
from machine_data import MENU, resources, logo
from os import system, name

# This function clear the console screen.
def clear():
    """This function clear the console screen."""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# This function checks the available resources are sufficient for the order.
def check_resource_available(user_choice):
    """This function checks the available resources are sufficient for the order.
    It returns True if all the recorsed are available in the machine. 
    Othewise it returns False."""

    for item in user_choice['ingredients']:
        if user_choice['ingredients'][item] >= resources[item]:
            print(f"\n\tSorry there is not enough {item}.")
            return False
        
    return True


# This function processes coins and 
# returns the total amount of dollar value inserted in terms of coins.
def process_coins():
    """Asks user to insert coins and returns the total dollar value of the inserted coins."""
    print("\nPlease insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    dollar_value = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    return dollar_value

# This function deducts the ingredients from the available resources and serves coffee. 
def make_coffee(option):
    """This function deducts the ingredients from the available resources and serves coffee."""
    user_choice = MENU[option]

    for item in user_choice['ingredients']:
        resources[item] -= user_choice['ingredients'][item]

    print(f"Here is your {option}. ☕️ Enjoy!")


#### Coffee Machine Program ####
def coffee_machine():
    """This is coffee machine program."""
    
    clear()
    print("\n\t\t\tWelcome to the Coffee Machine Interface!\n")
    print(logo)
    
    # Initialize variables.
    machine_on = True
    money = 0

    while machine_on:
        # Ask user for choices.
        option = input("What would you like? (espresso/latte/cappuccino): ")

        # Turn off the Coffee Machine by entering "off" to the prompt.
        if option == "off":
            machine_on = False
        # When user enters "report" to the prompt, a report should be generated that shows 
        # available resources.
        elif option == "report":
            print(f"\n\tWater: {resources['water']}ml\n\tMilk: {resources['milk']}ml\n\tCoffee: {resources['coffee']}gm\n\tMoney: ${money}\n")
        elif option in ["espresso", "latte", "cappuccino"]:
            user_choice = MENU[option]
          
            if check_resource_available(user_choice):
                inserted_dollar_value = process_coins()
              
                if inserted_dollar_value < user_choice['cost']:
                    print("\n\tSorry that's not enough money. Money refunded.")
                else:
                    change_value = round(inserted_dollar_value - user_choice['cost'], 2)
                    if change_value > 0:
                        print(f"\n\tHere is ${change_value} dollars in change.")
                    
                    money += user_choice['cost']
                    
                    make_coffee(option)
        else:
            print("\n\tWRONG OPTION !!\n")
            machine_on = False


if __name__ == '__main__':
    coffee_machine()