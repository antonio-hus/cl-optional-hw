
""" Imports Section """
import gui
import re


""" Conversions """
def verify_number(number: int, base: int) -> bool:

    # We transform our number into a string for ease of access to the elements
    # We then iterate through each digit and see if all digits are less than the base
    # Case in which our number is valid. Otherwise, invalid !
    number_str = str(number)
    for digit in number_str:
        if int(digit) > base:
            return False
    return True


def substitution_method(number: int, source_base: int, destination_base: int) -> int:
    pass


def successive_divs_muls_method(number: int, source_base: int, destination_base: int) -> int:
    pass


def rapid_method(number: int, source_base: int, destination_base: int) -> int:
    pass


def conversion(number: int, source_base: int, destination_base: int) -> int:
    gui.clear_console()
    result = 0

    # If source_base < destination_base, then apply substitution method

    # If source_base > destination_base, then apply successive divisions / multiplications method

    # If powers of two => Rapid Conversions

    print("Number's", number, "(from base", source_base, ") representation in base", destination_base, "is", result)
    return result


""" Arithmetic operations """
def separate_operands_and_operators(expression):
    # Define a regular expression pattern to match operators and operands
    pattern = r'(\d+|\D)'

    # Use re.findall to find all matches in the expression
    tokens = re.findall(pattern, expression)

    # Separate numbers and operators
    operands = [token for token in tokens if token.isdigit()]
    operators = [token for token in tokens if not token.isdigit()]

    return operands, operators


def addition(x: int, y: int, base: int) -> int:
    carry = 0
    result = 0

    while x != 0 or y != 0:

        temp_sum = 0
        temp_sum += carry
        temp_sum += x % 10
        temp_sum += y % 10

        carry = temp_sum // base
        result = result * 10 + (temp_sum % base)

        x = x // 10
        y = y // 10

    result = result * 10 + carry
    return int(str(result)[::-1])




def subtraction(x: int, y: int, base: int) -> int:
    pass


def multiplication(x: int, y: int, base: int) -> int:
    carry = 0
    result = 0

    while x != 0:
        temp_prod = x % 10
        temp_prod *= y
        temp_prod += carry

        carry = temp_prod // base
        result = result * 10 + (temp_prod % base)

        x = x // 10

    result = result * 10 + carry
    return int(str(result)[::-1])


def division(x: int, y: int, base: int) -> int:
    pass


def arithmetic_operations(base: int):

    gui.clear_console()
    print("Now please enter the operation you want to perform.")
    print("Use two numbers in the selected base, separated by operators")
    print("The operators can be: '+', '-', '*' and '/'.")

    result = 0
    operands = []
    operators = []

    # Verify Expression
    ok = False
    while not ok:

        expression = input(">")
        operands, operators = separate_operands_and_operators(expression)

        ok = True
        for number in operands:
            if not verify_number(number, base):
                ok = False

        if len(operators) != len(operands) - 1:
            ok = False

        if not ok:
            print("Bad Input - Please enter a valid expression in base", base)

    operands.reverse()
    operators.reverse()

    # Compute Expression
    while operators != [] and len(operands) >= 2:

        x = int(operands.pop())
        y = int(operands.pop())
        op = operators.pop()

        if op == '+':
            result = addition(x, y, base)
        elif op == '-':
            pass
        elif op == '*':
            result = multiplication(x, y, base)
        elif op == '/':
            pass

        operands.append(result)

    print(result)
