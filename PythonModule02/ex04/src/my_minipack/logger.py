import time
import os

#... your definition of log decorator...
def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        username = os.getenv("USER")
        name_of_function = func.__name__.replace("_", " ").title()
        str = ""
        space_str = str + " " * (20 - len(name_of_function))
        unit = "s" if execution_time > 1 else "ms"
        with open("machine.log", "a") as machine_file:
            machine_file.write(f"({username})Running: {name_of_function}{space_str}[ exec-time = {execution_time:.3f} {unit} ]\n")
        return result
    return wrapper