import sys
def input():
    return sys.stdin.readline().rstrip()

n = input()
answer = 0

count = [0 for i in range(10)]

for i in n:
    if i == "9" or i == "6":
        if count[9] == count[6]:
            count[6] += 1
        else:
            count[9] += 1
    else:
        count[int(i)] += 1
print(max(count))


