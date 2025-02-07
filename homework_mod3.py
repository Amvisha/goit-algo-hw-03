from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Function returns an integer indicating the number of days from the given date to the current one

    Input:
    :param date: string     Date in 'YYYY-MM-DD' format.

    Output:
    :return: integer
             A negative number if the specified date is in the future.
    """
    while True:
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()  # Converting a date string to a datetime object
            break

        except Exception as e: # Exception handling for incorrect date format
            print(e)

    today = datetime.today().date()  # Current date
    days_from_today = (date - today).days  # Difference between dates
    return days_from_today

# Example of use
# result: int = get_days_from_today("2021-10-09")
# print(f"{result} days between today's date and the given date.")
