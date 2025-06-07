# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.
    operation must be one of: 'add', 'subtract', 'multiply', 'divide'.
    For divide by zero, returns a special string.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "ERROR_DIVIDE_BY_ZERO"
        return num1 / num2
    else:
        return "ERROR_INVALID_OPERATION"
