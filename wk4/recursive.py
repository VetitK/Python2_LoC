# วนซ้ำ, function return ตัวมันเอง

def minus_by_2(x: int) -> int:
    result = x - 2
    if result < 0:
        return x
    return minus_by_2(result)

print(minus_by_2(6))

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(3))
# factorial(3) = 3 * factorial(2) = 6
# factorial(2) = 2 * factorial(1) = 2
# factorial(1) = 1 * factorial(0) = 1
# factorial(0) = 1
