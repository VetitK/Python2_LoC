import time


def gcd_version1(x, y):
    start = max(x, y)
    while True:
        if (x % start == 0) and (y % start == 0):
            return start
        start -= 1

# gcd(a,b) <= min(x, y)


def gcd_version2(x, y):  # 24, 102
    start = min(x, y)
    while True:
        if (x % start == 0) and (y % start == 0):
            return start
        start -= 1


# Euclid
def gcd_euclidean(x, y):
    while y != 0:
        x, y = y, x % y

    return x


t1 = time.time()
gcd_version1(137690, 298)
t2 = time.time()
gcd_version2(137690, 298)
t3 = time.time()
gcd_euclidean(137690, 298)
t4 = time.time()

print(t2-t1, (t3-t2), (t4-t3))
