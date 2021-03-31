from floor import Floor


class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.floors = {}
        self.availablility = {

        }

    def add_floor(self, floor_no, availability):
        floor = Floor(floor_no)
        self.floors[floor.floor_no] = floor


    def remove_floor(self, floor_no):
        pass

    def get_availability(self):
        availability = {

        }
        for floor_no in self.floors.keys():
            floor = self.floors[floor_no]
            for slot in floor.slots:
                if not slot.is_occupied:
                    if availability.get(slot.type):
                        availability[slot.type]
                    else:
                        availability[slot.type]
                    availability.push({
                        floor_no: floor_no,
                        slot_no: slot.id,
                        category: slot.type
                    })



