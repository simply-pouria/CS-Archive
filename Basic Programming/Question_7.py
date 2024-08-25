


def permutation_generator(lst: list, start: int, end: int, permutations: list) -> list:  # this generates all n!
    # permutations of a list  with the length of n

    # the algorithm here is derived from https://www.codingninjas.com/studio/library/print-all-permutations-in-string

    if start == end:
        permutations.append(lst[:])  # adding a copy to prevent it from changing after the value of lst changed

    else:

        for index in range(start, end):
            lst[index], lst[start] = lst[start], lst[index]
            permutation_generator(lst=lst, start=(start + 1), end=end, permutations=permutations)
            lst[index], lst[start] = lst[start], lst[index]

    return permutations


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

        if new_set not in subsets[len(new_set)]:  # single element subsets might be generated excessively with
            # this algorithm, if so, this if-statement prevents that
            subsets[len(new_set)].append(new_set)

        if len(new_set) > 1:
            subset_generator(initial_set=new_set,
                             subsets=subsets)

    return subsets


def subset_permutation(initial_set: list) -> list:  # returns permutations of the subset of a set

    container = []  # this will contain permutations of subsets

    plain_subsets_dictionary = plain_dict(initial_set=initial_set)

    subsets = subset_generator(initial_set=initial_set,
                               subsets=plain_subsets_dictionary)

    for subset_key in subsets:

        for subset in subsets[subset_key]:
            permutation_generator(lst=subset,
                                  start=0,
                                  end=len(subset),
                                  permutations=container)

    return container


def interface():
    print("// Question 7: Creating Strings")

    characters = []
    counter = 0

    print("// You will be inputting the characters you want the permutations of, in order to end it, Enter 0")

    while True:
        counter += 1
        character = input(f"// Enter the character {counter}: ")

        if character == '0':
            break

        characters.append(character)

    permutations = subset_permutation(initial_set=characters)
    print("the permutations are:")

    for permutation in permutations:
        p = ''

        for char in permutation:
            p += char

        print(p)


if __name__ == "__main__":
    interface()
