from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = CoffeeMaker()
payment = MoneyMachine()
check_menu = Menu()

is_on = True
while is_on:
    choice = input(f"What would you like? {check_menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        make_coffee.report()
        payment.report()
    else:
        item = check_menu.find_drink(choice)
        if make_coffee.is_resource_sufficient(item) and payment.make_payment(item.cost):
            make_coffee.make_coffee(item)




