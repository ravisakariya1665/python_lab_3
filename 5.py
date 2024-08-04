class ArithmeticOperations:
    def __init__(self):
        self.__result = 0

    def add(self, num1, num2):
        self.__result = num1 + num2
        return self.__result

    def subtract(self, num1, num2):
        self.__result = num1 - num2
        return self.__result

    def get_result(self):
        return self.__result

# Example usage
operations = ArithmeticOperations()
print("Addition:", operations.add(10, 5))
print("Subtraction:", operations.subtract(10, 5))
