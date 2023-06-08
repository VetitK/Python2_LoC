class Person:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

    def calculate_BMI(self):
        # weight / height (m) ** 2
        bmi = self.weight / ((self.height / 100) ** 2)
        return bmi


vetit = Person(age=80, height=161, weight=52)
title = Person(age=12, height=163, weight=46)
# print(title.age)
print(title.calculate_BMI())
print(vetit.calculate_BMI())

l = [1,2]
l.append()