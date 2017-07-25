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


 
                   
if __name__ == '__main__':

    import doctest
    doctest.testmod()
