from app import add_branch, add_vehicle, get_available_vehicles, rent_vehicle

if __name__ == '__main__':
    add_branch('gachibowli', ['1 suv for Rs.12 per hour', '3 sedan for Rs.10 per hour', '3 bikes for Rs.20 per hour'])
    add_branch('kukatpally', ['3 sedan for Rs.11 per hour', '3 bikes for Rs.30 per hour', '4 hatch_back for Rs.8 per hour']);
    add_branch('miyapur', ['1 suv for Rs.11 per hour', '10 bikes for Rs.3 per hour', '3 sedan for Rs.10 per hour']);
    # add_vehicle('gachibowli', '1 sedan')
    # get_available_vehicles('gachibowli', time ,range)

    print(rent_vehicle('gachibowli', 'suv', '1', '2'))
    print(rent_vehicle('gachibowli', 'suv', '1', '2'))

    print(rent_vehicle('miyapur', 'suv', '1', '2'))
    add_vehicle('gachibowli', '1 suv')

    print(rent_vehicle('gachibowli', 'suv', '1', '2'))