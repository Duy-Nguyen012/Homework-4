import time

def timestamp(func):
    def wrapper(*args, **kwargs):
        current_time = time.ctime()
        print({current_time})
        result = func(*args, **kwargs)
        print(f"Decorated Content: {result}")
        return result
    return wrapper
@timestamp
def hi(): 
    print('hi')






