n = 7

matrix = [[0] * n for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1

while top <= bottom and left <= right:

    # ➡️ Right
    for j in range(left, right + 1):
        matrix[top][j] = num
        num += 1
    top += 1

    # ⬇️ Down
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # ⬅️ Left
    if top <= bottom:
        for j in range(right, left - 1, -1):
            matrix[bottom][j] = num
            num += 1
        bottom -= 1

    # ⬆️ Up
    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

# Print Matrix
for row in matrix:
    for value in row:
        print(f"{value:2}", end=" ")
    print()