from datetime import datetime, timedelta

users = [
    {'name': 'John', 'birthday': datetime(1985, 7, 13)},
    {'name': 'Jane', 'birthday': datetime(1995, 7, 12)},
    {'name': 'Bob', 'birthday': datetime(2000, 7, 10)},
    {'name': 'Alice', 'birthday': datetime(2001, 7, 8)},
    {'name': 'David', 'birthday': datetime(1999, 8, 4)},
    {'name': 'Eva', 'birthday': datetime(1997, 8, 5)},
    {'name': 'Mike', 'birthday': datetime(1990, 7, 9)},
    {'name': 'Anna', 'birthday': datetime(1991, 7, 14)},
    {'name': 'Tom', 'birthday': datetime(2002, 7, 11)},
]



def get_birthdays_per_week(users):
    current_datetime = datetime.now()
    start_period = (current_datetime + timedelta(5 - current_datetime.weekday())).date()

    end_period = (current_datetime + timedelta(12 - current_datetime.weekday())).date()
    start_of_week = start_period + timedelta() 

    congrats = {}

    for user in users:
        birthday = user['birthday'].date().replace(year=current_datetime.year)
        if start_period <= birthday <= end_period:
            if birthday.weekday() >= 5:
                birthday = start_of_week
            if congrats.get(birthday):
                congrats[birthday].append(user['name'])
            else:
                congrats[birthday] = [user['name']]

    sorted_dates = sorted(congrats.keys())
            
    for bd in sorted_dates:
        print(f'{bd.strftime("%A")}: {", ".join(congrats[bd])}')
            


if __name__ == "__main__":
    get_birthdays_per_week(users)
