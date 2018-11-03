#Tentative Response:---
missing_keys=[]
missingval=[]
dict1={
    "txnID": "172275524",
    "totalFare": 625,
    "tempBookingKey": "REDBUS::12304408455328002|10103473|2018-10-22",
    "respCode": "SUCCESS",
    "errorCode": "SUCCESS",
    "commonFrBrkUp": {
        "totalFare": 625,
        "respCode": "SUCCESS",
        "commonFrBreakUp": {
            "rtInformation": {
                "serviceStartTime": "18:30",
                "serviceStartDate": "22-Oct-2018 00:00",
                "serviceNo": "712",
                "serviceName": "MANALI DEHRADUN",
                "platformNo": "",
                "noOfchilds": "0",
                "noOfadults": "1",
                "journeyDateStr": "22-Oct-2018 00:00",
                "destinationName": "DEHRADUN",
                "departTime": "22-Oct-2018 20:15",
                "bookingId": "172275524",
                "boardingPoint": "KULLU",
                "arriveTime": "23-Oct-2018 11:30"
            },
            "paxArr": {
                "paxArr": [
                    {
                        "paxStNo": "46",
                        "paxName": "TestA",
                        "paxAge": "25.0",
                        "customerPriceBreakUp": {
                            "customerPriceBreakUp": [
                                {
                                    "value": 590,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 590,
                                    "componentName": "BASIC_FARE",
                                    "cancellationHandling": "CANCELLATION_POLICY"
                                },
                                {
                                    "value": 11,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 11,
                                    "componentName": "LEVIES_CHARGES",
                                    "cancellationHandling": "FULLY_REFUNDED"
                                },
                                {
                                    "value": 14,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 14,
                                    "componentName": "TOLL_FEE",
                                    "cancellationHandling": "FULLY_REFUNDED"
                                },
                                {
                                    "value": 10,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 0,
                                    "componentName": "SERVICE_FEE",
                                    "cancellationHandling": "NOT_REFUNDED"
                                },
                                {
                                    "value": 0,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 0,
                                    "componentName": "RESERVATION_FEE",
                                    "cancellationHandling": "NOT_REFUNDED"
                                },
                                {
                                    "value": 0,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 0,
                                    "componentName": "DISCOUNT",
                                    "cancellationHandling": "NOT_REFUNDED"
                                },
                                {
                                    "value": 625,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 604,
                                    "componentName": "TOTAL_FARE",
                                    "cancellationHandling": "CANCELLATION_POLICY"
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "commission": 0,
        "commPerCentage": 0
    },
    "commission": 24.6,
    "commPerCentage": 4
}
dict2={
    "txnID": "172275524",
    "totalFare": 625,
    "tempBookingKey": "REDBUS::12304408455328002|10103473|2018-10-22",
    "respCode": "SUCCESS",
    "errorCode": "SUCCESS",
    "commonFrBrkUp": {
        "totalFare": 625,
        "respCode": "SUCCESS",
        "commonFrBreakUp": {
            "rtInformation": {
                "serviceStartTime": "18:30",
                "serviceStartDate": "22-Oct-2018 00:00",
                "serviceNo": "712",
                "serviceName": "MANALI DEHRADUN",
                "platformNo": "",
                "noOfchilds": "0",
                "noOfadults": "1",
                "journeyDateStr": "22-Oct-2018 00:00",
                "destinationName": "DEHRADUN",
                "departTime": "22-Oct-2018 20:15",
                "bookingId": "172275524",
                "boardingPoint": "KULLU",
                "arriveTime": "23-Oct-2018 11:30"
            },
            "paxArr": {
                "paxArr": [
                    {
                        "paxStNo": "46",
                        "paxName": "TestA",
                        "paxAge": "25.0",
                        "customerPriceBreakUp": {
                            "customerPriceBreakUp": [
                                {
                                    "value": 590,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 590,
                                    "componentName": "BASIC_FARE",
                                    "cancellationHandling": "CANCELLATION_POLICY"
                                },
                                {
                                    "value": 11,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 11,
                                    "componentName": "LEVIES_CHARGES",
                                    "cancellationHandling": "FULLY_REFUNDED"
                                },
                                {
                                    "value": 14,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 14,
                                    "componentName": "TOLL_FEE",
                                    "cancellationHandling": "FULLY_REFUNDED"
                                },
                                {
                                    "value": 10,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 0,
                                    "componentName": "SERVICE_FEE",
                                    "cancellationHandling": "NOT_REFUNDED"
                                },
                                {
                                    "value": 0,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 0,
                                    "componentName": "RESERVATION_FEE",
                                    "cancellationHandling": "NOT_REFUNDED"
                                },
                                {
                                    "value": 0,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 0,
                                    "componentName": "DISCOUNT",
                                    "cancellationHandling": "NOT_REFUNDED"
                                },
                                {
                                    "value": 625,
                                    "type": "NON_DISCOUNT",
                                    "refundableValue": 604,
                                    "componentName": "TOTAL_FARE",
                                    "cancellationHandling": "CANCELLATION_POLICY"
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "commission": 0,
        "commPerCentage": 0
    },
    "commission": 24.6,
    "commPerCentage": 4
}
def compare(d1,d2):
    all_keys=d1.keys()
    all_keys2=d2.keys()
    for k in all_keys:
        if k not in all_keys2:
            missing_keys.append(k)
            continue
        elif type(d1[k])==int or type(d1[k])==str or type(d1[k])==float:
            if k not in all_keys2:
                missing_keys.append(k)
                continue
        elif type(d1[k]==list):
            for ele in d1[k]:

        elif type(d1[k]==dict):
            pass



if __name__=='__main__':
     dict1.keys()