from FoxUI import cprint, clear_screen

from Question_02 import factorial


def power(x: int | float, n: int) -> float:  # because ** operator is prohibited

    if n < 0:
        raise ValueError("only non-negative numbers are accepted")

    if n == 0:
        return 1

    counter = 1
    base = x

    while counter < n:
        x *= base
        counter += 1

    return x


def absolute_value(x):  # because abs() is not allowed
    return x if x >= 0 else -x


#
# DEFINING FUNCTIONS THAT ARE SPECIFIED IN THE DOCUMENT
#


# I'm using the Babylonian method to estimate square root
# (I found out about it here https://en.wikipedia.org/wiki/Methods_of_computing_square_roots)
def square_root(x: int | float) -> float:
    if x < 0:
        raise ValueError("out of square root domain")

    guess = x  # starting with x itself as the first guess
    imperfection = absolute_value((guess * guess) - x)

    while imperfection > 0.0001:  # tolerance is specified at 0.0001 as I think it's a fair performance/accuracy balance

        guess = 0.5 * (guess + (x / guess))
        imperfection = absolute_value((guess * guess) - x)

    return guess


# I'm using the Taylor series to estimate sin(x)
# (I found out about it here https://medium.com/@tarlanahad/how-is-sin-x-calculated-by-computers-8d386a54cefc)
def sin(x: int | float) -> float:
    n = 0
    sin_estimation = 0
    while n <= 10:  # the Taylor series is calculated till 10

        nominator = (power(x=-1, n=n)) * power(x=x, n=((2 * n) + 1))
        denominator = factorial(number=((2 * n) + 1))

        sin_estimation += (nominator / denominator)
        n += 1

    return sin_estimation


# to represent various polynomials I'm defining a class as it's more convenient in this case compared to a function
class Polynomial:

    def __init__(self, degree: int, coefficients: list):  # requiring the user to indicate a specific
        # polynomial when defining an object of this class
        self.y = None
        self.degree = degree
        self.coefficients = coefficients

        if len(self.coefficients) != degree + 1:  # coefficients are taken as positional arguments and need to
            # indicate the coefficient of each power of x respectively (including x^0)

            raise ValueError("you need to enter coefficients for each nomial, if it doesn't exist enter 0, you also "
                             "need to enter a coefficient for x^0")

        elif degree <= 0:
            raise ValueError("only natural numbers are accepted")

    def find_y(self, x: int | float) -> float:

        self.y = 0
        for coefficient in self.coefficients:
            self.y += coefficient * (power(x=x, n=self.degree - (self.coefficients.index(coefficient))))

        return self.y


#
# ESTIMATING INTEGRAL USING THE TRAPEZOIDAL RULE
#


def trapezoidal_rule(interval: tuple, func) -> float:  # calculates the integral of a specified function over a
    # specified interval using a single trapezoid

    start_point = interval[0]
    end_point = interval[1]
    interval_length = end_point - start_point

    return (interval_length / 2) * (func(start_point) + func(end_point))


def estimate_integral(interval: tuple, sub_intervals_quantity: int, func) -> float:  # divides the interval into
    # sub-intervals and performs the trapezoidal integration on each of them

    integral = 0
    start_point = interval[0]
    end_point = interval[1]
    interval_length = end_point - start_point
    sub_intervals_length = interval_length / sub_intervals_quantity

    while start_point < end_point:

        sub_interval_end = start_point + sub_intervals_length
        integral += trapezoidal_rule(interval=(start_point, sub_interval_end),
                                     func=func)
        start_point = sub_interval_end

    return integral


def interface():
    clear_screen()
    cprint.question("Question 5: Numerical Integration")

    try:

        start_point = float(cprint.input("Enter the start point of the interval, over which you want to integrate: "))

        end_point = float(cprint.input("Enter the end point of the interval, over which you want to integrate: "))

        if end_point <= start_point:
            raise ValueError

        intervals_quantity = int(cprint.input("Enter the the number of intervals you want the initial interval to be "
                                       "divided to: (the higher the number the more precise the integral would be) "))

        if intervals_quantity < 1:
            raise ValueError

        function = cprint.input("Enter the function you want to integrate: (sin, square root, polynomial) ").lower()

        match function:

            case 'sin':
                cprint.answer("the integral is approximately:")
                cprint.answer(estimate_integral(interval=(start_point, end_point),
                                        sub_intervals_quantity=intervals_quantity,
                                        func=sin))

            case 'square root':
                cprint.answer(estimate_integral(interval=(start_point, end_point),
                                        sub_intervals_quantity=intervals_quantity,
                                        func=square_root))

            case 'polynomial':
                cprint.answer("the integral is approximately: ")
                degree = int(cprint.input("enter the degree of the polynomial "))
                coefficients = []

                for i in range(degree+1):

                    coefficient = float(cprint.input(f"what is the coefficient of x^{i} "))
                    coefficients.append(coefficient)

                polynomial_instance = Polynomial(degree, coefficients)

                cprint.answer("the integral is approximately:")
                cprint.answer(estimate_integral(interval=(start_point, end_point),
                                        sub_intervals_quantity=intervals_quantity,
                                        func=polynomial_instance.find_y))

            case _:
                raise ValueError

    except (ValueError, TypeError):
        cprint.error("wrong input|(note that the start point should be smaller than the end point, number of integrals"
              " should be a natural number, and you should enter the name of the function you want to integrate).")


if __name__ == "__main__":
    interface()

