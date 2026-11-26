#시간 초과로 실패한 코드(2차원 배열 2개 만드는 것 때문인 듯)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
#기물 좌표를 배열에 담기
thing = []
for i in range(k):
    x, y = map(int, input().split())
    #배열의 인덱스는 0부터 시작, 체스판 좌표는 (1,1)부터 시작이니까 -1
    thing.append((x - 1, y - 1))

#기물이 있는 위치를 표시하는 판이랑 방문한 위치를 표시하는 판이랑 구분
#기물 위치 배열에 두는 것보다 판에 표시헤놓는 게 바로 확인하기 쉽기 때문   
has_thing = [[False] * n for _ in range(n)]    
visited = [[False] * n for _ in range(n)]

for i in range(len(thing)):
    x, y = thing[i]
    has_thing[x][y] = True

#상하좌우(2칸씩 이동이니까)
dx = [0, 0, -2, 2]
dy = [-2, 2, 0, 0]

count = 0

#thing의 x, y 좌표 꺼내서 이동하기
for i in range(k):
    x, y = thing[i]
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        
        if not has_thing[nx][ny] and not visited[nx][ny]:
            count += 1
            visited[nx][ny] = True
                   
print(count)