import json
import functools

def save_to_json(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "function_name": func.__name__,
                "parameters": {
                    "args": args,
                    "kwargs": kwargs
                },
                "result": result
            }
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            return result
        return wrapper
    return decorator

@save_to_json("result.json")
def add(a, b):
    return a + b

result = add(5, 7)
print("Результат:", result)
