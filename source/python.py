class Python():

    def __init__(self, name, sex, age, length):
        self.name = name
        self.sex = sex
        self.age = age
        self.length = length

    def move(self):
        print("{} moves".format(self.name))

