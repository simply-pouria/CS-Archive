from FoxUI import cprint, clear_screen

from Question_10 import equation_solver
from Question_05 import absolute_value
from Question_09 import reverse_bubble_sort
from Question_05 import square_root


# I represent lines consistently as a tuple like this (slope, constant)
def line_intersection(line_1: tuple[float, float], line_2: tuple[float, float]) -> tuple[float, float]:
    # uses Cramer's method, actuated in question 10, to solve 2 by 2 linear equations that we encounter here

    intersection_point = equation_solver(variable_matrix=[[line_1[0], -1],
                                                          [line_2[0], -1]],

                                         column_vector=[line_1[1],
                                                        line_2[1]])

    intersection_point = (intersection_point[0], intersection_point[1])

    return intersection_point


# draws a perpendicular bisector between two points
def perpendicular_bisector_finder(point_1: tuple[float, float],
                                  point_2: tuple[float, float]) -> tuple[float | None, float]:
    midpoint = ((point_1[0] + point_2[0]) / 2, (point_1[1] + point_2[1]) / 2)

    # working around the zero division exception

    if absolute_value(point_1[0] - point_2[0]) == 0:  # when ΔX = 0
        perpendicular_bisector_slope = 0

    elif absolute_value(point_1[1] - point_2[1]) == 0:  # when ΔY = 0
        perpendicular_bisector = (None, midpoint[0])  # the line will be  x = k
        # (I know that k here is not the constant and this is not mathematically accurate
        # but this is how I represent it : (None (indicating the slope doesn't exist), k (in x=k))
        return perpendicular_bisector

    else:
        perpendicular_bisector_slope = -1 / (
                    (absolute_value(point_1[1] - point_2[1])) / (absolute_value(point_1[0] - point_2[0])))

    perpendicular_bisector_constant = midpoint[1] - (perpendicular_bisector_slope * midpoint[0])
    perpendicular_bisector = (perpendicular_bisector_slope, perpendicular_bisector_constant)

    return perpendicular_bisector


# draws a line between two points
def line_drawer(point_1: tuple[float, float], point_2: tuple[float, float]) -> tuple[float | None, float]:
    if absolute_value(point_1[0] - point_2[0]) == 0:  # when ΔX = 0
        line = (None, point_2[0])
        return line  # the line will be  x = k
        # (I know that k here is not the constant but this is how I represent and differentiate it anyway

    else:
        slope = (absolute_value(point_1[1] - point_2[1])) / (absolute_value(point_1[0] - point_2[0]))

    constant = point_2[1] - (slope * point_2[0])
    line = (slope, constant)
    return line


# checks if the points are on a single line
def on_a_line(point_1: tuple[float, float], point_2: tuple[float, float], point_3: tuple[float, float]) -> bool:
    line = line_drawer(point_1=point_1,
                       point_2=point_2)

    if (not line[0]) and (point_3[0] == point_2):
        return True

    else:
        if (point_3[0] * line[0]) + line[1] == point_3[1]:
            return True

    return False


# finds the point that is between two other points (this is used only if they form a line)
def middle_point_finder(point_1: tuple[float, float],
                        point_2: tuple[float, float],
                        point_3: tuple[float, float]) -> tuple[float, float]:
    x_s = reverse_bubble_sort([point_1[0], point_2[0], point_3[0]])
    y_s = reverse_bubble_sort([point_1[1], point_2[1], point_3[1]])

    point = (x_s[1], y_s[1])
    return point


# returns the perpendicular bisectors which form the outlines of the voronoi diagram,
# except  if the points are on a line, in this case we only need two perpendicular bisectors to solve the problem
def voronoi_diagram_outlines(point_1: tuple[float, float],
                             point_2: tuple[float, float],
                             point_3: tuple[float, float]) -> list:
    points = [point_1, point_2, point_3]
    perpendicular_bisectors = []

    # this if statement is explained in the explanation document
    if on_a_line(point_1=point_1,
                 point_2=point_2,
                 point_3=point_3):

        middle_point = middle_point_finder(point_1=point_1,
                                           point_2=point_2,
                                           point_3=point_3)

        points.remove(middle_point)

        for point in points:
            perpendicular_bisectors.append(perpendicular_bisector_finder(point_1=point, point_2=middle_point))

    else:

        perpendicular_bisectors.append(perpendicular_bisector_finder(point_1, point_2))
        perpendicular_bisectors.append(perpendicular_bisector_finder(point_1, point_3))
        perpendicular_bisectors.append(perpendicular_bisector_finder(point_2, point_3))

    return perpendicular_bisectors


