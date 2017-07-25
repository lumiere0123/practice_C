#Define a class Pet that contains three object (instance) variables: name, species, and age. 
#The constructor for Pet should take arguments (in the listed order) that initialize these variables.

class BankAccount(object):

    interest_rate = 0.3

    def __init__(self, owner, balance=1000):
        self.owner = owner
        self.balance = balance
    def withdraw(self, amt):

        if self.balance >= amt:
            self.balance = self.balance - amt
            return True
        else:
            return False

    def deposit(self, amt):
        
        self.balance =+ amt
        return self.balance
    def check_balance(self):
        return self.balance

    def __str__(self):
        status = "owner: " + str(self.owner) + " balance: " +str(self.balance) + " int: " + str(self.interest_rate)
        return status


    def __eq__(self, other):
        return self.owner == other.owner and self.balance == other.balance


b1 = BankAccount("Roy", 100)
b2 = BankAccount("Roy", 100)


print(str(b1==b2))


##b1 = BankAccount("John", 100)
#b1 = BankAccount("John",10000)
#b2 = BankAccount("Roy", 100)
#
#print(b1)
#b1.withdraw(100)
#
#
#print(b1.check_balance())
#
#print("interest:" + str(b1.interest_rate))
#print("balance:" + str(b1.balance))
 




