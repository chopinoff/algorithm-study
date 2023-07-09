import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int,input().split())
queue = [i for i in range(1,n+1)]

# result는 제거된 사람들의 순서를 저장하는 리스트입니다. 
# count는 현재 제거될 사람의 인덱스를 나타내는 변수입니다.
result = []
count = 0

for i in range(n):
    count += k-1
    if count >= len(queue):
        count = count%len(queue)
    result.append(str(queue.pop(count)))
print("<", ", ".join(result), ">", sep = '')