from datetime import datetime

def count_days_between(date_one: str, date_two: str) -> str:
    # datetime.strptime str p (parse) time '2024-03-04' -> datetime(year=2024, month=3, day=4)
    # datetime.strftime str f (format) time datetime(year=2024, month=3, day=4) -> '2024-03-04'
    # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    try:
        date_one = datetime.strptime(date_one, '%Y-%m-%d')
        date_two = datetime.strptime(date_two, '%Y-%m-%d')
    except ValueError:
        # print('Error!')
        return 0

    # https://docs.python.org/3/library/datetime.html#datetime.timedelta
    delta = date_one - date_two
    return abs(delta.days)

print(count_days_between('2024-01-01', '2024-03-01'))
print(count_days_between('2024.01.01', '2024.03.01'))