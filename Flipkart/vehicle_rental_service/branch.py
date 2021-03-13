from vehicle import Vehicle
from models.branchs import BRANCHES


class Branch:
    def __init__(self, branch_name):
        self.name = branch_name
        self.vehicles = {}
        BRANCHES[self.name] = self

    def add_vehicles(self, vehicles_details):
        for vehicle_detail in vehicles_details:
            vehicle = Vehicle(vehicle_detail, self.name)
            if self.vehicles.get(vehicle.vehicle_type):
                self.vehicles[vehicle.vehicle_type]['count'] += vehicle['count']
            else:
                self.vehicles[vehicle.vehicle_type] = {
                    "count": vehicle.count,
                    "price": vehicle.price
                }

    def add_extra_vehicle(self, vehicle_detail):
        count, vehicle_type = vehicle_detail.split()
        self.vehicles[vehicle_type]['count'] += int(count)
