N = int(input())

count = 0

for H in range(N+1):
    for M in range(60):
        for S in range(60):
            if '3' in str(H)+str(M)+str(S):
                count += 1


print(count)
