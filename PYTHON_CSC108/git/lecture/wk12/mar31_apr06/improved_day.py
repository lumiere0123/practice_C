import event

class Day:

    """A calendar day and its events."""

    def __init__(self, day=1, month='January', year=2014):
        """ (Day, int, str, int) -> NoneType

        Initialize a day on the calendar with day, month and year,
        and no events. Default values for day, month and year are 1,
        'January' and 2014 respectively.

        >>> d = Day(5, 'April', 2014)
        >>> d.day
        5
        >>> d.month
        'April'
        >>> d.year
        2014
        >>> d.events
        []
        """
        
        self.day = day
        self.month = month
        self.year = year
        self.events = []
        
        
    def schedule_event(self, new_event):
        """ (Day, Event) -> bool
    
        Return True if and only if new_event doesn't overlap with any existing
        event on this day.
        
        >>> d = Day(26, 'March', 2014)
        >>> e = event.Event(11, 12, 'Meeting')
        >>> d.schedule_event(e)
        True
        >>> e2 = event.Event(11, 14, 'coffee')
        >>> d.schedule_event(e2)
        False
        """
        
        for scheduled_event in self.events:
            if scheduled_event.overlaps(new_event):
                return False
        
        self.events.append(new_event)
        return True
        
         
    def __str__(self):
         """ (Day) -> str
 
         Return a string representation of this day.
 
         >>> d = Day(4, 'April', 2014)
         >>> d.schedule_event(event.Event(13, 14, 'Submit last exercise'))
         True
         >>> d.schedule_event(event.Event(19, 23, 'Celebrate end of classes'))
         True
         >>> print(d)
         4 April 2014:
         - Submit last exercise: from 13 to 14
         - Celebrate end of classes: from 19 to 23
         """
         
         day_representation = "{0} {1} {2}:".format(self.day, self.month,
                                                    self.year)
         
         for item in self.events:
             day_representation += "\n- " + str(item)
         return day_representation
 
         
        
if __name__ == '__main__':
    
    import doctest
    doctest.testmod()

    # Create New Year's day 2014
    new_year_day = Day()
    print(new_year_day)

    # Create someone's birthday
    birthday1 = Day(2, 'April')
    print(birthday1)

    # Create the first day of classes this term: January 6, 2014
    first_day = Day(6)
    print(first_day)

    # Create Canada Day, 2014
    canada_day = Day(month='July')
    print(canada_day)

    #All print statements in the main program were added 
    #simply to demonstrate that our code works. 
        