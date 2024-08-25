# Pouria Moradpour 4024023040

from Question_1 import interface as interface_1
from Question_2 import interface as interface_2
from Question_3 import interface as interface_3
from Question_4 import interface as interface_4
from Question_5 import interface as interface_5
from Question_6 import interface as interface_6
from Question_7 import interface as interface_7
from Question_8 import interface as interface_8
from Question_9 import interface as interface_9
from Question_10 import interface as interface_10


print("// Welcome!")

while True:

    try:
        question = int(input("// Enter the number of the question (1-10) to enter it's solution : "))

    except (ValueError, TypeError):
        print("// wrong input, please enter a natural number instead.")

    else:

        try:
            match question:  # only works on python 3.10 and above

                case 1:
                    interface_1()

                case 2:
                    interface_2()

                case 3:
                    interface_3()

                case 4:
                    interface_4()

                case 5:
                    interface_5()

                case 6:
                    interface_6()

                case 7:
                    interface_7()

                case 8:
                    interface_8()

                case 9:
                    interface_9()

                case 10:
                    interface_10()

                case _:
                    print("the number of questions is from 1 to 10")

        # potential errors ARE caught in the interface function of each question,
        # however this is just so that the program wouldn't crash if something goes under the radar.
        except Exception as error:
            print(f"oops looks like there is an issue:\n{error}")



