def my_steps(n):
    if not (1 <= n <= 25):
        raise ValueError("Input out of bounds. n should be between 1 and 25 inclusive.")
    
    # Base cases
    if n <= 2:
        return n
    
    # Recursive case: the number of ways to reach step n is the sum of ways to reach step n-1 and n-2
    return my_steps(n - 1) + my_steps(n - 2)

