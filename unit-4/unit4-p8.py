# Practical 8: Encapsulation and Abstraction

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def show_interest(self):
        pass

class SBI(Bank):
    def __init__(self):
        self.__rate = 7  # Private variable (encapsulation)

    def show_interest(self):
        print("Interest Rate:", self.__rate, "%")

account = SBI()
account.show_interest()
