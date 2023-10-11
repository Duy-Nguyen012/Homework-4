import datetime

def timestamp(original_function):
    def wrapper(*args, **kwargs):
        current_time = datetime.datetime.now()
        print(f"Timestamp: {current_time}")
        result = original_function(*args, **kwargs)
        return result
    return wrapper


