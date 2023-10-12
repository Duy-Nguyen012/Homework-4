import datetime

def timestamp(func):
    def wrapper(*args, **kwargs):
        current_time = time.ctime()
        print(f"Timestamp: {current_time}")
        result = func(*args, **kwargs)
        print(f"Decorated Content: {result}")
        return result
    return wrapper





