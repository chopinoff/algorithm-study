from sys import stdin

stdin = open("input/BOJ_15685_드래곤_커브.txt")

# 동-북-서-남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


n = int(stdin.readline().rstrip())
board = [[0] * 101 for _ in range(101)]

for _ in range(n):
    y, x, d, g = map(int, stdin.readline().rstrip().split())
    board[x][y] = 1
    temp = [d]
    q = [d]  # 이동방향
    for _ in range(g + 1):  # 0~g세대
        for k in q:
            x += dx[k]
            y += dy[k]
            board[x][y] = 1
        q = [(i + 1) % 4 for i in temp]
        q.reverse()
        temp = temp + q

result = 0
for i in range(100):
    for j in range(100):
        if (
            board[i][j]
            and board[i][j + 1]
            and board[i + 1][j]
            and board[i + 1][j + 1]
        ):
            result += 1

print(result)