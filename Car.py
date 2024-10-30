class Car:
    def __init__(self, model, year):
        self.model = model
        self._year = year
        self.__engine_status = False

    # Public method
    def start_car(self):
        if not self.__engine_status:
            self.__engine_status = True
            print(f"{self.model} is now started.")
        else:
            print(f"{self.model} is already running.")

    # Public method to stop the car
    def stop_car(self):
        if self.__engine_status:
            self.__engine_status = False
            print(f"{self.model} has been turned off.")
        else:
            print(f"{self.model} is already off.")

    # Protected method (for internal or subclass use)
    def _get_year(self):
        return self._year

    # Private method (for internal class use only)
    def __check_engine(self):
        return "Engine is running" if self.__engine_status else "Engine is off"

    # Public method to access private method for diagnostics
    def diagnostics(self):
        print(self.__check_engine())


# Usage example
car = Car("Tesla", 2023)

# Accessing public attributes and methods
print(car.model)  # Accessible
car.start_car()  # Accessible
car.diagnostics()  # Accessible

# Trying to access protected attribute (not recommended but accessible)
print(car._year)  # Accessible but should only be used within the class or subclass

# Trying to access private attribute directly (will raise AttributeError)
# print(car.__engine_status)  # Not accessible directly

# Accessing private method (will raise AttributeError)
# car.__check_engine()        # Not accessible directly

# Use the public method to stop the car
car.stop_car()