# Original problem ...
# Given a server's response time:
# return "server down" if there was no response (response time is none)
# return "server slow" if the response takes longer than 5000 ms
# return "server okay" if it returns a fast response_time

# We define a global value below, so that we can easily alter the value that
# triggers the "slow response" message if a client/boss requests a change.
SLOW_RESPONSE = 5000
def server_status(response_time):
    '''(int/None) -> str
    Given a server's response time, return "server down" if there was 
    no response, "server slow" if the response took longer than 5000
    ms, and "sever okay" otherwise.

    >>> server_status(None)
    'server down'
    >>> server_status(0)
    'server okay'
    >>> server_status(4500)
    'server okay'
    >>> server_status(5000)
    'server okay'
    >>> server_status(5500)
    'server slow'
    '''

    if response_time == None:
        return "server down"
    elif response_time > SLOW_RESPONSE:
        return "server slow"
    else:
        return "server okay"
