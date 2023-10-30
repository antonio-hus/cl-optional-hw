
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


def base10_substitution_method(number: int, source_base: int) -> int:
    p = 0
    s = 0
    while number != 0:
        s += number % 10 * (source_base ** p)
        number = number // 10
        p = p + 1
    return s


def base10_successive_divisions_method(number: int, destination_base: int) -> int:
    result = 0
    p = 1

    while number != 0:
        result = result + p * (number % destination_base)
        number = number // destination_base
        p = p * 10

    return result


def intermediate_base10_conversion(number: int, source_base: int, destination_base: int) -> int:
    number = base10_substitution_method(number, source_base)
    number = base10_successive_divisions_method(number, destination_base)
    return number


def substitution_method(number: int, source_base: int, destination_base: int) -> int:

    # Step 1 - Convert all digits of the number in destination_base
    # Since source_base < destination_base => already ok

    p = 0
    s = 0
    while number != 0:
        s += number % 10 * p
        p = p + 1
    return number


def successive_divisions_method(number: int, source_base: int, destination_base: int) -> int:
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
    p = 1

    while x != 0 or y != 0:

        temp_sum = 0
        temp_sum += carry
        temp_sum += x % 10
        temp_sum += y % 10

        carry = temp_sum // base
        result = result + (temp_sum % base) * p

        x = x // 10
        y = y // 10
        p = p * 10

    result = result + carry * p
    return result


def subtraction(x: int, y: int, base: int) -> int:
    borrow = 0
    result = 0
    p = 1

    while x != 0 or y != 0:

        temp_sub = borrow
        temp_sub += x % 10
        temp_sub -= y % 10

        if temp_sub < 0:
            borrow = -1
            temp_sub += base
        else:
            borrow = 0

        x = x // 10
        y = y // 10

        result = result + temp_sub * p
        p = p * 10

    return result


def multiplication(x: int, y: int, base: int) -> int:
    carry = 0
    result = 0
    p = 1

    while x != 0:
        temp_prod = x % 10
        temp_prod *= y
        temp_prod += carry

        carry = temp_prod // base
        result = result + (temp_prod % base) * p

        x = x // 10
        p = p * 10

    result = result + carry * p
    return result


def division(x: int, y: int, base: int) -> int:
    quotient = 0
    remainder = 0

    og = int(str(x)[::-1])  # Reverse of x
    current_remainder = og % 10
    while og != 0:
        current_remainder = base10_substitution_method(current_remainder, base)  # to base 10
        quotient = quotient * 10 + current_remainder // y

        og = og // 10
        current_remainder = current_remainder % y * 10 + og % 10
    remainder = current_remainder // 10
    print(quotient, remainder)
    return quotient


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
            result = subtraction(x, y, base)
        elif op == '*':
            result = multiplication(x, y, base)
        elif op == '/':
            result = division(x, y, base)

        operands.append(result)

    print(result)
