input = input()
row = int(input[1])
col = int(ord(input[0])-ord('a'))+1

count = 0

night_checks = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

for night_check in night_checks:
    night_row = row + night_check[0]
    night_col = col + night_check[1]

    if night_row >=1 and night_row <=8 and night_col>=1 and night_col <=8:
        count += 1

print(count)
