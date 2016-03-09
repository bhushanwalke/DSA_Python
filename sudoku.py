__author__ = 'bhushan'


def create_sudoku(string):
    string_list = list(string)
    sudoku = []
    for i in range(9):
        list1 = []
        for j in range(9):
            list1.append(string_list.pop(0))
        sudoku.append(list1)

    print sudoku[0][0]

create_sudoku("7...8...2..3.249...4...9....8421...5..9...2..1...9543....4...5...165.3..2...3...4")
