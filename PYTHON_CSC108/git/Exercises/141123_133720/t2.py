class iPod(object):    
    def __init__(self, max_song_capacity):
        self.max_song_capacity = max_song_capacity
        self.library = {}    # Should contain str -> list of str
        # { 
        #   'a': ['aa', 'bb'],
        #   'b': ['bb', 'bb' ]
        # }  
        self.num_songs = 0
    
    def space_available(self):
        '''(iPod) -> int
        Return the number of songs that may be stored in the space remaining on this device.
        '''
        return self.max_song_capacity - self.num_songs

 
    def add_song(self, artist, song_name):
        '''(iPod, str, str) -> bool
        Return True and add the requested song to the device iff there is space remaining.
        Note: Do not worry about duplicate songs. Do worry about having multiple songs by the same artist!
        '''
        if self.space_available() == 0:
            return False
        else:
            self.num_songs += 1
            self.library.setdefault(artist, [song_name]).append(song_name)
            return True
            
    def song_in_library(self, artist, song_name):
        '''(iPod, str, str) -> bool
        Return True iff song_name by artist is in the library.
        '''
        #songs=self.library[artist]
        songs=self.library.get(artist)
        
        # special case
        if songs == None:
            return False

        return song_name in songs


i1=iPod(2)
print("ACT: ",i1.space_available()         , " EXP: ", 2)
print("ACT: ",i1.add_song('a1','s1')       , " EXP: ", True)
print("ACT: ",i1.add_song('a2','s2')       , " EXP: ", True)
print("ACT: ",i1.add_song('a3','s3')       , " EXP: ", False )
print("ACT: ",i1.song_in_library('a1','s1'), " EXP: ", True  )
print("ACT: ",i1.song_in_library('a1','s3'), " EXP: ", False )
print("ACT: ",i1.song_in_library('a1','')  , " EXP: ", False )
print("ACT: ",i1.song_in_library('a4','a') , " EXP: ", False )
print("ACT: ",i1.song_in_library('','a')   , " EXP: ", False )



