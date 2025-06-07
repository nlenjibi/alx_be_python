# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform an arithmetic operation based on the input.

    Parameters:
    - num1 (float): The first number
    - num2 (float): The second number
    - operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
    - float: The result of the operation
    - str: Error message if division by zero or invalid operation
    """
    operation = operation.lower().strip()

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"
