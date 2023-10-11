
# Decorator function to capitalize the result of the original function
def allcaps(original_function):
    def wrapper():
        result = original_function()
        if result is not None and isinstance(result, str):
            return result.upper()
        return result
    return wrapper


if __name__ == "__main__":
    @allcaps
    def greeting():
        return "hello world"

    print(greeting())  

