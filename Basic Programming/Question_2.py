


def factorial(number: int) -> int:
    counter = number
    while counter > 1:

        number *= counter-1
        counter -= 1
    return number


def biggest_factorial(number: int) -> int:  # returns the biggest factorial that is smaller than or equal to the number

    keep = number  # this is only used to keep the initial value of number

    while True:

        if factorial(number=number) <= keep:
            return number

        number -= 1


def factorial_coefficient(number: int, fctl: int) -> int:  # calculates the coefficient of the factorial in the number

    coefficient = 0

    while number >= factorial(fctl):

        number -= factorial(fctl)
        coefficient += 1

    return coefficient


def factorial_expansion(number: int) -> dict:
    container = {}  # this acts as a container for each step.
    # the key n, means n! in the factorial expansion, the values are the coefficients of their correlative keys.

    while number >= 1:

        biggest_factorial_number = biggest_factorial(number=number)
        biggest_factorial_coefficient = factorial_coefficient(number=number,
                                                              fctl=biggest_factorial_number)

        container[biggest_factorial_number] = biggest_factorial_coefficient

        number -= biggest_factorial_coefficient * factorial(biggest_factorial_number)

    return container


def interface():

    try:
        print("// Question 2 - Factorial Expansion")
        user_input = int(input("// Enter the natural number you want the factorial expansion of: "))

    except (ValueError, TypeError):
        print("// there is an issue with your input, please enter a natural number")

    else:

        if user_input < 1:
            print("only natural numbers are allowed!")
        output = ''  # this works as a container

        factorial_expansion_dict = factorial_expansion(user_input)

        for key in factorial_expansion_dict:
            output += f'{factorial_expansion_dict[key]}({key}!) + '

        # the slicing is only here to delete the extra '+ ' at the end of the string
        print('// the factorial expansion is: ', output[:-3])


if __name__ == "__main__":
    interface()











