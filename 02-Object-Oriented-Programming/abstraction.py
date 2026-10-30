from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(Payment):
    def process_payment(self, amount):
        print("Credit Card Payment:", amount)

class UPI(Payment):
    def process_payment(self, amount):
        print("UPI Payment:", amount)

payment1 = CreditCard()
payment2 = UPI()

payment1.process_payment(2500)
payment2.process_payment(1500)
