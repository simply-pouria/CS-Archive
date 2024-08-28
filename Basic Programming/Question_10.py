


def is_n_n(matrix: list) -> bool:  # checks if the provided matrix has an n*n form

    for row in matrix:
        if len(row) != len(matrix):
            return False

    return True


def sub_matrix_generator(matrix: list, row: int, column: int) -> list:  # returns a sub_matrix by omitting the
    # specified rows and columns

    matrix_copy = [x[:] for x in matrix]  # straightforward shallow copies such as matrix[:] and list(matrix)
    # did not work

    matrix_copy.remove(matrix_copy[row])

    for single_row in matrix_copy:
        single_row.remove(single_row[column])

    return matrix_copy


def determinant(matrix: list) -> int:
    determinant_value = 0  # this will work as a container for each step
    matrix_size = len(matrix)
    if not is_n_n(matrix):
        raise ValueError('the provided matrix should have a nxn form')

    else:
        if matrix_size == 1:
            # The determinant of a 1x1 matrix is simply the value of its single entry.
            return matrix[0][0]
        else:
            for j in range(0,len(matrix)):  # iterates the first row of the matrix as indicated in the problems document
                new_temp_matrix = sub_matrix_generator(matrix=matrix, row=0, column=j)
                # calculates the determinant of the shrunk matrix and adds it to the container
                determinant_value += matrix[0][j] * ((-1)**j) * determinant(new_temp_matrix)
            return determinant_value

# for instance:
# print(determinant([[1 , 2 , 3 , 4 ],
# [5 , 6 , 7 , 8 ],
# [9 , 10, 11, 12],
# [13, 14, 15, 16]]))


# this function swaps a specified column of a matrix as it is needed to perform Cramer's Rule
def column_swapper(initial_matrix: list, new_column: list, column_index: int) -> list:
    matrix = [x[:] for x in initial_matrix]

    for row in matrix:
        row[column_index] = new_column[matrix.index(row)]  # swaps each element of the specified column with the
        # parallel element in the new_column

    return matrix


# this function is used to perform Cramer's Rule for a specified x
def cramer_rule(variable_matrix: list, column_vector: list, x_index: int) -> float:
    # x_index argument is used to indicate which x needs to be returned

    #  the naming here also aligns with those in the provided problems document in LMS Canvas
    det_a = determinant(matrix=variable_matrix)

    # creating Aj matrix by replacing column j with the column vector
    a_j = column_swapper(initial_matrix=variable_matrix,
                         new_column=column_vector,
                         column_index=x_index)

    det_aj = determinant(a_j)

    if det_a == 0:
        raise ValueError('the determinant of the variable matrix should not be zero, the answer is now either '
                         'dependant or inconsistent, use a RREF calculator instead')  # since det A is the denominator

    else:
        return det_aj / det_a


def equation_solver(variable_matrix: list, column_vector: list) -> dict:  # this one glues everything together!

    answers = {}  # this will work as a container for each step

    for column in variable_matrix:
        answer = cramer_rule(variable_matrix=variable_matrix,
                             column_vector=column_vector,
                             x_index=variable_matrix.index(column))

        answers[variable_matrix.index(column)] = answer

    return answers


def interface():

    print("// Question 10: Solving Linear Equations")

    try:

        n = int(input("// Enter the number of the equations (=number of the variables): "))

        if n < 0:
            raise ValueError

        # creating the variable matrix while getting the items
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(float(input(f"// Enter the item i={i+1} j={j+1} of the variable matrix: ")))

        # creating the column vector and adding the items
        vector = []
        for i in range(n):
            vector.append(float(input(f"// Enter the item {i+1} of the column vector: ")))

        answers = equation_solver(variable_matrix=matrix, column_vector=vector)

        print("the answers:")
        for key in answers:
            print(f"X{key + 1} = {answers[key]}")



    except (ValueError, TypeError):
        print("// wrong input. (please note that the number of equations is a natural number obviously)"
              "(also, the variable matrix's determinant cannot be zero,"
              " as the answer would be either inconsistent or dependent, for that use a RREF calculator)")


if __name__ == "__main__":
    interface()





