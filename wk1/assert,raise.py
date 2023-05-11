try:
    year = int(input())
except ValueError:
    print(' You must enter an integer.')
    year = int(input())
assert (1900 <= year) and (year <= 2023), 'ปีที่ใส่มาควรจะอยู่ในช่วง 1900 ถึง 2023'
print(2023 - year)
