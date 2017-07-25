def generate_random_story(training_file, context_length, num_words):
    """ (file open for reading, int, int) -> str

    Return a randomly generated story with num_words words based on a context
    of context_length words from the text in training_file.
    """
    
    #read the file into a single string and separate it into words (split)
    words = training_file.read().split()
    
    #Create a dictionary which maps context to a list of possible
    #words, based on all the words we read from the training file
    context_to_words = build_dictionary(words, context_length)
    
    #Generate a story with num_words words from context_to_words
    #dictionary
    new_story = generate_story(context_to_words, num_words, context_length)

    return new_story


def build_dictionary(words_list, context_length):
    """(list of str, int) -> dict of {tuple of str: list of str}
    
    Return a dictionary where each key is a tuple of words from
    words_list that form a context of context_length words and each
    value is a list of all possible words from words_list that
    follow this context.
    
    >>> #To do: Add a docstring example here
    """
    # *********  Work on this on your own!  *************** 
    
    #Design Decision: Assume you have this list ["to", "be"] and
    #a context_length of 1. How will your dictionary look like?
    #Here are two options:
    #{("to",) : ["be"]}
    #{("to",) : ["be"], ("be,") : []}
    #I made the first decision, which will influence the range for my
    #for loop below.
    
    #create an empty dictionary
    context_to_words = {}
    
    #loop over words_list and find out all possible contexts (keys)
    #Add their possible next words (values) to the dictionary
    
    for i in range(len(words_list) - context_length):
        #get current context using list slicing
        #words_list[i : i + context_length]
        current_context = words_list[i : i + context_length]
        
        #covert context into a tuple
        current_context = tuple(current_context)
        
        #get the next word
        next_word = words_list[i + context_length]

        #properly add that context (if new) and its next word to dictionary
        if current_context not in context_to_words:
            context_to_words[current_context] = []
        #append the next word
        context_to_words[current_context].append(next_word)
        
    #return the dictionary
    return context_to_words


def generate_story(context_to_possible_words, num_words, context_length):
    """
    """
    
    # *********  Work on this on your own!  *************** 

    #have an empty string as accumulator for my new story
    story = ""
    
    #randomly choose starting context (a key) which consists of 
    #context_length words. We pick a non-existent context and
    #do the random selection in the for-loop.
    current_context = None
    
    #Until I've written num_words, repeat the following:
    for i in range(num_words):
        if current_context not in context_to_possible_words:
            current_context = select_random_key(context_to_possible_words)

        #Based on current context, find possible next words and 
        #randomly pick one
        possible_words = context_to_possible_words[current_context]
        next_word = random.choice(possible_words)
        
        #write it into my story
        story += " " + next_word
        
        #update current context
        current_context = current_context[1:] + (next_word,)
        
    #return my new story (skip the first space if we want to be precise)
    return story[1:]


def select_random_key(context_to_possible_words):
    """(dict of (tuple of str : list of str)) -> tuple of str
    
    Return a random key from context_to_possible words
    """
    
    all_keys = []
    for key in context_to_possible_words:
        all_keys.append(key)
    return random.choice(all_keys)

    #An alternative solution to the for loop would be:
    #all_keys = list(context_to_possible_words.keys())
    #return random.choice(all_keys)
