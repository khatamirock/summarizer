from numpy import matrix


alien = []
newaln = []

matrix = []
matrix = [['a', 'h', 't', 'h'],
          ['h', 'h', 't', 'a'],
          ['t', 't', 'h', 'h'],
          ['a', 'h', 't', 'h'],
          ['h', 't', 'h', 'h'],


          ]
for x in range(5):
    a = []
    for y in range(4):
        inp = matrix[x][y]
        # input()
        # a.append((inp))
        if inp == 'a':
            alien.append((x, y))
        # print(x, y)
    # matrix.append(a)
print(matrix)

print(alien)


def check(pos, r, c):
    xx = pos[0]
    yy = pos[1]

    sorr = [(xx, yy+1), (xx, yy - 1), (xx-1, yy), (xx+1, yy)]
    for x in sorr:
        if x[0] < 0 or x[1] < 0 or x[0] >= r or x[1] >= c:
            pass
        else:
            # print(x, '<<')
            elem = matrix[x[0]][x[1]]
            if elem == 'h':
                matrix[x[0]][x[1]] = 'a'

                newaln.append((x[0], x[1]))


cont = 0
while alien:
    x = alien.pop(0)
    if len(alien) == 0:
        alien = newaln
        cont += 1
    check(x, 5, 4)


print(cont)
