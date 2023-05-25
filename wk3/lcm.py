from gcd import gcd_euclidean

def lcm_version1(x , y):
    start = 1
    while True:
        if start % x == 0 and start % y == 0:
            return start
        start += 1

def lcm_version2(x , y):
    start = max(x, y)
    while True:
        if start % x == 0 and start % y == 0:
            return start
        start += 1

def lcm_version3(x , y):
    start = max(x, y)
    while True:
        if start % x == 0 and start % y == 0:
            return start
        start += max(x, y)

def lcm_tidpro(x, y):
    return x * y / gcd_euclidean(x, y)