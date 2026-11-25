import sys
input = sys.stdin.readline

n, k = map(int, input().split())
has_thing = set()
for i in range(k):
    x, y = map(int, input().split())
    has_thing.add((x, y))
 
#체스판 좌표가 (1, 1)부터 시작하도록 
visited = [[False] * (n + 1) for _ in range(n + 1)]

dx = [0, 0, -2, 2]
dy = [-2, 2, 0, 0]

count = 0

for x, y in has_thing:
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        
        if (nx, ny) not in has_thing and not visited[nx][ny]:
            count += 1
            visited[nx][ny] = True
                   
print(count)