import threading
import json


class CoffeeMachine:

    def __init__(self, outlets, ingredients):
        self.outlets = outlets
        self.ingredients = ingredients
        self.orders = 0
        self.lock = threading.RLock()

    def refill(self, ingredient, count):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += count

    def make_beverage(self, beverage):
        if self.orders == self.outlets:
            print ("Already maximum outlets acquired")
            return False

        self.orders += 1
        ingredients = beverage.ingredients

        self.lock.acquire()

        result = True

        print('----- making %s -----' % beverage.name)

        for ingredient, value in ingredients.items():
            if ingredient not in self.ingredients:
                print("Ingredient %s is not available" % ingredient)
                result = False
            elif self.ingredients[ingredient] < value:
                print("Ingredient %s is not available in sufficient quantity" % ingredient)
                result = False

        if not result:
            self.lock.release()

            self.orders -= 1
            return result

        for ingredient, value in ingredients.items():
            self.ingredients[ingredient] -= value

        self.lock.release()
        self.orders -= 1

        print("beverage %s is ready" % beverage.name)

        print('Ingredient Quantity left After Beverage')
        print(json.dumps(self.ingredients, indent=4))
        print('----- make beverage done -----')
        return True

