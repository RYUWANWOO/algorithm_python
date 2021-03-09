# 큰 수 의 법칙

result = 0

n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

max = data[n-1]
max_second = data[n-2]

if max == max_second:
    for _ in range(0,m):
        result += max

if max != max_second:
    loop_count = 0
    while loop_count < m:
        max_loop_count = 0
        while max_loop_count < k:
            result += max
            max_loop_count += 1
            loop_count += 1
            if loop_count == m:
                break

        if loop_count == m:
            break
        else:
            result += max_second
            loop_count += 1

print(result)

#하지만 루프를 돌게 되면 m의 크기가 100억 이상이 되게 되면 시간 초과판정을 받는 다.
