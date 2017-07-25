def get_team(athlete_to_sports, sport):
    """ (dict of {str: list of str}, str) -> list of str
   
    Return a sorted list of the athletes from athlete_to_sports who play 
    sport. In athlete_to_sports, each key is an athlete and each value is a 
    list of sports that athlete plays.

    >>> D = {'MC': ['run','hockey'],'JC': ['run'],'BP':['run','swim','bike']}
    >>> get_team(D, 'run')
    ['BP', 'JC', MC']
    >>> get_team(D, 'bike')
    ['BP']
    """

    team = []
    for athlete in athlete_to_sports:
        sports_for_athlete = athlete_to_sports[athlete]
        if sport in sports_for_athlete:
            team.append(athlete)
    team.sort()
    return team
        
#At first we did
#return team.sort()
#Why was this wrong? 

#Remember that method sort() sorts the list **in-place**
#and returns the value None. But in our case we want the function to 
#return the new list team and not None. 