# calculates the distance of a specified point (center) from the k number of other points,
# doesn't raise an exception if a point is None
def euclidean_dist(center: tuple[float, float], *points: tuple) -> dict:

    distances = {}

    for point in points:

        if not point:
            continue

        delta_x_sqr = (absolute_value(center[0] - point[0])) ** 2
        delta_y_sqr = (absolute_value(center[1] - point[1])) ** 2
        distances[point] = square_root(delta_x_sqr + delta_y_sqr)

    return distances


def key_of_smallest_value(dictionary: dict):  # this is needed in the next function

    values = list(dictionary.values())
    smallest_value = reverse_bubble_sort(values)[-1]

    for key in dictionary:

        if dictionary[key] == smallest_value:
            return key


# returns the intersections required by the questions document
def voronoi_diagram_vertex_finder(perpendicular_bisectors: list, border: tuple,
                                  p1: tuple, p2: tuple, p3: tuple) -> list:
    voronoi_diagram_vertices = []

    if len(perpendicular_bisectors) == 3:
        circumcenter = line_intersection(line_1=perpendicular_bisectors[0], line_2=perpendicular_bisectors[1])
        voronoi_diagram_vertices.append(circumcenter)

    for p_bisector in perpendicular_bisectors:

        # finding intersections of each perpendicular bisector
        if p_bisector[0] is None:  # since I represent x=k lines as (None, k)

            # intersections of the perpendicular bisector with:
            x_axis = (p_bisector[1], 0)
            y_axis = None
            x_border = None
            y_border = (p_bisector[1], border[1])

        elif p_bisector[0] == 0:  # for the perpendicular bisectors that have a slope of 0 represented as (0, constant)

            # intersections of the perpendicular bisector with:
            x_axis = None
            y_axis = (0, p_bisector[1])
            x_border = (border[0], p_bisector[1])
            y_border = None

        else:

            # intersections of the perpendicular bisector with:
            x_axis = (-p_bisector[1] / p_bisector[0], 0)
            y_axis = (0, p_bisector[1])
            x_border = (border[0], (p_bisector[0] * border[0]) + p_bisector[1])
            y_border = ((border[1] - p_bisector[1]) / p_bisector[0], border[1])

        # finding the distance of each found intersection
        # and choosing the closest one to either the circumcenter or the middle point
        if len(perpendicular_bisectors) == 2:

            distances = euclidean_dist(middle_point_finder(point_1=p1, point_2=p2, point_3=p3),
                                       x_axis, y_axis, x_border, y_border)

        elif len(perpendicular_bisectors) == 3:

            distances = euclidean_dist(circumcenter,
                                       x_axis, y_axis, x_border, y_border)

        voronoi_diagram_vertices.append(key_of_smallest_value(distances))

    return voronoi_diagram_vertices


def interface():
    clear_screen()
    cprint.question("Question 6: City Division")
    coordinates = []

    try:
        x_border = float(cprint.input("Enter the length of the city: "))
        y_border = float(cprint.input("Enter the height of the city: "))

        for i in range(1, 4):

            x = float(cprint.input(f"Enter the x of the coordinates of the shop {i}: "))
            y = float(cprint.input(f"Enter the y of the coordinates of the shop {i}: "))

            coordinates.append((x, y))

        cprint.answer("the coordinates of the vertices is as followed:")

        vertices = voronoi_diagram_vertex_finder(perpendicular_bisectors=
                                                 voronoi_diagram_outlines(point_1=coordinates[0],
                                                                          point_2=coordinates[1],
                                                                          point_3=coordinates[2]),

                                                 border=(x_border, y_border),
                                                 p1=coordinates[0], p2=coordinates[1], p3=coordinates[2])

    except (ValueError, TypeError):
        cprint.error("wrong input|please enter a number instead.")


if __name__ == "__main__":
    interface()



