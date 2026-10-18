class student:
    college = "marwadi college"

    def instance_method(self):
        print("insstance method")

    @classmethod
    def class_method(cls):
        print("College:", cls.college)

    @staticmethod
    def static_method():
        print("Welcome to Python")

s1 = student()
s1.instance_method()
student.class_method()
student.static_method()
