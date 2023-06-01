def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return b


def product(l: list):
    result = 1
    for number in l:
        result *= number

    return result


name = input()
age = 20

print(f"Hello, my name is {name}") # Format String
