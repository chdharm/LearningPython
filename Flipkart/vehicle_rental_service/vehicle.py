class Vehicle:
    def __init__(self, vehicle_detail, branch_name):
        count, vehicle_type, price = self.get_price_type_count(vehicle_detail)
        self.vehicle_type = vehicle_type
        self.count = count
        self.price = price
        # self.branch_name = branch_name

    def get_price_type_count(self, vehicle_detail):
        vehicle_infos = vehicle_detail.split()
        count = int(vehicle_infos[0])
        type = vehicle_infos[1]
        price = int(vehicle_infos[3].split('.')[1])
        return [count, type, price]
