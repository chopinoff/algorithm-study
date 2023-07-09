import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
tower = list(map(int, input().split()))

stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    while stack:
        if tower[stack[-1] - 1] >= tower[i] :
            answer[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(i+1)
print(*answer)