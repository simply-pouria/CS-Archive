# Pouria Moradpour  4024023040


from Question_1 import prime_factorize  # this is needed from question 1


def lcm(numbers: list) -> int:

    prime_factorized = []
    factorized_lcm = {}

    # creating a list that contains the prime factorized numbers

    for number in numbers:
        prime_factorized.append(prime_factorize(number))

    # creating a dictionary that contains every prime factor in every provided number and its greatest power
    # (as it is needed to calculate lcm)

    # adds every prime factor as a key (with value being 0) to dictionary without creating duplicate keys
    for prime_factorized_number in prime_factorized:

        for prime_factor in prime_factorized_number:

            if prime_factor not in factorized_lcm.keys():

                factorized_lcm[prime_factor] = 0

    # now we also add the biggest value for each key
    for prime_factor in factorized_lcm:

        for prime_factorized_number in prime_factorized:

            # checks if the selected number (which is represented as a dictionary of {prime factor: power}) has a
            # bigger power than what we already have
            if prime_factor in prime_factorized_number.keys() and prime_factorized_number[prime_factor] > factorized_lcm[prime_factor]:

                factorized_lcm[prime_factor] = prime_factorized_number[prime_factor]

    # now we only need to calculate the number of lcm
    lcm_number = 1

    for prime_factor in factorized_lcm:
        lcm_number *= prime_factor ** (factorized_lcm[prime_factor])

    return lcm_number


def interface():

    print("// Question 3 - LCM")
    print("Enter the numbers that you want the LCM of, to end inputting enter 0 to return the LCM of the numbers "
          "you have entered so far")

    input_numbers = []

    try:

        flag = True
        while flag:

            user_input = int(input("// Enter the natural number you want the LCM of (enter 0 to end this and start "
                                   "calculation) : "))

            if user_input == 0:
                flag = False

            else:
                input_numbers.append(user_input)

        lcm_value = lcm(input_numbers)

    except (ValueError, TypeError, RecursionError):  # Recursion Error happens when a negative number is entered
        print("// there is an issue with your input, please enter a natural number")

    else:

        print('// the LCM is: ', lcm_value)


if __name__ == "__main__":
    interface()











