import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())

card = deque([c for c in range(1,n+1)])
while len(card) != 1:
    card.popleft()
    card.append(card.popleft())
print(*card)