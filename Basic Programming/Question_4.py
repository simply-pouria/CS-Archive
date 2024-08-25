


from Question_7 import subset_generator, plain_dict


def bubble_sort(lst: list):  # an ascending sort function is needed in the interface function,
    # I'm using the bubble sort function I wrote in the class

    for i in range(len(lst) - 1):

        for j in range(len(lst) - 1 - i):

            if lst[j+1] < lst[j]:

                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


# the input structure is like this: {(t1, t2): winner} where in the key tuple; t1, and t2 are the teams,
# and it is always in ascending order, labeled by numbers, and the value is either the name of the winner team or 0
# which indicates that the match resulted into a draw

# for instance:
# {(3, 4): 4} means that there was a match between teams 3 and 4, and team 4 won the match
# {(1,9): 0} means that there was a match between teams 1 and 9 , and the match ended a draw


def team_list(teams_quantity: int) -> list:  # generates a list containing teams which are named by numbers

    return list(range(1, teams_quantity+1))


def compare(team_1: int, team_2: int, games_data: dict, teams_list: list) -> bool:  # compares two specified teams and
    # swaps their location in the list if needed (the teams should be beside each other in the list for this
    # function to work properly)

    # since the keys are ascending here, and we are not allowed to use sort functions:
    if team_2 > team_1:
        result = games_data[(team_1, team_2)]

    elif team_2 < team_1:
        result = games_data[(team_2, team_1)]

    else:
        raise ValueError('teams can not be the same when comparing!')

    # ANALYSING RESULTS

    if result == 0:  # in this case the match was a draw

        return False  # meaning that we did not change anything

    elif result == team_1:

        if teams_list.index(team_1) + 1 == teams_list.index(team_2):  # team_1 has won and the order is already okay
            return False  # meaning that we did not change anything

        elif teams_list.index(team_2) + 1 == teams_list.index(team_1):  # team_1 has won and the order should be changed

            index_1 = teams_list.index(team_1)
            index_2 = teams_list.index(team_2)

            teams_list[index_2] = team_1
            teams_list[index_1] = team_2

            return True  # meaning that we changed the order

        else:
            raise ValueError('teams should be near each other in the list when comparing')

    elif result == team_2:

        if teams_list.index(team_2) + 1 == teams_list.index(team_1):  # team_2 has won and the order is already okay
            return False  # meaning that we did not change anything

        elif teams_list.index(team_1) + 1 == teams_list.index(team_2):  # team_2 has won and the order should be changed

            index_1 = teams_list.index(team_1)
            index_2 = teams_list.index(team_2)

            teams_list[index_2] = team_1
            teams_list[index_1] = team_2

            return True  # meaning that we changed the order

        else:
            raise ValueError('teams should be near each other when comparing')


def organize(games_data: dict, teams_list: list) -> list:

    iteration_index = 0

    while iteration_index < len(teams_list) - 1:  # this is here to iterate the teams_list with two elements at once
        # without causing index error

        team_1 = teams_list[iteration_index]
        team_2 = teams_list[iteration_index+1]

        change_status = compare(team_1=team_1,
                                team_2=team_2,
                                games_data=games_data,
                                teams_list=teams_list)

        index = iteration_index

        while change_status and index > 0:  # if two elements are swapped, we check if this changes the previous one
            # and continue doing this until we either finish the list or find two elements that don't swap positions

            change_status = compare(team_1=teams_list[index-1],
                                    team_2=teams_list[index],
                                    games_data=games_data,
                                    teams_list=teams_list)

            index -= 1

        iteration_index += 1

    return teams_list


def interface():

    print("// Question 4: Organizing Teams")

    try:
        teams = team_list(int(input("// Enter the number of the teams ")))

        # the subsets with the length of 2 will be the games held
        subsets = plain_dict(initial_set=teams)
        games = subset_generator(initial_set=teams,
                                 subsets=subsets)[2]

        # the keys of the dictionary with which organize() function work, are ascending tuple, creating them here
        games = [(*bubble_sort(game), ) for game in games]  # the (*list) syntax creates a tuple from a list

        games_data = {}

        for game in games:

            game_result = int(input(f"what was the result of the game held between teams {game[0]} and {game[1]}? ("
                                    f"answer with the number of the team, or 0 if the result was a draw)"))

            if game_result not in [0, game[0], game[1]]:
                raise IndexError

            games_data[game] = game_result

        print(organize(games_data=games_data, teams_list=teams))

    except (ValueError, TypeError, KeyError):
        # key error happens when user enters a negative number as the number of the teams
        print("// wrong input, please enter a natural number instead.")

    except IndexError:  # raised if the user enters a team as the winner that haven't participated in the game

        print("// the winner team has to have played the game ... right?")


if __name__ == "__main__":
    interface()























































