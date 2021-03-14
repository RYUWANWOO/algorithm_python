matrix = []

size = int(input())
ways = input().split(" ")


for row in range(0,size):
    matrix.append([])
    for col in range(0,size):
        matrix[row].append((row+1,col+1))

pointer_row, pointer_col = 0,0

for way in ways:

    if way == 'R':
        if pointer_col+1 >=size:
            continue
        else:
            pointer_col += 1
    elif way =='L':
        if pointer_col-1 <0:
            continue
        else:
            pointer_col -= 1
    elif way =='U':
        if pointer_row-1 <0:
            continue
        else:
            pointer_row -= 1
    elif way =='D':
        if pointer_row + 1 >= size:
            continue
        else:
            pointer_row += 1
    else:
        print("Wrong Diretions")
        break

print(matrix[pointer_row][pointer_col][0],matrix[pointer_row][pointer_col][1])