from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def is_maintanance(user_input: str) -> None:
    """Takes in command from user,
    turns off the coffee machine for maintanance"""
    if user_input.lower() == "off":
        exit("Shutting down for maintanance.")


def machine_report(user_input: str, coffee_maker: CoffeeMaker, money_machine: MoneyMachine):
    """takes in user input, if report evoked, prints machine stats"""
    if user_input == "report":
        money_machine.report()
        coffee_maker.report()
        return True


coffee_maker_loc_01 = CoffeeMaker()
menu_loc_01 = Menu()
money_machine_loc_01 = MoneyMachine()

while True:
    print("Fancy a cup of coffee?")
    print(f"Here are the options: {menu_loc_01.get_items()}")

    user_selection = input("type your selection: ").lower()
    is_maintanance(user_selection)
    if machine_report(user_selection, coffee_maker_loc_01, money_machine_loc_01):
        continue

    chosen_coffee = menu_loc_01.find_drink(user_selection)
    if not chosen_coffee:
        continue

    if not coffee_maker_loc_01.is_resource_sufficient(chosen_coffee):
        continue

    print(f"{chosen_coffee.name} price: {money_machine_loc_01.CURRENCY} {chosen_coffee.cost}")
    if not money_machine_loc_01.make_payment(chosen_coffee.cost):
        continue

    coffee_maker_loc_01.make_coffee(chosen_coffee)
