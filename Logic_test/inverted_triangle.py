# ข้อที่8
def print_inverted_triangle(rows):
    for i in range(rows):
        spaces = "  " * i
        stars = "* " * (2 * (rows - i) - 1)
        print(spaces + stars)

n = int(input("Enter number of rows: "))
print_inverted_triangle(n)
