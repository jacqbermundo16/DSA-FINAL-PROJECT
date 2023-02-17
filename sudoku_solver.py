# https://www.youtube.com/watch?v=eqUwSA0xI-s - Part 1 of the source code
# https://www.youtube.com/watch?v=lK4N8E6uNr4 - Part 2

# MODIFICATIONS 

# 1. Ask users to input their unsolved sudoku puzzle.
# 2. Add a menu list?
# 3. Ask users to solve another sudoku puzzle or to exit 
# 4. Make a more user-friendly interface if possible

# STEPS
# 1. Add info for the user like Program name and instructions
# 2. Create a function to ask the user for input and save it.
# 3. Make a menu list? 
# 4. Create a function for the menu list
# 5. Create a code that makes the program repeatable unless the user said stop.


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def basic_info():
    print('==================================')
    print('         SUDOKU SOLVER')
    print('==================================')
    print('Welcome to Sudoku  Solver, in here, we solve your sudoku puzzles.')
    print('To solve your puzzle, we need you to enter the values provided. Follow the steps below carefully to avoid mistakes.')
    print('\n')
    print('Guide to properly input your puzzle')
    print('1. Look at your puzzle and focus on the first row (topmost horintal alignment from left to right, containing 9 boxes).')
    print('2. Input the data by entering the numbers provides, if the box is empty, write 0.')
    print('   > Example: 1 0 0 3 2 0 4 5 0')
    print("   !!NOTE: Please make sure that the position of the numbers  are correct and each input are separated by a single space.")
    print('3. After inserting the numbers, press ENTER and do the same procedure for the next rows.')
    print("4. Once you're done, press ENTER to see the solution")
    print('==================================')

def ask_input():
    print('Please enter the data for each row.')
    _row1 = input("Row 1: ")
    row1 = _row1.split()
    row1 = [int(i) for i in row1]

    _row2 = input("Row 2: ")
    row2 = _row2.split()
    row2 = [int(i) for i in row2]

    _row3 = input("Row 3: ")
    row3 = _row3.split()
    row3 = [int(i) for i in row3]

    _row4 = input("Row 4: ")
    row4 = _row4.split()
    row4 = [int(i) for i in row4]

    _row5 = input("Row 5: ")
    row5 = _row5.split()
    row5 = [int(i) for i in row5]

    _row6 = input("Row 6: ")
    row6 = _row6.split()
    row6 = [int(i) for i in row6]

    _row7 = input("Row 7: ")
    row7 = _row7.split()
    row7 = [int(i) for i in row7]

    _row8 = input("Row 8: ")
    row8 = _row8.split()
    row8 = [int(i) for i in row8]

    _row9 = input("Row 9: ")
    row9 = _row9.split()
    row9 = [int(i) for i in row9]

    print('==================================')
    return row1, row2, row3, row4, row5, row6, row7, row8, row9

def menu_list():
    print('========================')
    print('1-> Solve another puzzle')
    print('2 -> Exit (y/n)')
    print('========================')
    print ()

def sudoku_solver():
    basic_info()
    r1, r2, r3, r4, r5, r6, r7, r8, r9 = ask_input()
    board = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

    print('Sudoku Puzzle')
    print_board(board)
    solve(board)
    print("---------------------------")
    print('Sudoku Puzzle Solution')
    print_board(board)
    print('==================================')
    menu_list()

    def menu():
        while True:
            askInput = int(input('What do you want to do? (1-2): '))
            num = askInput

            if num == 1:
                sudoku_solver()
                
            elif num == 2:
                ask = str(input("Do you want to exit? (y/n):  "))
                if ask == 'y':
                    break
    menu()

sudoku_solver()