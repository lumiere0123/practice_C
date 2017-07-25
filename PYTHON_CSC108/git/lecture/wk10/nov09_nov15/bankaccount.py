class BankAccount(object):
    interest_rate = .03             # A class attribute
    
    # Constructor with default parameter
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance     # A "private" member
        
    def withdraw(self, amt):
        '''(int) -> bool
        Return True iff there are sufficient funds to cover the 
        withdrawal. If there are enough funds, deduct from balance.
        '''
        if self._balance >= amt:
            self._balance -= amt
            return True
        return False
    
    def deposit(self, amt):
        '''(int) -> int
        Return the new balance after depositing amt.
        '''
        self._balance += amt
        return self._balance

    @property
    def balance(self):
        '''() -> int
        Return the account's balance.
        '''
        return self._balance
        
    # With the two functions below, this no longer functions like a bank
    # account. Do you want someone to be able to delete their balance?
    # Or modify it directly?  We would not normally provide these. If we 
    # didn't, it wouldn't be possible for someone to directly manipulate 
    # the balance variable.
    @balance.setter
    def balance(self, value):
        self._balance = value
        
    @balance.deleter
    def balance(self):
        self._balance = 0

    # Remember: attributes and methods that start with __ are used by the
    # system. In this case, __str__ is invoked whenever you use str(...)
    def __str__(self):
        '''() -> str
        Return a str representation of the object.
        '''
        return "%s's bankaccount (%d)" % (self.owner, self._balance)
        