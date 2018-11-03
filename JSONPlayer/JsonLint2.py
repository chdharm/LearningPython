import re,json
def compareJson(d1,d2):
    uni1=[]
    uni2=[]
    common=[]
    commondiffval=[]
    all_keys1=d1.keys()
    all_keys2=d2.keys()
    for key in all_keys1:
        if key not in all_keys2:
            uni1.append(key)
        elif d1[key]==d2[key]:
            common.append(key)
        elif d1[key]!=d2[key]:
            commondiffval.append(key)
    for key in all_keys2:
        if key not in all_keys1:
            uni2.append(key)

if __name__=='__main__':
    coming_json1={
	"success": True,
	"data": {
		"ToCityId": 7774,
		"FromCityId": 5334,
		"Buses": [{
			"NonRefundable": False,
			"MTicket": True,
			"CompanyId": 13311,
			"ProvCompId": 0,
			"ProvId": 15,
			"RouteBusId": 1,
			"BusType": {
				"IsAC": "NON_AC",
				"Seating": "SEATER",
				"Make": "NORMAL",
				"Axle": "SINGLE_AXLE",
				"Axel": "SINGLE_AXLE"
			},
			"Pickups": [{
				"PickupTime": "2018-09-30 14:10:00",
				"PickupArea": "",
				"PickupName": "Private bus booking counter , old bus stand , jeypore - 9439801078",
				"PickupCode": "58106"
			}],
			"Dropoffs": [{
				"DropoffTime": "2018-09-30 14:25:00",
				"DropoffName": "Rondapali",
				"DropoffCode": "120048"
			}],
			"Canc": [{
					"Amt": 0,
					"Pct": 80,
					"Mins": 0
				},
				{
					"Amt": 0,
					"Pct": 60,
					"Mins": 30
				},
				{
					"Amt": 0,
					"Pct": 30,
					"Mins": 120
				},
				{
					"Amt": 0,
					"Pct": 20,
					"Mins": 480
				},
				{
					"Amt": 0,
					"Pct": 10,
					"Mins": 1440
				}
			],
			"Amenities": [],
			"BusStatus": {
				"Availability": 36,
				"RouteBusId": 1,
				"BaseFares": [
					6,
					5
				],
				"DiscFares": [
					5,
					0
				],
				"APICharge": 1.8,
				"ServiceTax": 0
			},
			"DisplayBusType": "Non A/C, Seater",
			"Visibility": True,
			"CommPct": 0,
			"HasDiscount": False,
			"DiscountPct": 0,
			"DiscountAmt": 0,
			"ToName": "Rondapali",
			"FromName": "Jeypore",
			"ChartCode": "Q4GLJlJyiv0yEyeiFqkNkw==|YDSKCszVav7ApIPFpsyNyg==",
			"Duration": "0:15",
			"BusLabel": "3X1(41) NAC Seater  Ashok leyland",
			"CompanyName": "Gupta Travels",
			"ArrTime": "2018-09-30 14:25:00",
			"DeptTime": "2018-09-30 14:10:00",
			"TripId": "42361"
		}],
		"AllAmenities": [
			"Blanket",
			"Water_Bottle",
			"Central_TV",
			"WiFi",
			"Toilet",
			"Charging_Point",
			"Personal_TV",
			"Snacks",
			"GPS",
			"Newspaper",
			"Emergency_Exit",
			"Facial_Tissues",
			"Fire_Extinguisher",
			"Hammer",
			"Reading_Light",
			"Pillow",
			"Headsets",
			"Vomiting_Bag",
			"Novel",
			"Heater",
			"CCTV",
			"Fan",
			"Water_Bottle_Holder",
			"First_Aid_Box"
		],
		"TotalAvailSeats": 36,
		"JourneyDate": "2018-09-30",
		"ToCityName": "Rondapali",
		"FromCityName": "Jeypore"
	}
}
    coming_json2 = {
        "success": True,
        "data": {
            "ToCityId": 7774,
            "FromCityId": 5334,
            "Buses": [{
                "NonRefundable": False,
                "MTicket": True,
                "CompanyId": 13311,
                "ProvCompId": 0,
                "ProvId": 15,
                "RouteBusId": 1,
                "BusType": {
                    "IsAC": "NON_AC",
                    "Seating": "SEATER",
                    "Make": "NORMAL",
                    "Axle": "SINGLE_AXLE",
                    "Axel": "SINGLE_AXLE"
                },
                "Pickups": [{
                    "PickupTime": "2018-09-30 14:10:00",
                    "PickupArea": "",
                    "PickupName": "Private bus booking counter , old bus stand , jeypore - 9439801078",
                    "PickupCode": "58106"
                }],
                "Dropoffs": [{
                    "DropoffTime": "2018-09-30 14:25:00",
                    "DropoffName": "Rondapali",
                    "DropoffCode": "120048"
                }],
                "Canc": [{
                    "Amt": 0,
                    "Pct": 80,
                    "Mins": 0
                },
                    {
                        "Amt": 0,
                        "Pct": 60,
                        "Mins": 30
                    },
                    {
                        "Amt": 0,
                        "Pct": 30,
                        "Mins": 120
                    },
                    {
                        "Amt": 0,
                        "Pct": 20,
                        "Mins": 480
                    },
                    {
                        "Amt": 0,
                        "Pct": 10,
                        "Mins": 1440
                    }
                ],
                "Amenities": [],
                "BusStatus": {
                    "Availability": 36,
                    "RouteBusId": 1,
                    "BaseFares": [
                        6,
                        5
                    ],
                    "DiscFares": [
                        5,
                        0
                    ],
                    "APICharge": 1.8,
                    "ServiceTax": 0
                },
                "DisplayBusType": "Non A/C, Seater",
                "Visibility": True,
                "CommPct": 0,
                "HasDiscount": False,
                "DiscountPct": 0,
                "DiscountAmt": 0,
                "ToName": "Rondapali",
                "FromName": "Jeypore",
                "ChartCode": "Q4GLJlJyiv0yEyeiFqkNkw==|YDSKCszVav7ApIPFpsyNyg==",
                "Duration": "0:15",
                "BusLabel": "3X1(41) NAC Seater  Ashok leyland",
                "CompanyName": "Gupta Travels",
                "ArrTime": "2018-09-30 14:25:00",
                "DeptTime": "2018-09-30 14:10:00",
                "TripId": "42361"
            }],
            "AllAmenities": [
                "Blanket",
                "Water_Bottle",
                "Central_TV",
                "WiFi",
                "Toilet",
                "Charging_Point",
                "Personal_TV",
                "Snacks",
                "GPS",
                "Newspaper",
                "Emergency_Exit",
                "Facial_Tissues",
                "Fire_Extinguisher",
                "Hammer",
                "Reading_Light",
                "Pillow",
                "Headsets",
                "Vomiting_Bag",
                "Novel",
                "Heater",
                "CCTV",
                "Fan",
                "Water_Bottle_Holder",
                "First_Aid_Box"
            ],
            "TotalAvailSeats": 36,
            "JourneyDate": "2018-09-30",
            "ToCityName": "Rondapali",
            "FromCityName": "Jeypore"
        }
    }
print "------------------------->"
json_string1=json.dumps(coming_json1)
print type(json_string1)
print json_string1
print "-------------------------->"
json_string2=json.dumps(coming_json2)
print type(json_string2)
print json_string2

#Getting the matching one

#Getting the non-maching present only in 1

#Getting the non-maching present only in 2

