from datetime import datetime

def get_days_from_today(date):
    try:
        date_random = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = date_random - today
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'."


print(get_days_from_today("2024-12-15"))  
print(get_days_from_today("13.13.2000"))  
