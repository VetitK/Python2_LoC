year = int(input())  # 2012

# assert year < 2024
# < 1900, > 2023
if year < 1900 or year > 2023:
    raise TypeError('can only concatenate str (not "int") to str')
print(2023 - year)
