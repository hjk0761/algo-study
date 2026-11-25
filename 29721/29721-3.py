import sys
input = sys.stdin.readline

n, k = map(int, input().split())
has_thing = set()
for i in range(k):
    x, y = map(int, input().split())
    has_thing.add((x, y))
  
visited = set()

dx = [0, 0, -2, 2]
dy = [-2, 2, 0, 0]

count = 0

for x, y in has_thing:
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        
        #체스판이 (1, 1)에서 (n, n)까지 가능한 범위니까
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        
        if (nx, ny) not in has_thing and (nx, ny) not in visited:
            count += 1
            visited.add((nx, ny))
                   
print(count)