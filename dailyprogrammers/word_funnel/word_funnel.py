def word_funnel(first_word, second_word):
    words = set()

    for i in range(len(first_word)):
        words.add(first_word[:i] + first_word[i + 1:])
    return second_word in words
