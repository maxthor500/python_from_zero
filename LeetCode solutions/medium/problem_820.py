
def minimumLengthEncoding(words):
    words_set = set(words)
    for word in words:
        if word in words_set:
            for i in range(1, len(word)):
                words_set.discard(word[i:])
    return len("#".join(list(words_set))) + 1
