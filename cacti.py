
# Decorator function to count the number of cacti in a 2-D array
def cacti_number(original_function):
    def wrapper(array):
        # Check for invalid inputs
        if not isinstance(array, list) or not array:
            raise ValueError("Invalid input. Please provide a non-empty 2-D array.")

        # Check if the array is a perfect rectangle or square
        rows = len(array)
        cols = len(array[0])
        for row in array:
            if len(row) != cols:
                raise ValueError("Invalid input. Not a perfect rectangle or square.")

        # Count the number of cacti
        count = 0
        for row in array:
            for element in row:
                if element == 1:
                    count += 1

        return count

    return wrapper
