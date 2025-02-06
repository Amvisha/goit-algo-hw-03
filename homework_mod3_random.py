import random

def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list:
    """
        Generates a set of unique random numbers for a lottery ticket.

        Args:
         - min_number (int): The minimum possible number in the set (at least 1).
         - max_number (int): The maximum possible number in the set (at most 1000).
         - quantity (int): The number of numbers to choose from (a value between min and max).

        Returns:
         - list: A list of randomly selected, sorted numbers. Numbers in the set must not be repeated.
                 If the parameters do not meet the specified constraints, the function returns an empty list.
        """
    numbers = []
    if min_number < 1 or max_number > 1000 or not max_number - min_number >= quantity: # Checking the validity of input data
        return [] # Return an empty list

    for number in range(min_number, max_number+1): # Creating a list in the range from 'min_number' to 'max_number'
        numbers.append(number)
    numbers = random.sample(numbers, quantity) # Creating a list of length 'quantity' with unique elements chosen randomly
    numbers = sorted(numbers) # Create a new sorted list
    return numbers

lottery_numbers = get_numbers_ticket(1, 49, 5) # Example of using the function
print("Ваші лотерейні числа:", lottery_numbers)