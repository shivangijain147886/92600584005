class Payment:
    def pay(self):
        print("Payment process")

class UPI(Payment):
    def pay(self):
        print("Payment through UPI")

class Card(Payment):
    def pay(self):
        print("Payment through Card")

p1 = UPI()
p2 = Card()

p1.pay()
p2.pay()
