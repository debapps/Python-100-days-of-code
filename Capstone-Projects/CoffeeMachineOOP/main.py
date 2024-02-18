from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

logo = """
     )))
    (((
  +-----+
  |     |]
  `-----'    
___________
`---------'
"""

def coffee_machine_program():
    # Define all the objects.
    menu = Menu()
    coffee_machine = CoffeeMaker()
    money_process = MoneyMachine()

    print(logo)
    
    is_machine_on = True
    while is_machine_on:
        user_choice = input(f"\nWhat would you like? {menu.get_items()}: ")

        if user_choice == "off":
            is_machine_on = False
        elif user_choice == "report":
            print("\n")
            coffee_machine.report()
            money_process.report()
        else:
            drink = menu.find_drink(user_choice)
            if drink and coffee_machine.is_resource_sufficient(drink) and money_process.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)


if __name__ == "__main__":
    coffee_machine_program()