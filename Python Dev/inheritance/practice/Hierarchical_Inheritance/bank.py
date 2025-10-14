class Bank:
    def loan_interest(self):
        print("Base interest: 8%")

class SBI(Bank):
    def loan_interest(self):
        print("SBI interest: 7.5%")

class HDFC(Bank):
    def loan_interest(self):
        print("HDFC interest: 7.8%")

class ICICI(Bank):
    def loan_interest(self):
        print("ICICI interest: 8.2%")

for bank in [SBI(), HDFC(), ICICI()]:
    bank.loan_interest()