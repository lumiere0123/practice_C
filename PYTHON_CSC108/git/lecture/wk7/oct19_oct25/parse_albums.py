def count_albums(albums):
    '''(file) -> dict
    Return a dictionary that contains mappings between 
    the artists in the file albums and the number of 
    albums they have authored.
    '''
    
    albums.readline()
        
    album_dict = {}
    for line in albums:
        fields = line.strip().split(",")
        artist = fields[0]
        album_dict[artist] = album_dict.get(artist, 0) + 1
        
    return album_dict