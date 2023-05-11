# global scope, local scope

a = 5 # global

# def f(): # global
#     print(a) # global
# f()

# def g():
#     a = 3 # local
#     print(a) # local
# g()
# print(a) # global

# def h():
#     a += 3 # local
#     print(a) # local
    
# h()

def j():
    global a
    a += 3 # global
    print(a) # global
    
j()

a = 5 # global
def f():
    a = 4 # local บน f
    def g():
        a = 2 # local บน g