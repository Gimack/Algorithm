import sys
import queue
import copy
dx = [0,0,1,-1]
dy = [1,-1,0,0]
N,M = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for i in range(N)]
for i in arr:
    i = list(i)
location = []
for i in range(0,N):
    for j in range(0,M):
        if arr[i][j] == 'o':
            location.append([i,j])
            arr[i][j] = '.'
q = queue.Queue()
location.append(0)
q.put(location)
result = -1
visit = [[[[False for i in range(M)] for j in range(N)] for k in range(M)] for l in range(N)]
while q.qsize() != 0 and result == -1:
    loc = q.get()
    if loc[2] > 10:
        continue
    c1_x = loc[0][1]
    c1_y = loc[0][0]
    c2_x = loc[1][1]
    c2_y = loc[1][0]
    for i in range(0,4):
        if c1_y + dy[i] < 0 or c1_y + dy[i] >= N or c1_x + dx[i] < 0 or c1_x + dx[i] >= M:
            if c2_y + dy[i] < 0 or c2_y + dy[i] >= N or c2_x + dx[i] < 0 or c2_x + dx[i] >= M:
                continue
            else:
                result = loc[2] + 1
                break
        elif c2_y + dy[i] < 0 or c2_y + dy[i] >= N or c2_x + dx[i] < 0 or c2_x + dx[i] >= M:
            result = loc[2] + 1
            break
        else :
            move_1 = False
            move_2 = False
            s1_y = c1_y
            s1_x = c1_x
            s2_y = c2_y
            s2_x = c2_x
            if arr[c1_y + dy[i]][c1_x + dx[i]] == '.':
                c1_y = c1_y + dy[i]
                c1_x = c1_x + dx[i]
                move_1 = True
            if arr[c2_y + dy[i]][c2_x + dx[i]] == '.':
                c2_y = c2_y + dy[i]
                c2_x = c2_x + dx[i]
                move_2 = True
            if c1_y == c2_y and c1_x == c2_x:
                if move_1:
                    c1_y -= dy[i]
                    c1_x -= dx[i]
                else:
                    c2_y -= dy[i]
                    c2_x -= dx[i]
            if not visit[c1_y][c1_x][c2_y][c1_x]:
                visit[c1_y][c1_x][c2_y][c2_x] = True
                count = loc[2] + 1
                put_loc = [[c1_y, c1_x],[c2_y, c2_x],count]
                q.put(put_loc)
            c1_x = s1_x
            c1_y = s1_y
            c2_x = s2_x
            c2_y = s2_y
print(result)