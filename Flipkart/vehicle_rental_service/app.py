from branch import Branch
from models.branchs import BRANCHES
from models.rentals import RENTALS

#Todo: Sorry dude, Time was less so syntax mistakes and was not able to test it

def add_branch(branch_name, branch_vehicle_details):
    branch = Branch(branch_name)
    branch.add_vehicles(branch_vehicle_details)
    # return BRANCHES

def add_vehicle(branch, vehicles):
    branch = BRANCHES[branch]
    branch.add_extra_vehicle(vehicles)

def is_booked(booking, from_date_time, to_date_time):
    startDate, endDate, price = booking
    if from_date_time < startDate and startDate < to_date_time and to_date_time < endDate:
        True
    if startDate < from_date_time and from_date_time < endDate and endDate < to_date_time:
        True
    if from_date_time < startDate and endDate < to_date_time:
        True
    if startDate < from_date_time and to_date_time < endDate:
        True
    return False


def rent_vehicle(branch_name, vehicle_type, from_date_time, to_date_time):
    branch_rentals = RENTALS[branch_name] if RENTALS.get(branch_name) else None
    branch_all_vehicles = BRANCHES[branch_name].vehicles
    for v_type in branch_all_vehicles.keys():
        if v_type == vehicle_type:
            total_count = branch_all_vehicles[v_type]['count']
            already_booked = 0
            if branch_rentals is not None:
                for branch_rental_vehicle in branch_rentals.keys():
                    all_bookings = branch_rentals[branch_rental_vehicle]['bookings']
                    for booking in all_bookings:
                        is_booked_flag = is_booked(booking, from_date_time, to_date_time)
                        if is_booked_flag:
                            already_booked += 1
            if total_count > already_booked:
                if not RENTALS.get(branch_name):
                    RENTALS[branch_name] = {}
                if not RENTALS[branch_name].get(vehicle_type):
                    RENTALS[branch_name][vehicle_type] = { "bookings": [] }
                RENTALS[branch_name][vehicle_type]['bookings'].append(
                    [from_date_time, to_date_time, BRANCHES[branch_name].vehicles[vehicle_type]['price']])
                return "Booking Successfull"
    return "Unsuccessfull"


def get_available_vehicles(branch_name, from_date_time, to_date_time):
    branch_rentals = RENTALS[branch_name]
    branch_all_vehicles = BRANCHES[branch_name].vehicles
    for vehicle in branch_all_vehicles:
        total_count = vehicle.count
        already_booked = 0
        for branch_rental_vehicle in branch_rentals[vehicle.vehicle_type]:
            all_bookings = branch_rental_vehicle.bookings
            for booking in all_bookings:
                is_booked = is_booked(booking, from_date_time, to_date_time)
                if is_booked:
                    already_booked += 1
        if total_count > already_booked:
            print('{} {} available for RS.{}'.format(total_count - already_booked, vehicle.vehicle_type, vehicle.price))


def print_system_view(from_date_time, to_date_time):
    for branch_name in RENTALS:
        # print("Branch Name:", branch_name, ":")
        branch_rentals = RENTALS[branch_name]
        branch_all_vehicles = BRANCHES[branch_name].vehicles
        for vehicle in branch_all_vehicles:
            total_count = vehicle.count
            already_booked = 0
            for branch_rental_vehicle in branch_rentals[vehicle.vehicle_type]:
                all_bookings = branch_rental_vehicle.bookings
                for booking in all_bookings:
                    is_booked = (is_booked, from_date_time, to_date_time)
                    if is_booked:
                        already_booked += 1
            if total_count > already_booked:
                if total_count == already_booked:
                    print("all {} are booked out of {}.".format(vehicle.vehicle_type, total_count))
                else:
                    print("{} {} are booked out of {}.".format(already_booked, vehicle.vehicle_type, total_count))
