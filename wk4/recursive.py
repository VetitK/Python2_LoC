# วนซ้ำ, function return ตัวมันเอง
import time


def minus_by_2(x: int) -> int:
    result = x - 2
    if result < 0:
        return x
    return minus_by_2(result)

# print(minus_by_2(6))


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

# print(factorial(3))
# factorial(3) = 3 * factorial(2) = 6
# factorial(2) = 2 * factorial(1) = 2
# factorial(1) = 1 * factorial(0) = 1
# factorial(0) = 1


def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# f(4) = f(3) + f(2) = 1 + 1 = 2
# f(3) = f(2) + f(1) = 1 + 0 = 1
# f(7)= 8, f(11) = 55


def fibonacci_dp(n: int) -> int:
    dp = [0 for _ in range(n)]
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]


t1 = time.time()
print(fibonacci_dp(100000000))
# print(fibonacci(40))
t2 = time.time()
print(round(t2-t1, 10))
