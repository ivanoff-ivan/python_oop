def generate_line(i, n):
    spaces = " " * (n - i)
    stars = "* " * (i + 1)
    return f"{spaces}{stars}"


def print_rhombus(n):
    for i in range(n):
        print(generate_line(i, n))

    for i in range(n - 2, -1, -1):
        print(generate_line(i, n))


print_rhombus(int(input()))
