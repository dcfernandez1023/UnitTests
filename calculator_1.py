class Calculator():
    # constructor
    # if initial_calculation is not of type int or float, set last_calculation to 0
    # if initial_calculation is valid, set it to 0 by default, or the specified value of initial_calculation
    def __init__(self, initial_calculation=0):
        if not self.__is_valid_input(initial_calculation):
            initial_calculation = 0
        self.__last_calculation = initial_calculation

    # getter
    def get_last_calculation(self):
        return self.__last_calculation

    # add function
    # if addend1 or addend2 are not of type int or float, returns "INVALID INPUT"
    # if addend2 = 0, returns last_calculation + addend1
    # otherwise returns addend1 + addend2
    def add(self, addend1, addend2=0):
        if not self.__is_valid_input(addend1) or not self.__is_valid_input(addend2):
            return "INVALID INPUT"
        if addend2 == 0:
            return self.__last_calculation + addend1
        return addend1 + addend2

    # subtract function
    # if num1 or num2 are not of type int or float, returns "INVALID INPUT"
    # if num2 = 0, returns last_calculation - num1
    # otherwise returns num1 - num2
    def subtract(self, num1, num2=0):
        if not self.__is_valid_input(num1) or not self.__is_valid_input(num2):
            return "INVALID INPUT"
        if num2 == 0:
            return self.__last_calculation - num1
        return num1 - num2

    # checks for valid input; returns true if 'num' is int or float, false otherwise
    def __is_valid_input(self, num):
        if isinstance(num, int) or isinstance(num, float):
            return True
        return False
