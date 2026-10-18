class Father:
    def show(self):
        print("Father class")

class Mother:
    def show(self):
        print("Mother class")

class Child(Father, Mother):
    def __str__(self):
        return "Child object created"

c = Child()
c.show()
print(Child.mro())
print(c)
