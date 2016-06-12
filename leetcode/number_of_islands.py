def numofislands(arr):
    count = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                count += 1
                clearRestOfLand(arr, i, j)

    return count


def clearRestOfLand(arr, i, j):
    if i<0 or j<0 or i>=len(arr) or j>= len(arr[i]) or arr[i][j] == 0:
        return

    arr[i][j] = 0
    clearRestOfLand(arr, i + 1, j)
    clearRestOfLand(arr, i - 1, j)
    clearRestOfLand(arr, i, j + 1)
    clearRestOfLand(arr, i, j - 1)
    return


arr = [[1,1,1,0,0],
       [1,1,0,0,0],
       [1,0,0,1,0],
       [0,0,0,0,0]]
print numofislands(arr)
