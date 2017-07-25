from bankaccount import BankAccount

class SavingsAccount(BankAccount):
    interest_rate = .03
    
    def calculate_interest(self):
        return self._balance * self.interest_rate