from abc import ABC,abstractmethod

class Payment(ABC):
    def print_slip(self,amount):
        print("purchase of Amount",amount)
    @abstractmethod
    def payment(self):
        pass

class CreditCardPalyment(Payment):
    def payment(self,amount):
        print("credit card payment of ",amount)


class mobil_Wallet(Payment):
    def payment(self,amount):
        print("mobile payment of ", amount)

c = CreditCardPalyment()
c.payment(100)
c.print_slip(100)

m = mobil_Wallet()
m.payment(200)
m.print_slip(200)




# create car inherit it to the suzuki and tata