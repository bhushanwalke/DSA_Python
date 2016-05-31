matrix = [[1,2],
          [3,4],]
matrix1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    # for i in matrix:
    #     print i
    matrix.reverse()

    for i in range(len(matrix)):
        for j in range(i):
            print(matrix[i][j], matrix[j][i], matrix[j][i], matrix[i][j])
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in matrix:
        print i

rotate(matrix1)



