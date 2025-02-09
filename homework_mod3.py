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
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()  # Converting a date string to a datetime object
        today = datetime.today().date()  # Current date
        days_from_today = (date - today).days  # Difference between dates
        return days_from_today

    except ValueError: # Exception handling for incorrect date format
        print("Invalid date format. Use 'YYYY-MM-DD' format.")
        return None



# Example of use
# date = "2021-10-09"
# result: int = get_days_from_today(date)
# print(f"Number of days from {date} to today: {result}.")
