# 1 in 1 out
def square(x):
    result = x ** 2
    return result

# n = int(input())
# square_of_n = square(n)
# print(square_of_n)

# print(square(n))

# many in 1 out


def power(x, y):
    result = x ** y
    return result


# print(power(3, 5))

# 0 in 1 out

def introduce():
    print('Hi my name is Prayuth ChanOcha.')
    return "P'Ve"


introduce()


# 1 in many out
def find_square_and_sqrt(x):
    sqrt_of_x = x ** 0.5
    square_of_x = x ** 2
    return sqrt_of_x, square_of_x


print(find_square_and_sqrt(9))

# 1 in 0 out


def send_help(name):
    print(f"กำลังส่งความช่วยเหลือให้ {name}")
    # return None

result = send_help("Vetit")
print(result)
