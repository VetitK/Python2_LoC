def product(d, *args):
    result = 1
    for number in args:
        result *= number
    result += d
    return result


# print(product(2, 4, 5))

def greetings(name: str ='Vetit',**kwargs):
    # name, nationality
    print(
        f"Hello, my name is {kwargs['name']}, I am {kwargs['nationality']}. I am {kwargs['age']} years old.")
    if kwargs['isJebKhee']:
        print(f'ห้องน้ำอยู่ไหน')


greetings(name="Vetit", nationality="SmurfMartian",
          age=20, สันดาน="Lawful Evil", isJebKhee=False)

def _sum(a, b, *args, w=4, y=5, **kwargs):
    return a + b + args[0] + args[-1] + w + y + kwargs['z']

# print(_sum(1, 2, 4, 5, 7, w=0, y=6, z=9))
print(_sum(1, 2, 5, x=4, z=10))