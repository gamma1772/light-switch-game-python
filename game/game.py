import random
import time

on, off = ' O ', ' X '

x, y = 0, 0


def generate_matrix(matrix, x_coord=5, y_coord=5):
    """Populates matrix with lights randomly switched on or off"""

    for i in range(x_coord):
        for j in range(y_coord):
            matrix[i][j] = random.choice([on, off])

    return


def display_matrix(matrix):
    """Displays matrix in CLI"""

    for row in range(x):
        print(matrix[row])

    return


def test_condition(matrix):
    """Tests whether all lights in the matrix are switched off. If at least one light is on, test fails"""

    for i in range(x):
        for j in range(y):
            if matrix[i][j] == on:
                return False

    return True


def turn_off_light(matrix, coordinates):
    """TUrns off lights in a cross pattern starting from given coordinates"""

    for i in range(x):
        matrix[i][coordinates[1]] = off

    for j in range(y):
        matrix[coordinates[0]][j] = off

    return


def input_test():
    """Tests user input and based on passed values, defines a tuple, or prompts user to input correct values"""

    a = 0, 0

    while True:
        user_input = input("Define X and Y separated by a comma (x,y): ")

        if user_input.__contains__(','):
            test = True
            for num in user_input.split(','):
                if not num.isnumeric():
                    test = False
                    break
            if not test:
                incorrect_input()
                continue

            a = tuple(int(z) for z in user_input.split(','))
            if len(a) == 2:
                break
            else:
                incorrect_input()
        else:
            incorrect_input()

    return a


def incorrect_input():
    """Outputs a message for user to input correct values, and sleeps 2 seconds"""

    print("Incorrect input, coordinates X and Y must be separated by a comma")
    time.sleep(2)


def game():
    """Generates the matrix, then runs the game in a loop until test condition returns True."""

    global x, y

    a = input_test()
    x, y = a[0], a[1]

    matrix = [[off for i in range(y)] for j in range(x)]

    generate_matrix(matrix, x, y)

    while True:
        display_matrix(matrix)

        if test_condition(matrix):
            break

        turn_off_light(matrix, input_test())

    return
