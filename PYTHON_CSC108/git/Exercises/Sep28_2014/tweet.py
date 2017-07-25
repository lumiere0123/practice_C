MIN_LENGTH = 1
MAX_LENGTH = 140


def is_valid_tweet(tweet):
    """ (str) -> bool

    Return True if and only if tweet is no less than 1 and no more
    than 140 characters long.

    >>> is_valid_tweet('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper')
    True
    >>> is_valid_tweet('The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand them clearly. - Donald Knuth')
    False
    """
    if len(tweet) >= 1 and len(tweet) <= 140:
        return True
    else:
        return False


def contains_hash_symbol(tweet):
    """ (str) -> bool

    Return True iff tweet contains a hash symbol(#).

    >>> contains_hash_symbol("#")
    True
    >>> contains_hash_symbol("Hello#")
    True
    >>> contains_hash_symbol("")
    False
    >>> contains_hash_symbol("Hello")
    False
    """
    if '#' in tweet:
        return True
    else:
        return False



def is_mentioned(tweet, username):
    """ (str, str) -> bool

    Return True iff tweet mentions username proceded by @

    >>> is_mentioned("Hello @dan", "dan")
    True
    >>> is_mentioned("Hello @dan", "@dan")
    False
    >>> is_mentioned("Hello @dancing", "dan")
    True
    >>> is_mentioned("Hello @adan", "dan")
    False
    >>> is_mentioned("Hello adan", "dan")
    False
    >>> is_mentioned("@dan there", "dan")
    True
    """
    if "@" + username  in tweet:
        return True
    else:
        return False

def report_shortest(first_tweet, second_tweet):
    """ (str, str) -> str

    Return
        'Tweet 1' when first_tweet is shorter than second_tweet
        'Tweet 2' when second_tweet is shorter than first_tweet
        'Same length' when the tweets have the same length

    >>> report_shortest("","")
    'Same length'
    >>> report_shortest("A","")
    'Tweet 2'
    >>> report_shortest("A","ABC")
    'Tweet 1'
    >>> report_shortest("abc","ABC")
    'Same length'
    """
    if len(first_tweet) > len(second_tweet):
        return 'Tweet 2'
    if len(first_tweet) < len(second_tweet):
        return 'Tweet 1'
    else:
        return 'Same length'



def is_reply(tweet):
    """ (str) -> bool

    Return True iff tweet is a reply, which starts with @ symbol

    >>> is_reply("")
    False
    >>> is_reply("@")
    False
    >>> is_reply("a @hello")
    False
    >>> is_reply("@a")
    True
    >>> is_reply("@a hello")
    True
    """
    if  len(tweet) > 1 and tweet[0] == "@":
        return True
    else: 
        return False

def format_reply_to(username_or_at_username, tweet):
    """ (str, str) -> str

    Return a reply tweet which consists of @username followed by space
    followed by tweet. If the reply tweet is more than 140, return
    a exceeding number followed by ' characters too long'

    >>> my_tweet = "This is message of 135 char long dummy " \
        + "dummy dummy dummy Hello, This is message of 135 char " \
        + "long dummy dummy dummy dummy dummy dummy du"

    >>> format_reply_to("@123",my_tweet)
    '@123 This is message of 135 char long dummy dummy dummy \
dummy Hello, This is message of 135 char long dummy dummy \
dummy dummy dummy dummy du'

    >>> format_reply_to("123",my_tweet)
    '@123 This is message of 135 char long dummy dummy dummy \
dummy Hello, This is message of 135 char long dummy dummy \
dummy dummy dummy dummy du'

    >>> format_reply_to("@123456",my_tweet)
    '3 characters too long'

    >>> format_reply_to("1234",my_tweet)
    '1 characters too long'
    """


    if username_or_at_username[0] == "@":
        username = username_or_at_username
    else:
        username = "@" + username_or_at_username  

    tweet_body = username + " " + tweet


    if len(tweet_body) > 140:
        return str(len(tweet_body) - 140) + ' characters too long'
    else:
        return tweet_body



    ##if "@" in username_or_at_username:
    ##    if len(username_or_at_username) + len(" ") + len(tweet) > 140:
    ##        return str(len(username_or_at_username) + len(" ") + len(tweet) - 140) + " " + "characters too long"
    ##    else:
    ##       if len("@" + username_or_at_username) + len(" ") + len(tweet) > 140:
    ##            return str(len("@" + username_or_at_username) + len(" ") + len(tweet) - 140) + " " + "characters too long"


    ##else:
    ##    if "@" in username_or_at_username:
    ##        return username_or_at_username + " " + tweet
    ##    else:
    ##        return "@" + username_or_at_username + " " + tweet
# Define the other functions described in the handout here.

import doctest
doctest.testmod()
