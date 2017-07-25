class Event:    
    """A new calendar event."""

    def __init__(self, start_time, end_time, event_name):
        """ (Event, int, int, str) -> NoneType

        Precondition: 0 <= start_time < end_time <= 23
        
        Initialize a new event that starts at start_time, ends at end_time,
        and is named event_name.

        >>> e = Event(12, 13, 'Lunch')
        >>> e.start_time
        12
        >>> e.end_time
        13
        >>> e.name
        'Lunch'
        """
        
        self.start_time = start_time
        self.end_time = end_time
        self.name = event_name


    def rename(self, new_name):
        """ (Event, str) -> NoneType

        Change the name of this event to new_name.
        
        >>> e = Event(12, 13, 'Lunch')
        >>> e.rename('Breakfast')
        >>> e.name
        'Breakfast'
        """
        
        self.name = new_name

    def duration(self):
        """ (Event) -> int

        Return the duration of this event.

        >>> e = Event(10, 11, 'Lecture')
        >>> e.duration()
        1
        """
        
        return (self.end_time - self.start_time)

    
    def __str__(self):
        """ (Event) -> str

        Return a string representation of this event.

        >>> e = Event(6, 7, 'Run')
        >>> str(e)
        'Run: from 6 to 7'
        """
        
        #return self.name + ": from " + str(self.start_time) + " to " + \
        #       str(self.end_time)

        # If this special __str__ method is not defined then str(e) in the docstring
        # example would print the memory address of this Event object.
              
        return "{0}: from {1} to {2}".format(self.name, self.start_time,\
                                             self.end_time)

    def __eq__(self, other):
        """ (Event, Event) -> bool

        Return True iff this event has the same start time, end time, 
        and name as other.

        >>> e1 = Event(6, 7, 'Run')
        >>> e2 = Event(10, 11, 'Sleep')
        >>> e1 == e2
        False
        """

        # If this special __eq__ method is not defined then e1 == e2 in the docstring
        # would compare the memory addresses of Event objects e1 and e2.

        # You can also use e1.__eq__(e2) instead of e1 == e2 in the docstring. 
        
        return (self.start_time == other.start_time) and \
               (self.end_time == other.end_time) and \
               (self.name == other.name)

    def overlaps(self, other):
        """ (Event, Event) -> bool

        Return True iff this event overlaps with event other.

        >>> e1 = Event(6, 7, 'Run')
        >>> e2 = Event(0, 7, 'Sleep')
        >>> e1.overlaps(e2)
        True
        """
        
        return not ((self.end_time <= other.start_time) or \
        (other.end_time <= self.start_time))
    
        #DeMorgan's law
        #not (a or b) <=> (not a) and (not b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
