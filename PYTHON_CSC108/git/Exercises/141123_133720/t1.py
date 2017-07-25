class RealEstateSystem:

    # Constructor
    def __init__(self):
        """ (RealEstateSystem)
        Initialize the homes list
        """
        self.homes = []

    def add_home(self, home):
        """ (RealEstateSystem, Home) -> NoneType
        Adds a home to our system
        """
        self.homes.append(home)
    
    def extract_minimum_price(self):
        """ (RealEstateSystem) -> int
        Return the lowest priced home in the system, or -1 if there are no houses in the system
        """
        # mtd.1

        #saved_min=0
        ## iterate each of home in homes
        #for home in self.homes:
        #    # save only min value 
        #    curr_price = home.price
        #    if saved_min == 0:
        #        saved_min = curr_price
        #    else:
        #        if saved_min >= curr_price:
        #            saved_min = curr_price
        #  
        #if saved_min == 0:
        #    return -1  
        #else:
        #    return saved_min

        # mtd.2

        prices=[]
        # iterate each of home in homes
        for home in self.homes:
            prices.append(home.price)

        if len(prices) == 0:
            return -1  
        else:
            return min(prices)

class Home:
    """ An instance of a home """
    def __init__(self, price):
        """ (Home, float)
        Initialize a home
        """
        self.price = price



r=RealEstateSystem()
h1 = Home(10)
h2 = Home(30)
h3 = Home(20)
r.add_home(h1)
r.add_home(h2)
r.add_home(h3)
print(r.extract_minimum_price())

r2=RealEstateSystem()
print(r2.extract_minimum_price())
