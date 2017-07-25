##########  Provided helper function. ############


def clean_up(s):
    r""" (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """

    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result


def create_word_count(text):
    r""" (list of str) -> list of str and int

    Return an empty list when 'text' does not contain a word. Otherwise,
    return a list which even index stores 'word' and odd index stores
    the corresponding of 'word' occurrences from 'text'

    >>> create_word_count(['a','b'])
    ['a', 1, 'b', 1]
    >>> create_word_count(['a','b','a'])
    ['a', 2, 'b', 1]
    >>> create_word_count(['!!!\n', 'a\n','b\n','a\n'])
    ['a', 2, 'b', 1]
    >>> create_word_count(['\n'])
    []
    """
    FOUND_WORD_INCREASE = 1
    COUNT_IDX_OFFSET = 1

    # [<word1> , <num-of-word1>, <word2>, <num-of-word2>, ...]
    word_count = []

    # Process each text from text
    for each_text in text:

        # Get words for each_text, then process each word from the words
        words = each_text.split()
        for word in words:
            word = clean_up(word)

            # Don't accept an empty word
            if word:
                # [ ... <word>, <count> ] -> [ ... <word>, <count>+1 ]
                if word in word_count:
                    word_idx = word_count.index(word)
                    count_idx = word_idx + COUNT_IDX_OFFSET
                    word_count[count_idx] += FOUND_WORD_INCREASE
                # [ ... ] -> [ ... <new-word>, 1 ]
                else:
                    word_count.append(word)
                    word_count.append(FOUND_WORD_INCREASE)

    return word_count


def get_count(word, word_count):
    r"""(str, list of str) -> int

    Return the number of occurrence of word by looking at word_count
    which consists of a pair of word and its occurrence

    >>> get_count('a', ['a', 1, 'b', 2])
    1
    >>> get_count('b', ['a', 1, 'b', 2])
    2
    """
    COUNT_IDX_OFFSET = 1

    if word in word_count:
        return word_count[word_count.index(word) + COUNT_IDX_OFFSET]
    else:
        return 0


def get_words(text):
    r""" (list of str) -> list of str
    Return a list of unique words from text

    >>> get_words(['a','b'])
    ['a', 'b']
    >>> get_words(['a','b','a'])
    ['a', 'b']
    >>> get_words(['a\n','b\n','a\n'])
    ['a', 'b']
    >>> get_words(['!!!\n', 'a\n','b\n','a\n'])
    ['a', 'b']
    >>> get_words(['\n'])
    []
    """

    unique_words = []
    FOUND_WORD_INCREASE = 1
    WORD_COUNT_IDX_OFFSET = 1

    # Process each text from text
    for each_text in text:

        # Get words for each_text, then process each word from the words
        words = each_text.split()
        for word in words:
            word = clean_up(word)

            # Word should not be empty
            if word != "" and word not in unique_words:
                unique_words.append(word)

    return unique_words

##########  Complete the following functions. ############


def avg_word_length(text):
    r""" (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143
    >>> text = ['\nJames Fennimore Cooper\n', '\nPeter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143
    >>> text = ['\nJa!es Fenn@more Cooper\n', '\nPeter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143
    >>> text = ['!!!!!\n', '!a\n' ,'b\n']
    >>> avg_word_length(text)
    1.0
    >>> text = ['!!!!!\n']
    >>> avg_word_length(text)
    0.0

    """
    total_char = 0
    total_words = 0

    # Get only unique words
    words = get_words(text)

    word_count = create_word_count(text)
    # Get the number of chars for each words and save it
    for word in words:
        count = get_count(word, word_count)
        total_char += len(word) * count
        total_words += count

    if len(words):
        # total # of characters /  total # of words
        return total_char / total_words
    else:
        return 0.0


def type_token_ratio(text):
    r""" (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n', 'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    >>> text = ['a\n', 'b\n', 'a\n']
    >>> type_token_ratio(text)
    0.6666666666666666
    >>> text = ['!!;!\n','a\n','b\n', 'a\n', 'b\n', 'a\n']
    >>> type_token_ratio(text)
    0.4
    """

    words_count_total = 0

    # Get only unique words
    words = get_words(text)
    word_count = create_word_count(text)

    # Get number of occurrence for each words and save it
    for word in words:
        words_count_total += get_count(word, word_count)

    # total # of unique words /  total # of words
    return len(words) / words_count_total


