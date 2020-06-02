import sys
import math
import queue
from itertools import permutations
N = int(sys.stdin.readline())
people = list(map(int,sys.stdin.readline().split()))
all = sum(people)
arr = [list(map(int,sys.stdin.readline().split()))for i in range(N)]
result = math.inf
for i in range(1,N//2+1):
    A = list(permutations(range(N),i))
    for l in A:
        visit = [False for i in range(N)]
        people_l = people[l[0]]
        count = 1
        visit[l[0]] = True
        q = queue.Queue()
        q.put(l[0])
        while q.qsize() != 0:
            location = q.get()
            for j in range(1,len(arr[location])):
                for k in l:
                    if not visit[k] and k == arr[location][j]-1 :
                        visit[k] = True
                        people_l += people[k]
                        count += 1
        if count != i:
            continue
        area = 0
        for j in range(N):
            if not visit[j]:
                visit[j] = True
                q.put(j)
                area += 1
                if area > 1:
                    break
                while q.qsize() != 0:
                    location = q.get()
                    for k in range(1,len(arr[location])):
                        if not visit[arr[location][k] -1]:
                            visit[arr[location][k] -1] = True
                            q.put(arr[location][k] -1)
        if area == 1:
            if result > abs(all - 2*people_l):
                result = abs(all - 2*people_l)
if result == math.inf:
    print(-1)
else:
    print(result)