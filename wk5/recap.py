# recap
class Person:
    def __init__(self, name):
        # properties
        self.name = name
        self.age = 21
    
    def greetings(self):
        print(f"Hello, my name is {self.name}")

# vetit = Person()
title = Person(name="Aerial")
title.greetings()