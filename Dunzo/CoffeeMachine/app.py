import json
from config import CONFIG_JSON
from c_machine import CoffeeMachine
from beverage import Beverage

if __name__ == '__main__':
    json_data = CONFIG_JSON
    machine = json_data['machine']
    outlets = machine['outlets']
    outlet_count = outlets['count_n']
    items = machine['total_items_quantity']
    beverages = machine['beverages']

    beverage_list = list()

    for beverage in beverages:
        beverage_list.append(Beverage(beverage, beverages[beverage]))

    coffee_machine = CoffeeMachine(outlet_count, items)

    for beverage in beverage_list:
        coffee_machine.make_beverage(beverage)

    water = Beverage('wagter', {
        "hot_water": 100
    })

    coffee_machine.make_beverage(water)

    raw_tea = Beverage('raw_tea', {
        'sugar_syrup': 30,
        'tea_leaves_syrup': 30
    })

    coffee_machine.make_beverage(raw_tea)
