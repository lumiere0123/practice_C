def add_sighting(kinds, counts, sighting):
    '''(list of str, list of int, str) -> NoneType
    Update the list of types of items seen and the list
    of times each item has been seen.

    >>> animals = ['cat', 'dog']
    >>> counts = [1, 2]
    >>> add_sighting(animals, counts, 'goose')
    >>> animals
    ['cat', 'dog', 'goose']
    >>> counts
    [1, 2, 1]
    >>> add_sighting(animals, counts, 'dog')
    >>> animals
    ['cat', 'dog', 'goose']
    >>> counts
    [1, 3, 1]
    '''

    if sighting in kinds:
        index = kinds.index(sighting)
        counts[index] += 1
    else:                  # Not in the list
        kinds.append(sighting)
        counts.append(1) 

        
def add_sighting_v2(sightings, new_sighting):
    '''(dict, str) -> None
    Update the dictionary of sightings with the new_sighting.
    '''

    sightings[new_sighting] = sightings.get(new_sighting, 0) + 1