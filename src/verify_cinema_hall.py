import re

def verify_cinema_hall(hall_name, hall_height, hall_length):
    # Hall name: allow alphanumeric and spaces only
    if not isinstance(hall_name, str) or not re.match(r'^[A-Za-z0-9 ]+$', hall_name):
        return False
    # Height and length: must be integers and positive
    if not isinstance(hall_height, int) or hall_height < 0:
        return False
    if not isinstance(hall_length, int) or hall_length < 0:
        return False
    return True