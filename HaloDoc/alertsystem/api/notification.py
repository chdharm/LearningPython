from sms import send_sms
from phone import call_user
from email import send_email
from config.alert_config import ALERT_CONFIG

def send_notification(notif_type, username, usercontacts):
    if notif_type == 'email' and usercontacts.get('email'):
        _email = usercontacts.get('email')
        send_email(_email, '___MSG___')
    elif notif_type == 'phone' and usercontacts.get('mobile'):
        call_user(usercontacts.get('mobile'), '___MSG___')
    elif notif_type == 'sms' and usercontacts.get('mobile'):
        send_sms(usercontacts.get('mobile'), '__MSG__')

def notify_users(event_type):
    try:
        users = ALERT_CONFIG[event_type.upper()].SUBSCRIBED
        types = ALERT_CONFIG[event_type.upper()].TYPES
        for notif_type in types:
            for user_name in users.keys():
                send_notification(notif_type, user_name, users[user_name])

    except:
        print("Error in sending notification")

