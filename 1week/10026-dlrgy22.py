ㅇimport sys
import queue
def not_blindness(arr,N):
    q = queue.Queue()
    count = 0
    visit = [[True for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                visit[i][j] = False
                location = [i,j]
                q.put(location)
                char = arr[i][j]
                while q.qsize() != 0:
                    location = q.get()
                    if location[0]<N-1:
                        if arr[location[0]+1][location[1]] == char and visit[location[0]+1][location[1]] :
                            loc = [location[0]+1,location[1]]
                            q.put(loc)
                            visit[loc[0]][loc[1]] = False
                    if location[1]<N-1:
                        if arr[location[0]][location[1]+1] == char and visit[location[0]][location[1]+1]:
                            loc = [location[0],location[1]+1]
                            q.put(loc)
                            visit[loc[0]][loc[1]] = False
                    if location[0] > 0:
                        if arr[location[0]-1][location[1]] == char and visit[location[0]-1][location[1]] :
                            loc = [location[0]-1,location[1]]
                            q.put(loc)
                            visit[loc[0]][loc[1]] = False
                    if location[1] > 0:
                        if arr[location[0]][location[1]-1] == char and visit[location[0]][location[1]-1] :
                            loc = [location[0],location[1]-1]
                            q.put(loc)
                            visit[loc[0]][loc[1]] = False
                count += 1
    print(count,end = ' ')

def blindness(arr,N):
    q = queue.Queue()
    count = 0
    visit = [[True for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                visit[i][j] = False
                location = [i,j]
                q.put(location)
                if(arr[i][j] == 'R' or arr[i][j] == 'G'):
                    char1 = 'R'
                    char2 = 'G'
                else:
                    char1 = 'B'
                    char2 = ' '
                while q.qsize() != 0:
                    location = q.get()
                    if location[0]<N-1:
                        if (arr[location[0]+1][location[1]] == char1 or arr[location[0]+1][location[1]] == char2) and visit[location[0]+1][location[1]] :
                            loc = [location[0]+1,location[1]]
                            q.put(loc)
                            visit[loc[0]][loc[1]] = False
                    if location[1]<N-1:
                        if (arr[location[0]][location[1]+1] == char1 or arr[location[0]][location[1]+1] == char2) and visit[location[0]][location[1]+1]:
                            loc = [location[0],location[1]+1]
                            q.put(loc)
                            visit[loc[0]][loc[1]] = False
                    if location[0] > 0:
                        if (arr[location[0]-1][location[1]] == char1 or arr[location[0]-1][location[1]] == char2) and visit[location[0]-1][location[1]] :
                            loc = [location[0]-1,location[1]]
                            q.put(loc)
                            visit[loc[0]][loc[1]] = False
                    if location[1] > 0:
                        if (arr[location[0]][location[1]-1] == char1 or arr[location[0]][location[1]-1] == char2) and visit[location[0]][location[1]-1] :
                            loc = [location[0],location[1]-1]
                            q.put(loc)
                            visit[loc[0]][loc[1]] = False
                count += 1
    print(count)

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline())for j in range(N+1)]
not_blindness(arr,N)
blindness(arr,N)