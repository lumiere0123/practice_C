import event

class Day:
    """A calendar day and its events."""

    def __init__(self, day, month, year):
        """ (Day, int, str, int) -> NoneType
       
        Initialize a day on the calendar with day, month and year,
        and no events.

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
        """ (Day, Event) -> NoneType

        Schedule new_event on this day, even if it overlaps with
        an existing event. Later we will improve this method.

        >>> d = Day(26, 'March', 2014)
        >>> e = event.Event(11, 12, 'Meeting')
        >>> d.schedule_event(e)
        >>> d.events[0] == e
        True
        >>> e2 = event.Event(15, 16, 'Coffee')
        >>> d.schedule_event(e2)
        >>> d.events[1] == e2
        True
        """
        
        self.events.append(new_event)

     
    def __str__(self):
        """ (Day) -> str

        Return a string representation of this day.

        >>> d = Day(4, 'April', 2014)
        >>> d.schedule_event(event.Event(13, 14, 'Submit last exercise'))
        >>> d.schedule_event(event.Event(19, 23, 'Celebrate end of classes'))
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

    #import doctest
    #doctest.testmod()
    
    # Create day 5 April 2014.
    d = Day(5, 'April', 2014)
    #print(d)
    #Careful! the print statements, commented out here, were simply added
    #for demonstration purposes during lecture. Your code should NOT have any
    #print statements except for the last one where we
    #ask you to print the day.
    
    # Add an event "Sleep in" from 0 to 11 on 5 April 2014.
    sleep_event = event.Event(0, 11, "Sleep in")
    d.schedule_event(sleep_event)
    #print(d)

    # Add an event "Brunch" from 11 to 13 on 5 April 2014.
    d.schedule_event(event.Event(11, 13, "Brunch"))
    #print(d)
    
    # Print the day 5 April 2014, including its events
    print(d)
    
    
