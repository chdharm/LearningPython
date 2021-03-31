class SLot:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.is_occupied = False  # Remove later if not useful

    def book(self):
        self.is_occupied = True

    def exit(self):
        self.is_occupied = False
