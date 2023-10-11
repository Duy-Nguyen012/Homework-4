import datetime

def timestamp(original_function):
    def wrapper(*args, **kwargs):
        current_time = datetime.datetime.now()
        print(f"Timestamp: {current_time}")
        result = original_function(*args, **kwargs)
        return result
    return wrapper

# Example usage:
if __name__ == "__main__":
    @timestamp
    def log_message(message):
        print(message)

    log_message("hi")
