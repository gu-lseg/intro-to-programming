import random


class Python():

    def __init__(self, name, sex, age, length):
        self.name = name
        self.sex = sex
        self.age = age
        self.length = length

    def move(self):
        print("{} slithers".format(self.name))

    def eat(self):
        """ a snake gets longer when it eats """
        self.length = self.length + 1

    def starve(self):
        """ a snake shorter when it starves """
        # is there a bug here?
        self.length = self.length - 1

    def __lt__(self, other):
        return self.length < other.length

    def __gt__(self, other):
        return self.length > other.length

    def __add__(self, other):
        if self.sex == other.sex:
            return None
        new_name = self.name + other.name
        sex = random.choice(['M', 'F'])
        return Python(new_name, sex, 0, 1)

    def __str__(self):
        body = '=' * self.length
        return "{}>  {}".format(body, self.name)


# Example run

# jane = Python('Jane', 'F', 4, 6)
# john = Python('John', 'M', 15, 4)
# print(john)
# print(jane)
# jane < john
# jane > john
# jane + john
# baby = jane + john
# print(baby)
