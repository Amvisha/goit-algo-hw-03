from datetime import datetime

def get_days_from_today() -> int:
    """
    Function returns an integer indicating the number of days from the given date to the current one

    Output:
    :return: integer
             A negative number if the specified date is in the future.
    """
    while True:
        given_date = input("Enter the date in the format 'YYYY-MM-DD' (e.g. '2020-10-09') ")

        try:
            given_date = datetime.strptime(given_date, '%Y-%m-%d').date()  # Converting a date string to a datetime object
            break

        except Exception as e: # Exception handling for incorrect date format
            print(e)

    today = datetime.today().date()  # Current date
    days_from_today = (given_date - today).days  # Difference between dates
    return days_from_today

result: int = get_days_from_today()
print(f"{result} days between today's date and the given date.")
