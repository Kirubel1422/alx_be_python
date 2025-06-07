from datetime import datetime, timedelta

def display_current_datetime() -> datetime:
    return datetime.now()

def calculate_future_date(days: int) -> datetime:
    current_date = display_current_datetime()
    return current_date + timedelta(days=days)

current_date = display_current_datetime()
print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')

number_of_days = int(input("Enter the number of days to add to the current date: "))
future_date = calculate_future_date(number_of_days)

print(f'Future date: {future_date.strftime("%Y-%m-%d")}')
