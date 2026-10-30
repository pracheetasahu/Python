def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper

@uppercase_decorator
def get_message():
    return "welcome to python programming"

print(get_message())
