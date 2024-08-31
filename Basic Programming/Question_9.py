from FoxUI import cprint, clear_screen

# the following two functions are from question 7, since we need to have subsets here as well,
# I'm not importing them because it's a little different here
#

def plain_dict(initial_set: list) -> dict:  # this generates a plain dictionary which is needed in the next function

    # this dictionary will contain the subsets, with the length of the subsets as the keys, and a list containing
    # subsets of that length as the value, since the next function does not calculate the null and
    # the set itself as subsets, we add the subset itself here, and just ignore the null subset as it is not needed.
    subsets = {len(initial_set): [initial_set]}

    for dict_key in range(1, len(initial_set)):

        subsets[dict_key] = []

    return subsets


def subset_generator(initial_set: list, subsets: dict) -> dict:

    for element in initial_set:

        #  creating a new set that is the same as initial list except it doesn't have the specified element in it,
        #  remove method is not used as it will change the initial_set itself
        new_set = initial_set[:initial_set.index(element)] + initial_set[initial_set.index(element) + 1:]

        if new_set not in subsets[len(new_set)]:  # some single element subsets might be generated excessively with
            # this algorithm, if so, this if-statement prevents that
            subsets[len(new_set)].append(new_set)

        if len(new_set) > 1:
            subset_generator(initial_set=new_set,
                             subsets=subsets)

    return subsets


#
# the following code is not from question 7 anymore
#


# returns the intersection of two intervals
def intersect(first_interval: tuple, second_interval: tuple) -> tuple | None:

    # this essentially means 'biggest interval startpoint, smallest interval endpoint'
    intersection = (first_interval[0] if second_interval[0] < first_interval[0] else second_interval[0],
                    second_interval[1] if second_interval[1] < first_interval[1] else first_interval[1])

    if intersection[0] >= intersection[1]:
        return None

    return intersection


# returns the intersection of n intervals
def multi_intersection(intervals: list) -> tuple | None:

    # this works based on A∩B∩C = (A∩B)∩C
    last_intersection = intervals[0]

    for interval in intervals[1:]:
        last_intersection = intersect(last_intersection, interval)

        if not last_intersection:
            return None

    return last_intersection


def reverse_bubble_sort(lst: list):  # a descending sort function is needed in the next function,
    # I'm using the bubble sort function I wrote in the class, and then reversing it

    for i in range(len(lst) - 1):

        for j in range(len(lst) - 1 - i):

            if lst[j+1] < lst[j]:

                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst[::-1]


def descend_keys(dctnr: dict) -> dict:  # returns a dictionary whose keys are sorted in descending order
    # this is needed so that the iteration would work properly in the next function

    new_dctnr = {}
    descending_keys = reverse_bubble_sort(lst=list(dctnr.keys()))

    for key in descending_keys:
        new_dctnr[key] = dctnr[key]

    return new_dctnr


def golden_age_calc(world_science_history: dict) -> tuple:  # calculates the golden age using the previous functions

    scientist_combinations = plain_dict(initial_set=list(world_science_history.keys()))
    scientist_combinations = descend_keys(subset_generator(initial_set=list(world_science_history.keys()),
                                                           subsets=scientist_combinations))

    for key in scientist_combinations:

        for scientists in scientist_combinations[key]:

            mutual_age = multi_intersection([world_science_history[scientist] for scientist in scientists])

            if mutual_age:

                return mutual_age, scientists


def interface():
    clear_screen()
    cprint.question("Question 9: The Golden Age")
    science_history = {}

    try:
        cprint.info("Enter 0 to end the inputting process, and calculate the golden age")

        while True:

            scientist = cprint.input("Enter the name of the scientist: ")

            if scientist == '0':
                break

            birth = int(cprint.input("Enter their birth year: "))
            death = int(cprint.input("Enter their death year: "))

            if birth < 1 or death < 1:
                raise ValueError

            science_history[scientist] = (birth, death)

        golden_age = golden_age_calc(world_science_history=science_history)

        if len(golden_age[1]) < 2:
            cprint.answer("unfortunately there had not been a time when two or more scientists were alive simultaneously")

        else:
            cprint.answer(f"the golden age was from {golden_age[0][0]} till {golden_age[0][1]} "
                  f"with scientists: {golden_age[1]} being alive then")

    except (ValueError, TypeError):
        cprint.error("wrong input|(note that you need to enter a natural number for the birth/death year).")

    except KeyError:
        cprint.error("note that birth year should be before death year, and that we need at least two scientists obviously")

    except IndexError:
        cprint.error("the number of scientists can't be zero! you need at least two of them")
        


if __name__ == "__main__":
    interface()















































