def add_sighting(sightings, new_sighting):
    '''(dict, str) -> None
    Update the dictionary of sightings with the new_sighting.

    >>> animals = {'cat': 1, 'dog': 2}
    >>> add_sighting(animals, 'goose')
    >>> animals
    {'cat': 1, 'goose': 1, 'dog': 2}
    >>> add_sighting(animals, 'dog')
    >>> animals
    {'cat': 1, 'goose': 1, 'dog': 3}
    '''

    sightings[new_sighting] = sightings.get(new_sighting, 0) + 1
    

def invert_sightings(sightings):
    '''(dict {str:int}) -> dict {int:str}
    Return a dictionary which is sightings inverted.
    (Every key is now a value. Its key was its original value.)
    
    >>> animals = {'cat': 1, 'dog': 3}
    >>> invert_sightings(animals)
    {1:'cat', 3: 'dog'}
    '''
    
    inverted = {}
    
    for (key, value) in sightings.items():
        inverted.setdefault(value, []).append(key)
        
        # The line above, using setdefault, does the following:
        #inverted[value] = inverted.get(value, [])
        #inverted[value].append(key)
    
    return inverted
    
    
def invert_inverted_sightings(inverted_sightings):
    '''(dict {int:[list of str]}) -> dict {str:int}
    Return a new dictionary which is the inverted dictionary
    inverted again (restored).
    '''

    inverted = {}
    
    for (key, value) in inverted_sightings.items():
                
        # value is now a list, so we need to iterate through it
        for obj in value:
            inverted[obj] = key
    
    return inverted
    

if __name__ == "__main__":
    animals = {'cat': 1, 'dog': 2}
    add_sighting(animals, 'goose')
    print(animals)
