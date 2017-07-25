class Card: 

    balance = 0
    owner = ""
    default_reload = 0

    def __init__(self, owner, balance, default_reload):
        self.owner = owner
        self.balance = balance
        self.default_reload = default_reload

    def __str__(self):
        return "Owner: " + self.owner + "Balance: " + str(self.balance)

    def __repr__(self):
        return "HELLO" 

    def reload_default(self):
        self.reload(self.default_reload)

    def buy_coffee(self, amt_paid):
        if amt_paid <= self.balance:
            self.balance -= amt_paid
            return True
        else:
            return False

    # add amt to reload
    def reload(self,  amt):
        self.balance += amt


if __name__ == '__main__':
    card_for_karen = Card("Karen", 100, 50)

    
    #count=0
    #while ( count < 26 )
    #    card_for_karen.buy_coffee(2.5) 
    #    count=+count
    
    for dummy in range(25):
        card_for_karen.buy_coffee(2.5) 

    
    card_for_sven = Card("Sven", 50, 20)

    card_for_sven.buy_coffee(5)

    card_for_karen.reload_default() 
    
    card_for_sven.reload(5.72)
   
    print(card_for_karen) 
    print(card_for_sven) 
 

    a=[ card_for_sven, card_for_karen]
    b={ 'a': card_for_sven}
    print(a) 
    print(b) 


    
