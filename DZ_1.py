from datetime import datetime

def get_days_from_today(date):
    date_random = datetime.strptime(date, '%Y-%m-%d').date()
    today = datetime.today().date()
    delta = date_random - today
    return delta.days


print(get_days_from_today("2021-10-09"))
