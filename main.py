from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def order():
    end_ordering = False
    while end_ordering is not True:
        ordering = input(f"What would you like? ({menu.get_items()})").lower()
        variant = menu.find_drink(ordering)
        if variant is None:
            end_ordering = True
            print("Sorry, we don't have that in our coffee machine. Have a nice day!")
        elif variant.name == "report":
            print(f"{coffee_maker.report()}\n{money_machine.report()}")
        elif variant.name == "off":
            end_ordering = True
            print("Beep bop, turning off.")
        else:
            if money_machine.make_payment(variant.cost) is False:
                end_ordering = True
            else:
                coffee_maker.make_coffee(variant)
                end_ordering = True


order()
