def is_leap_year(year):
    if not(year % 4) and (not(year % 400) or year % 100):
        return True
    return False

