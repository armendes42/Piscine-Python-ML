import time
from random import randint
import os

#... your definition of log decorator...
def log(func):
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

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)