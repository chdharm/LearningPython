from slot import SLot
from config.categories import CATEGORIES


class Floor:
    def __init__(self, f_no):
        self.floor_no = f_no
        self.CATEGORIES = CATEGORIES

    def add_slot(self, id, type):
        slot = SLot(id, type)
        self.CATEGORIES[slot.type].slot.push(slot.id)

    def remove_slot(self, type):
        self.CATEGORIES[type].slot

