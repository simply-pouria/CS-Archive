# Pouria Moradpour  4024023040


#  I'm using the Prime Factorization by Division Method here

def is_prime(number: int) -> bool:  # checks whether a number is a prime number

    for factor in range((number // 2) + 1, 1, -1):  # 1 and the number itself (except for 1,2, and 4) are not considered
        # here so every factor found here means that our number is a composite one

        if number == 4 or (number % factor == 0 and factor not in (1, 2)):
            return False

    return True


def prime_number_generator(start_point: int = 1):  # in this method we need prime numbers to be generated respectively

    number = start_point

    while True:

        if is_prime(number):
            return number

        number += 1


# this method is more complex but way faster and more efficient than generating every prime number smaller than the
# specified number and then checking it
def prime_factorize(number: int, prime_factor: int = 2, prime_factors=None):

    if prime_factors is None:
        prime_factors = {}

    if number == 1:

        return prime_factors

    quotient = number/prime_factor
    integer_division = number//prime_factor

    if quotient == integer_division:

        # adds to the power of the prime factor if it's added before
        if prime_factors.get(prime_factor):
            prime_factors[prime_factor] += 1

        # adds the prime factor if it's not added before
        else:
            prime_factors[prime_factor] = 1

        if quotient//prime_factor == quotient/prime_factor:  # checks if the remnant still has the same prime factor

            return prime_factorize(number//prime_factor,
                                   prime_factor=prime_number_generator(start_point=prime_factor),
                                   prime_factors=prime_factors)

        elif quotient == 1:  # 1 might be reached here, if so, this statement prevents the program from recurring
            # again, though it is not necessary
            return prime_factors

        else:  # this is the case when we have found a prime factor, but there is no more of that factor in the
            # number so we move on to the next prime factor
            return prime_factorize(number//prime_factor,
                                   prime_factor=prime_number_generator(start_point=prime_factor+1),
                                   prime_factors=prime_factors)

    else:  # this is the case when the examined prime factor was not found in the number, therefore we move on
        return prime_factorize(number,
                               prime_factor=prime_number_generator(start_point=prime_factor+1),
                               prime_factors=prime_factors)


def interface():

    print("// Question 1: Prime Factorization")

    try:
        integer = int(input("// Enter a natural number to get it's prime factorization: "))
        prime_factors = prime_factorize(number=integer)

    except (ValueError, TypeError, RecursionError):  # Recursion Error happens when a negative number is entered
        print("// wrong input, please enter a natural number instead.")

    else:

        output = ''  # this works as a container

        for prime_factor in prime_factors:

            output += f'{prime_factor}^{prime_factors[prime_factor]} + '

        print('// the prime  factorization is: ', output[:-3])  # to omit the + in the end


if __name__ == "__main__":
    interface()



