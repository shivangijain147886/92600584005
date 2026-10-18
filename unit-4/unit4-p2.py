class student:
    def__init__(self):
        print("constructor is called")
    def__del__(self):
        print("deconstructor is called ")

s1 = student()
del s1
