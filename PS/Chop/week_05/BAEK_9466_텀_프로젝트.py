from sys import stdin, setrecursionlimit

stdin = open("input/BAEK_9466_텀_프로젝트.txt")

setrecursionlimit(10**6)

def dfs(n):
    global count

    visited[n] = True
    team.append(n)

    if visited[arr[n]] == True:
        if arr[n] in team:
            count -= len(team[team.index(arr[n]):])
        return
    else:
        dfs(arr[n])

T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())

    arr = [0] + list(map(int, stdin.readline().rstrip().split()))

    visited = [False] * (N + 1)
    count = N
    for i in range(1, N + 1):
        if not visited[i]:
            team = []
            dfs(i)
    print(count)

# 시간초과 풀이
# T = int(stdin.readline().rstrip())

# def dfs(x):
# 	global cnt
# 	next = arr[x]
# 	arr[x] = 0
# 	if next:
# 		if next in team:
# 			cnt += team.index(next)
# 			return
# 	else:
# 		cnt += len(team) - 1
# 		return
# 	team.append(next)
# 	dfs(next)

# for _ in range(T):
# 	N = int(stdin.readline().rstrip())
# 	arr = [0] + list(map(int, stdin.readline().rstrip().split()))
# 	cnt = 0
# 	for i in range(1, N+1):
# 		if arr[i]:
# 			team = [i]
# 			dfs(i)
# 	print(cnt)