class A:
    def show(self):
        print("class A")

class B(A):
    pass

b = B()
b.show()

class C(B):
    pass

c=C()
c.show()

class X:
    def display1(self):
        print("class X")

class Y:
    def display2(self):
        print("class Y")

class Z(X,Y):
    pass

z=Z()
z.display1()
z.display2()
