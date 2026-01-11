def limit_calls(max_calls):
    def decorator(func):
        call = 0
        def wrapper():
            nonlocal call
            if call < max_calls:
                func()
                call += 1
            else:
                print(f"Error: Function '{func.__name__}' has been called too many times.")
        return wrapper
    return decorator

@limit_calls(3)
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()
say_hello()
