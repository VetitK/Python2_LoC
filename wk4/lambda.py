def square(x: int) -> int:
    result = x ** 2
    return result


lambda x: x ** 2


def product(a, b, c):
    return a * b * c


lambda a, b, c: a * b * c


def get_last_element(l: list):
    return l[-1]


lambda l: l[-1]


# key
scores = [('B_Vetit', 94), ('C_Tiew', 1), ('A_Title', 81)]
scores.sort(key=lambda x: x[1], reverse=True)

print(scores)

# filter
nums = [2, 3, 6, 7, 8, 12, 15]


def is_odd_number(x: int) -> bool:
    return x % 2 != 0


print(*filter(lambda x: x <= 6, nums))