def hapax_legomena_ratio(text):
    r""" (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the hapax legomena ratio for text. This ratio is the number of
    words that occur exactly once divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n', 'James Gosling\n']
    >>> hapax_legomena_ratio(text)
    0.7777777777777778
    >>> text = ['A B C\n', 'A B C D']
    >>> hapax_legomena_ratio(text)
    0.14285714285714285
    >>> text = ['A\n']
    >>> hapax_legomena_ratio(text)
    1.0
    >>> text = ['A\n','A\n']
    >>> hapax_legomena_ratio(text)
    0.0
    """

    FOUND_INCREASE = 1

    found_once = []
    found_twice = []

    found_only_once_count = 0
    total_word = 0

    # Process each text from text
    for each_text in text:

        # Get words for each_text, then process each word from the words
        words = each_text.split()
        for word in words:
            word = clean_up(word)
            total_word += FOUND_INCREASE

            # word is first found
            if word not in found_once:
                found_once.append(word)
            else:
                # word is secondly found
                if word in found_once and word not in found_twice:
                    found_twice.append(word)

    # Find the number of words that was found only once
    for once_word in found_once:
        if once_word not in found_twice:
            found_only_once_count += FOUND_INCREASE

    return found_only_once_count/total_word


def split_on_separators(original, separators):
    r""" (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    >>> split_on_separators("Hoo!ray! Fin,ally, we're done.", "!,")
    ['Hoo', 'ray', ' Fin', 'ally', " we're done."]
    >>> split_on_separators("A","!,")
    ['A']
    >>> split_on_separators(" "," ")
    ['', '']
    >>> split_on_separators(" ","A")
    [' ']
    >>> split_on_separators("A"," ")
    ['A']
    """

    result = [original]
    for separator in separators:
        temp = []
        for each_string in result:
            # When a separator is ! and  result is ["A!B", "C!D"]
            #
            # [].extend(["A", "B"]) becomes ["A", "B"]
            # ["A", "B"].extend(["C", "D"]) becomes["A", "B", "C", "D" ]
            temp.extend(each_string.split(separator))
        result = temp

    return result


def avg_sentence_length(text):
    r""" (list of str) -> float

    Precondition: text contains at least one sentence.

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.

    Return the average number of words per sentence in text.

    >>> text = ['The time has come, the Walrus said\n', 'To talk of many things: of shoes - and ships - and sealing wax,\n', 'Of cabbages; and kings.\n', 'And why the sea is boiling hot;\n', 'and whether pigs have wings.\n']
    >>> avg_sentence_length(text)
    17.5
    >>> text = ['The time. Walrus said\n', 'To. talk of many \n']
    >>> avg_sentence_length(text)
    2.6666666666666665
    """

    SENTENCE_SEPARATORS = "!?."
    total_words = 0
    total_sentences = 0

    # Convert text to a single string. Then, get sentences.
    sentences = split_on_separators(" ".join(text), SENTENCE_SEPARATORS)

    # Get the number of words for each sentence
    for sentence in sentences:

        words = get_words(sentence.split("\n"))
        word_count = create_word_count(sentence.split("\n"))

        # Sentence should have at least a word
        if len(words):
            total_sentences += 1
            for word in words:
                total_words += get_count(word, word_count)

    #  total # of words / total # of sentences
    if total_sentences:
        return total_words / total_sentences
    else:
        return 0


def avg_sentence_complexity(text):
    r""" (list of str) -> float

    Precondition: text contains at least one sentence.

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of ,;:

    Return the average number of phrases per sentence in text.

    >>> text = ['The time has come, the Walrus said\n', 'To talk of many things: of shoes - and ships - and sealing wax,\n', 'Of cabbages; and kings.\n', 'And why the sea is boiling hot;\n', 'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    >>> text = ['The time said\n', 'To talk: of shoes. pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    1.5
    """

    SENTENCE_SEPARATORS = "!?."
    PHRASE_SEPARATORS = ",;:"

    total_sentence = 0
    total_phrase = 0

    # Convert text to a single string. Then, get sentences
    sentences = split_on_separators(" ".join(text), SENTENCE_SEPARATORS)

    # Get the number of phrases for each sentence
    for sentence in sentences:
        phrases = split_on_separators(sentence, PHRASE_SEPARATORS)

        words = get_words(phrases)

        # A phrase must have at least one word
        if len(words):
            total_sentence += 1
            total_phrase += len(phrases)

    return total_phrase/total_sentence


def compare_signatures(sig1, sig2, weight):
    r""" (list, list, list of float) -> float

    Return a non-negative float indicating the similarity of the two
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.

    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007

    >>> sig1 = ["a_stng" , 2.4, 0.1, 0.02, 13.0, 2.0]
    >>> sig2 = ["a_stng2", 2.3, 0.1, 0.01, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    10.8
    """
    FIRST_FEATURE_IDX = 1
    LAST_FEATURE_IDX = 5
    RANGE_OFFSET = 1

    similarity = 0

    # similarity == abs(diffence of each feature) * corresponding weight
    for feature in range(FIRST_FEATURE_IDX, LAST_FEATURE_IDX + RANGE_OFFSET):
        abs_sig1_sig2 = abs(sig1[feature] - sig2[feature])
        similarity += abs_sig1_sig2 * weight[feature]

    return similarity

import doctest
doctest.testmod()
