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
   
#이중for문 시간초과로 이진탐색으로 변경 
for i in range(len(arr2)):
    #확인할 배열(arr)의 시작 인덱스
    left = 0
    #확인할 배열(arr)의 끝 인덱스(인덱스는 0부터니까 길이에서 -1 해줘야 함)
    right = len(arr) - 1
    #가장 첫번째 칭호를 찾아야하므로 선언(맨 오른쪽부터 시작해서 점차 왼쪽으로 이동)
    index = len(arr) - 1
    
    #left인덱스의 값이 right인덱스의 값보다 작거나 같으면
    while left <= right:
        mid = (left + right) // 2
        if arr2[i] <= arr[mid][1]:
            index = mid
            #맨 처음 right은 볼 필요 없으니 mid의 바로 왼쪽으로 이동
            right = mid - 1
        else:
            #맨 처음 left는 볼 필요 없으니 mid의 바로 오른쪽으로 이동
            left = mid + 1
    result.append(arr[index][0])        

for i in range(len(result)):
    print(result[i])
