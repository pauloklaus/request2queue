from datetime import datetime

def is_datetime_valid(check_datetime: str) -> bool:
    datetime_mask = "%Y-%m-%dT%H:%M:%S"
    try:
        datetime.strptime(check_datetime, datetime_mask)
        return True
    except:
        return False
