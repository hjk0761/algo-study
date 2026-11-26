import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for i in range(n):
    name, max_power = input().split()
    arr.append([name, int(max_power)])

arr2 = []
result = []

for i in range(m):
    power = int(input())
    arr2.append(power)
    
for i in range(len(arr2)):
    for j in range(len(arr)):
        if arr2[i] <= arr[j][1]:
            result.append(arr[j][0])
            break

for i in range(len(result)):
    print(result[i])
