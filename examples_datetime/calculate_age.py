from datetime import datetime

def calculate_age(birthdate: str) -> int:
    """ 
    Calculates persons age based on birthdate
        - birthdate: string birthdate of a person in format '%Y-%m-%d'

    throws ValueError: when date is in wrong format
    """
    try:
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError('Please enter date in format "%Y-%m-%d"')
    
    today = datetime.today().date()

    year_difference = today.year - birthdate.year
    # lesser_month_lesser_day = (today.month < birthdate.month and today.day < birthdate.day)
    # same_month_lesser_day = (today.month == birthdate.month and today.day < birthdate.day)
    # if lesser_month_lesser_day and same_month_lesser_day:
    #     year_difference -= 1
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        year_difference -= 1
    # return (today - birthdate).days // 365
    return year_difference


print(calculate_age('1996-04-19'))