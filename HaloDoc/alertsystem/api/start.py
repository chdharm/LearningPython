import random
from threading import Thread, Lock
from datetime import datetime
from notification import notify_users
from config.notification_threshold import NOTIFICATION_THRESHOLD_TIMING, NOTIFICATION_THRESHOLD_COUNT, \
    NOTIFICATION_FLUSH_WAITING_TIME

EVENTS = {
    "CRITICAL": {
        "is_under_maintenance": False,
        "maintenance_start_time": datetime.now(),
        "events": [
            'time'
        ]
    },
    "INFO": {
        "is_under_maintenance": False,
        "maintenance_start_time": datetime.now(),
        "events": [
            'time'
        ]
    },
    "BLOKER": {
        "is_under_maintenance": False,
        "maintenance_start_time": datetime.now(),
        "events": [
            'time'
        ]
    },
    "WARNING": {
        "is_under_maintenance": False,
        "maintenance_start_time": datetime.now(),
        "events": [
            'time'
        ]
    }
}


def flush_older_events(flush_till, event_type, lock):
    with lock.acquire():
        events = EVENTS
        EVENTS[event_type.upper()].events = filter(lambda x: x <= flush_till, events[event_type.upper()].events)


def should_send_events(event_type, lock):
    datetime_now = datetime.now()
    flush_till = None
    if EVENTS[event_type.upper()].is_under_maintenance:
        flush_till = datetime_now
        thread = Thread(target=flush_older_events, args=(flush_till, lock))
        thread.start()
        return False
    eligible_events = filter(lambda x: x <= datetime_now and (datetime_now - x).total_seconds() >= 100,
                             EVENTS[event_type.upper()].events)
    if len(eleigible_events) > NOTIFICATION_THRESHOLD_COUNT:
        flush_till = datetime_now + datetime.datetime.combine(datetime_now, datetime.time(10, 23))
        thread = Thread(target=flush_older_events, args=(flush_till, lock))
        thread.start()
        return True


if __name__ == '__main__':
    lock = Lock()
    while True:
        try:
            _input = input().split(" ")
            if not _input:
                continue
            time = _input[0]
            event_type = _input[1]
            with lock.acquire():
                datetime_now = datetime.now()
                if not EVENTS[event_type.upper()].is_under_maintenance:
                    EVENTS[event_type.upper()].events.append(time)
                elif (datetime_now - maintenance_start_time).total_seconds() > NOTIFICATION_FLUSH_WAITING_TIME:
                    EVENTS[event_type.upper()] = {
                        "is_under_maintenance": False,
                        "maintenance_start_time": datetime_now,
                        "events": []
                    }

            if should_send_events(event_type, lock):
                new_thread = Thread(target=notify_users, args=(event_type,))
                new_thread.start()
                EVENTS[event_type.upper()] = {
                    "is_under_maintenance": True,
                    "maintenance_start_time": datetime_now,
                    "events": []
                }
        except:
            print("Error in processing")
            pass
