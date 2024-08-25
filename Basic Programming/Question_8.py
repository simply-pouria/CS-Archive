# Pouria Moradpour 4024023040


# this operates a single prefix expression so the next function don't become cluttered and unreadable
def operate(left_num: float, right_num: float, operator: str) -> float:

    match operator:  # this only works on python 3.10 and above

        case '+':
            return left_num + right_num

        case '-':
            return left_num - right_num

        case '*':
            return left_num * right_num

        case '/':
            return left_num / right_num

        case '//':
            return left_num // right_num

        case '**':
            return left_num ** right_num


def prefix_expression_calculator(expression: str) -> float:

    cached = []
    expression = expression.strip().split()[::-1]

    for char in expression:

        if char.isdigit():
            cached.append(float(char))

        else:

            result = operate(left_num=cached[-1],
                             right_num=cached[-2],
                             operator=char)

            # removing the last two used numbers and adding the result instead
            cached.remove(cached[-1])
            cached.remove(cached[-1])
            cached.append(result)

    return result


def interface():

    print("// Question 8: Prefix Expressions Evaluation")

    prefix_expression = ''

    print("// Enter your prefix expression character by character from left to right, enter 0 to end inputting")

    while True:
        inp = input("// Enter the operand or operator: ")

        if inp == '0':
            break

        prefix_expression += f"{inp} "

    prefix_expression = prefix_expression[:-1]  # deleting the last whitespace

    try:

        print(f"the evaluation of the expression {prefix_expression} is:"
              f"\n{prefix_expression_calculator(prefix_expression)}")

    except (ValueError, TypeError):
        print("// wrong prefix expression.")


if __name__ == "__main__":
    interface()



















