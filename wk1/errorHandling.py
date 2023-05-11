try:
    print('Program STARTO')
    print(2/0)  # ZeroDivisionError
    print(vetit)  # NameError
except NameError:
    print('There is a NameERR!')
except ZeroDivisionError:
    print('You cannot divide a number by 0.')
else:
    print('Hooray there is no ERR.')
finally:
    print('ENDED')
print('Finished')


