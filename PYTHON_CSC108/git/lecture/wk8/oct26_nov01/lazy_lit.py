import random

def make_dictionary(f):
    '''(file) _> dict of {str: list of str}
    Return a dictionary where the keys are words in f and 
    the value for a key is the list of words that follow 
    it in f.
    '''
    
    d = {}
    context = ''
    for line in f:
        words = line.strip().split()
        for word in words: 
            d.setdefault(context, []).append(word)
            context = word
    
    return d


def mimic_text(word_dict, num_words):
    '''(dict of {str: list of str}, int) -> str
    Return a string that mimics the text encoded in word_dict.
    The string must be of length num_words.
    '''
    
    story = []
    context = ''
    for i in range(num_words):
        possible_words = word_dict[context]
        rand_index = random.randint(0, len(possible_words) - 1)
        context = possible_words[rand_index]
        story.append(context)
    
    return ' '.join(story)


if __name__ == "__main__":
    words = make_dictionary(open("shakespeare.txt"))
    print(mimic_text(words, 200))