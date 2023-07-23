import sys
def input():
    return sys.stdin.readline().rstrip()

n, r, c = map(int, input().split())
answer = 0

while n != 0:
    # 1사분면 2사분면
    # 3사분면 4사분면
    n -= 1
    # 1사분면에서 시작하는 점이라면
    if (0 <= r < 2 ** n) and (0 <= c < 2 ** n):
        answer += (2 ** n) * (2 ** n ) * 0
        # 1사분면에서 시작하므로 더 축소할 필요가 없다.

    # 2사분면에서 시작하는 점이라면
    if (0<= r < 2 ** n) and (2 **n <= c < 2 ** (n+1)):
        # 2사분면에서 시작하는 지점 더해주기
        answer += (2 ** n) * (2 ** n) * 1
        # 열 축소
        c -= 2 ** n

    # 3사분면에서 시작하는 점이라면
    if (2 ** n <= r < 2 ** (n+1)) and (0 <= c < 2 ** n):
        answer += (2 ** n) * (2 ** n) * 2
        r -= 2 ** n

    # 4사분면에서 시작하는 점이라면
    if (2 ** n <= r < 2 ** (n+1)) and (2 ** n <= c < 2 ** (n+1)):
        answer += (2 ** n) * (2 ** n) * 3
        r -= 2 ** n
        c -= 2 ** n
print(answer) 