def Gauss(A):
    for k in range(len(A) - 1):
        At = A.copy()
        for i in range(len(A)):
            assert At[i] is A[i]
            for j in range(len(A)):
                if i <= k:
                    A[i][j] = At[i][j]
                elif i > k and j > k:
                    print('use', i, k)
                    A[i][j] = At[i][j] - (At[i][k] / At[k][k]) * At[k][j]
                elif i > k >= j:
                    print('clear', i, j)
                    A[i][j] = 0
    return A


matrix = [[2, 1, 5, 4, 8, 4],
          [3, 4, 1, 2, 6, 7],
          [2, 3, 5, 7, 2, 3],
          [5, 5, 9, 10, -3, 4],
          [4, 2, 7, 9, 3, 7],
          [5, 8, 9, 2, 6, 1]]
M = Gauss(matrix)
for i in range(len(M)):
    print(*M[i])

