def print_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            print('*', end='')
        print()
print_rectangle(4, 3)


def print_triangle(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))


print_triangle(5)

n=4
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

n = 3
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        if j == 0 or j == 2*i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for i in range(n-2, -1, -1):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        if j == 0 or j == 2*i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

height = 5
for i in range(height):
    for j in range(i + 1):
        print("*", end="")
    print()

height = 5

height = 5


for i in range(height, 0, -1):
    for j in range(i):
        print("*", end="")
    print()